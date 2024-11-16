const express = require("express");
const { connectToMongoDB } = require('./connect');
const urlRoute = require('./routes/url');
const URL = require('./models/url');
const cors = require("cors");

const app = express();
const PORT = 3000;

// Connect to MongoDB
connectToMongoDB("mongodb://localhost:27017/short-url")
    .then(() => console.log("MongoDB connected"));

app.use(cors());

app.use(express.json());
app.use("/url", urlRoute);

// Redirect handler for short URLs
app.get('/:shortId', async (req, res) => {
    const ShortId = req.params.shortId;
    console.log(ShortId);
    console.log("hello");

    try {
        const entry = await URL.findOne({ shortId: ShortId });

        if (!entry) {
            return res.status(404).json({ message: 'URL not found' });
        }

        await URL.updateOne(
            { shortId: ShortId },
            { $push: { visitHistory: { timestamp: Date.now() } } } // Push the new visit history
        );

        // Redirect to the stored URL
        res.redirect(entry.redirectURL);
    } catch (error) {
        console.error("Error occurred:", error);
        res.status(500).json({ message: 'Server error' });
    }
});


// Start server
app.listen(PORT, () => console.log(`Server started at port: ${PORT}`));
