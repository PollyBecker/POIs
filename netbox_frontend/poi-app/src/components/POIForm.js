import React, { useState } from 'react';
import axios from 'axios';

const POIForm = () => {
    // Decidi gerenciar o estado do formulário e do POI criado com o hook useState.
    const [formData, setFormData] = useState({ name: '', x: '', y: '', description: '' });
    const [createdPOI, setCreatedPOI] = useState(null);

    // Decidi usar uma função handleChange para atualizar o estado do formulário.
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); // Previne o comportamento padrão do formulário
        try {
            // Decidi utilizar axios para fazer a requisição POST.
            // Axios é uma biblioteca popular que simplifica as requisições HTTP e oferece melhor suporte a promessas.
            const response = await axios.post('http://127.0.0.1:8000/pois/', formData);
            setCreatedPOI(response.data.poi); // Atualizo o estado com o POI criado
        } catch (error) {
            // Decidi fornecer feedback ao usuário em caso de erro.
            if (error.response && error.response.data.message) {
                alert(error.response.data.message); // Mensagem de erro específica
            } else {
                alert('Ocorreu um erro ao criar o POI.'); // Mensagem de erro genérica
            }
        }
    };

    return (
        <div>
            <h2>Cadastrar nova POI</h2>
            <form onSubmit={handleSubmit}>
                {/* Decidi usar inputs controlados para garantir que o estado do formulário esteja sempre sincronizado com os valores dos inputs. */}
                <input type="text" name="name" placeholder="Nome" onChange={handleChange} required />
                <input type="text" name="description" placeholder="Descrição" onChange={handleChange} required />
                <input type="number" name="x" placeholder="Coordenada X" onChange={handleChange} required />
                <input type="number" name="y" placeholder="Coordenada Y" onChange={handleChange} required />
                <button type="submit">Cadastrar POI</button>
            </form>
            {createdPOI && (
                <div>
                    <h3>POI Criado:</h3>
                    <p><strong>Nome:</strong> {createdPOI.name}</p>
                    <p><strong>Descrição:</strong> {createdPOI.description}</p>
                    <p><strong>Coordenada X:</strong> {createdPOI.x}</p>
                    <p><strong>Coordenada Y:</strong> {createdPOI.y}</p>
                </div>
            )}
        </div>
    );
};

export default POIForm;
