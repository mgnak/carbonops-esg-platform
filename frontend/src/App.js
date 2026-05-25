import React, { useState } from 'react';
import axios from 'axios';

const API_BASE = 'http://127.0.0.1:8000/api';

function App() {
  const [file, setFile] = useState(null);
  const [sourceType, setSourceType] = useState('sap_fuel');
  const [message, setMessage] = useState('');

  const handleUpload = async () => {
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append('file', file);
    formData.append('source_type', sourceType);

    try {
      const res = await axios.post(`${API_BASE}/upload/`, formData);
      setMessage(res.data.message);
    } catch (err) {
      setMessage("Upload failed: " + err.response?.data?.error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-8">CarbonOps - ESG Data Ingestion</h1>

      <div className="max-w-md bg-white p-6 rounded-xl shadow">
        <h2 className="text-xl mb-4">Upload Data</h2>
        
        <select 
          className="w-full p-3 border mb-4"
          value={sourceType} 
          onChange={(e) => setSourceType(e.target.value)}
        >
          <option value="sap_fuel">SAP Fuel & Procurement</option>
          <option value="utility_electricity">Utility Electricity</option>
          <option value="corporate_travel">Corporate Travel</option>
        </select>

        <input 
          type="file" 
          onChange={(e) => setFile(e.target.files[0])}
          className="mb-4 block w-full"
        />

        <button 
          onClick={handleUpload}
          className="bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-700 w-full"
        >
          Upload & Process
        </button>

        {message && <p className="mt-4 text-green-600">{message}</p>}
      </div>
    </div>
  );
}

export default App;