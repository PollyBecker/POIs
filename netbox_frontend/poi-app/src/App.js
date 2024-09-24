import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import POIForm from './components/POIForm';
import POIList from './components/POIList';
import POIProximity from './components/POIProximity';
import './App.css';
import Home from './components/Home'; 

const App = () => {
    return (
        <Router>
            <div className="container">
                <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=ff91a4&height=120&section=header" alt="Header" />
                <h1><Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>POI App</Link></h1>
                <Routes>
                    <Route exact path="/" element={<Home />} />
                    <Route exact path="/create" element={<POIForm />} />
                    <Route path="/list" element={<POIList />} />
                    <Route path="/proximity" element={<POIProximity />} />
                </Routes>
                <nav>
                    <ul>
                        <li><Link to="/create">Cadastrar POI</Link></li>
                        <li><Link to="/list">Lista de POIs</Link></li>
                        <li><Link to="/proximity">POIs perto de você</Link></li>
                    </ul>
                </nav>
            </div>
        </Router>
    );
};

export default App;
