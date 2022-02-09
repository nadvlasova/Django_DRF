import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import axios from "axios";
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],

        };
    }

    componentDidMount() {

        axios.get('http://127.0.0.1:8000/api/usersapp/').then(response => {
            // const users = response.data
            this.setState(
                {
                    'users': response.data
                }
            )
        }).catch(error => console.log(error))


    }

    render() {
        return (<div>
                <div>
                    <Menu/>
                </div>

                <div>
                    <UserList users={this.state.users}/>
                </div>

                <div>
                    <Footer/>
                </div>
            </div>
        );
    }
}

export default App;
