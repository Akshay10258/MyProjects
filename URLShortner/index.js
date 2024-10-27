const express = require("express");
const { connectToMongoDB } = require('./connect')
const urlRoute = require('./routes/url')
const URL = require('./models/url');

const app = express();
const PORT = 3000;

connectToMongoDB("mongodb://localhost:27017/short-url")
.then (()=> console.log("MongoDB connected"))

app.use(express.json())
app.use("/url" , urlRoute)

app.get('/:shortId', async (req, res) => {
    const ShortId = req.params.shortId;

    console.log(ShortId);
    console.log("hello")
    const entry = await URL.findOne(
        {
            shortId : ShortId,
        }
    //     {
    //         $push: {
    //         visitHistory: {
    //             timestamp: Date.now(),
    //         },
    //         },
    //     }
        );
        res.redirect(entry.redirectURL);
    });

app.listen(PORT , ()=> console.log(`Server started at port : ${PORT}`))