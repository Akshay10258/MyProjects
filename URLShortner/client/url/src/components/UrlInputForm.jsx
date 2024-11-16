import { useState } from 'react';

const UrlInputForm = () => {
    const [url, setUrl] = useState('');
    const [error, setError] = useState('');
    const [shortId, setShortId] = useState('');
    const [analytics,setAnalytics]=useState('')

    const handleInputChange = (e) => {
        setUrl(e.target.value);
    };
    const getAnalytics=async() => {
        try {
            const res = await fetch(`http://localhost:3000/url/analytics/${shortId}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!res.ok) {
                throw new Error('Could not get response');
            }

            const result = await res.json();
            console.log('got analytics:', result);

            // Save the shortId for redirection link
            setAnalytics(result);
            setError('');
        } catch (err) {
            console.error('Error getting analytics:', err);
            setError('There was an error');
        }
    }
    
    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!url) {
            setError('Please enter a URL');
            return;
        }

        try {
            const data = { url };

            const res = await fetch('http://localhost:3000/url', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!res.ok) {
                throw new Error('Could not get response');
            }

            const result = await res.json();
            console.log('URL submitted successfully:', result);

            // Save the shortId for redirection link
            setShortId(result.id);
            setError('');
        } catch (err) {
            console.error('Error submitting URL:', err);
            setError('There was an error submitting the URL');
        }
    };

    return (
        <div className="url-form-container">
            <form onSubmit={handleSubmit}>
                <div style={{ display: 'flex', justifyContent: 'center', margin: '200px' }}>
                    <input
                        type="text"
                        value={url}
                        onChange={handleInputChange}
                        placeholder="Enter URL"
                        style={{
                            border: '2px solid #333',
                            padding: '10px',
                            width: '100%',
                            maxWidth: '500px',
                        }}
                        required
                    />
                    <button type="submit">Submit</button>
                </div>
            </form>

            {error && <p className="error">{error}</p>}

            {/* Display the short URL link when shortId is available */}
            {shortId && (
                <div style={{ textAlign: 'center', marginTop: '20px',fontSize: '50px', }}>
                    <p>Shortened URL:</p>
                    <a
                        href={`http://localhost:3000/${shortId}`}
                        target="_blank"
                        style={{
                            fontSize: '50px',
                            color: '#007BFF',
                            textDecoration: 'none',
                            fontWeight: 'bold',
                        }}
                    >
                        http://localhost:3000/{shortId}
                    </a><br></br>
                    <button style={{width:'100px',height:'60px'}} onClick={()=>{getAnalytics()}}>Get analytics</button>
                </div>

            
            )}
            {analytics &&(
                <div style={{ textAlign: 'center', marginTop: '20px',fontSize: '50px', }}>
                    <div>Total Clicks : {analytics.totalClicks}</div>
                </div>
            )}

            
        </div>
    );
};

export default UrlInputForm;
