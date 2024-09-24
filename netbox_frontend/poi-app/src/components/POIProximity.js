import React, { useState } from 'react';
import axios from 'axios';

const POIProximity = () => {
  const [formData, setFormData] = useState({ x: '', y: '', max_distance: '' });
  const [results, setResults] = useState([]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/pois/proximidade/', formData);
      setResults(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
    <h2>Encontre as POIs perto de você</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" name="x" placeholder="Coordenada X" onChange={handleChange} required />
        <input type="number" name="y" placeholder="Coordenada Y" onChange={handleChange} required />
        <input type="number" name="max_distance" placeholder="Distância Máxima" onChange={handleChange} required />
        <button type="submit">Buscar POIs</button>
      </form>
      <ul>
        {results.map((poi) => (
          <li key={poi.id}>{poi.name} (X: {poi.x}, Y: {poi.y})</li>
        ))}
      </ul>
    </div>
  );
};

export default POIProximity;
