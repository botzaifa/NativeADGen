import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [formData, setFormData] = useState({
    companyName: '',
    productInfo: '',
    theme: '',
    adType: '',
    tagline: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const { companyName, productInfo, theme, adType, tagline } = formData;
      const slug = `/${companyName}/${productInfo}/${theme}/${adType}/${tagline}`; 

      const response = await axios.post(`http://127.0.0.1:5000/save-data${slug}`);
      console.log('Data submitted:', response.data);
      setFormData({
        companyName: '',
        productInfo: '',
        theme: '',
        adType: '',
        tagline: ''
      });
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  return (
    <div>
      <h1>Ad Information Form</h1>
      <form onSubmit={handleSubmit}>
        <label>Company Name:</label>
        <input type="text" name="companyName" value={formData.companyName} onChange={handleChange} required />
        <br />
        <label>Product Information:</label>
        <input type="text" name="productInfo" value={formData.productInfo} onChange={handleChange} required />
        <br />
        <label>Theme:</label>
        <input type="text" name="theme" value={formData.theme} onChange={handleChange} required />
        <br />
        <label>Ad Type:</label>
        <input type="text" name="adType" value={formData.adType} onChange={handleChange} required />
        <br />
        <label>Tagline (optional):</label>
        <input type="text" name="tagline" value={formData.tagline} onChange={handleChange} />
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default App;