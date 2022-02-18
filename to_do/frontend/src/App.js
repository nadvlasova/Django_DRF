import React from 'react';
import logo from './logo.svg';

import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'
import UserList from "./components/User.js";
import ProjectList from "./components/Projects";
import TodoList from "./components/Todos";
import Navbar from "./components/Menu.js";
import Footer from "./components/Footer.js";
import TodoListUser from "./components/TodosUser";
import NotFound404 from "./components/NotFound404";
import axios from "axios";
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from "react-router-dom";

const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            navbarItems: [
                {name: 'Users', href: '/'},
                {name: 'Projects', href: '/projects'},
                {name: 'Todos', href: '/todos'},

            ],
            'users': [],
            'projects': [],
            'todos': []

        }
    }

    componentDidMount() {
        axios.get(get_url('usersapp/'))
            .then(response => {
                this.setState({users: response.data})
            }).catch(error => console.log(error))

        axios.get(get_url('projects/'))
            .then(response => {
                this.setState({projects: response.data})
            }).catch(error => console.log(error))

        axios.get(get_url('todos/'))
            .then(response => {
                this.setState({todos: response.data})
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <header>
                        <Navbar navbarItems={this.state.navbarItems}/>
                    </header>
                    <main role="main" class="flex-shrink-0">
                        <div className="container">
                            {/*<HashRouter>*/}
                            <Switch>
                                <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                                <Route exact path='/projects'
                                       component={() => <ProjectList projects={this.state.projects}/>}/>
                                <Route exact path='/todos' component={() => <TodoList todos={this.state.todos}/>}/>

                                <Route path='/user/:id'>
                                    <TodoListUser todos={this.state.todos} creators={this.state.creators}/>
                                </Route>

                                <Redirect from='/1' to='/' />
                                <Route component={NotFound404}/>
                            </Switch>
                            {/*</HashRouter>*/}
                        </div>
                    </main>
                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
