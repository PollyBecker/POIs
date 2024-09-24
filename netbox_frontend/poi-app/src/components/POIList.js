import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Tooltip as ReactTooltip } from 'react-tooltip';
import 'react-tooltip/dist/react-tooltip.css';

const POIList = () => {
    const [pois, setPOIs] = useState([]);

    useEffect(() => {
        fetchPOIs();
    }, []);

    const fetchPOIs = async () => {
        const response = await axios.get('http://127.0.0.1:8000/pois/');
        setPOIs(response.data);
    };

    return (
        <div>
            <h2>Lista de POIs</h2>
            <ul>
                {pois.map((poi) => (
                    <li key={poi.id}>
                        <div data-tooltip-id={`tooltip-${poi.id}`} data-tooltip-content={poi.description}>
                            {poi.name} (x={poi.x}, y={poi.y})
                        </div>
                        <ReactTooltip id={`tooltip-${poi.id}`} />
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default POIList;
