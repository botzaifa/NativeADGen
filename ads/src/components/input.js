import React, { useState } from 'react';
import axios from 'axios'; // For making HTTP requests

const App = () => {
  const [companyName, setCompanyName] = useState('');
  const [productInfo, setProductInfo] = useState('');
  const [theme, setTheme] = useState('');
  const [adType, setAdType] = useState('');
  const [tagline, setTagline] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Prepare the data to send to the backend
    const data = {
      companyName,
      productInfo,
      theme,
      adType,
      tagline
    };

    // Send POST request to Flask backend
    try {
      const response = await axios.post('http://127.0.0.1:5000/save-data', data);
      console.log('Data submitted:', response.data);
      // Reset the form after successful submission
      setCompanyName('');
      setProductInfo('');
      setTheme('');
      setAdType('');
      setTagline('');
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <div>
      <h1>Ad Information Form</h1>
      <form onSubmit={handleSubmit}>
        <label>Company Name:</label>
        <input type="text" value={companyName} onChange={(e) => setCompanyName(e.target.value)} required />
        <br />
        <label>Product Information:</label>
        <input type="text" value={productInfo} onChange={(e) => setProductInfo(e.target.value)} required />
        <br />
        <label>Theme:</label>
        <input type="text" value={theme} onChange={(e) => setTheme(e.target.value)} required />
        <br />
        <label>Type of Ad:</label>
        <input type="text" value={adType} onChange={(e) => setAdType(e.target.value)} required />
        <br />
        <label>Tagline (optional):</label>
        <input type="text" value={tagline} onChange={(e) => setTagline(e.target.value)} />
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default App;
