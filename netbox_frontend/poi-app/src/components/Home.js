import React from 'react';
import Typing from 'react-typing-effect';

const Home = () => (
    <div className="center-container">
         {/* Decidi usar o componente Typing da biblioteca react-typing-effect para criar um efeito de digitação animado.
            Isso melhora a experiência do usuário ao adicionar uma animação visualmente atraente à página inicial. */}
        <Typing
            text={[
                "Bem-vindo ao POI App",
                "Escolha uma opção no menu para começar."
            ]}
            speed={100}
            eraseDelay={2000}
            typingDelay={500}
            cursorClassName="typing-cursor"
            className="typing-text"
        />
    </div>
);

export default Home;
