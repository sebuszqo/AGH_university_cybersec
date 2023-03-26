//W powyższym skrypcie została utworzona klasa Counter, która rozszerza React. Component i implementuje metody constructor, decrement, componentDidMount oraz render. Klasa ta reprezentuje pojedynczy licznik, który jest wyświetlany na stronie jako element <span> z wartością licznika. W konstruktorze klasy ustawiana jest początkowa wartość licznika, która pobierana jest z pola formularza o identyfikatorze counter

import React from 'react';
import ReactDOM from 'react-dom';

class Counter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            counter: document.getElementById('counter').valueAsNumber,
        };
    }

    decrement() {
        if (this.state.counter <= 0) {
            return 0;
        }

        this.setState({
            counter: this.state.counter - 1,
        });
    }

    componentDidMount() {
        setInterval(this.decrement.bind(this), 1000);
    }

    render() {
        return <span>{this.state.counter}</span>;
    }
}

const element = <Counter></Counter>;
ReactDOM.render(element, document.getElementsByClassName('mx-auto')[0]);
