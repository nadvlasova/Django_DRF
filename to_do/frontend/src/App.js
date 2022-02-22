import React from 'react';
import logo from './logo.svg';
import {Route, Link, Switch, Redirect, BrowserRouter as Router} from "react-router-dom";

import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'

import UserList from "./components/User.js";
import {ProjectList, ProjectDetail} from "./components/Projects.js";
import TodoList from "./components/Todos.js";
import Navbar from "./components/Menu.js";
import Footer from "./components/Footer.js";
import NotFound404 from "./components/NotFound404.js";
import axios from "axios";


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
            'project': [],
            'todos': []

        }
    }

    getProject(id) {
        axios.get(get_url(`projects/${id}`))
            .then(response => {
                console.log(response.data)
                this.setState({project: response.data})
            }).catch(error => console.log(error))
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
                <Router>
                    <header>
                        <Navbar navbarItems={this.state.navbarItems}/>
                    </header>
                    <main role="main" class="flex-shrink-0">
                        <div className="container">
                            <Switch>
                                <Route exact path='/'> <UserList users={this.state.users}/> </Route>

                                <Route exact path='/projects'> <ProjectList projects={this.state.projects}/></Route>

                                <Route exact path='/todos'>  <TodoList todos={this.state.todos}/> </Route>


                                <Route path="/project/:id"
                                       children={<ProjectDetail getProject={(id) => this.getProject(id)}
                                                                item={this.state.project}/>}/>

                                <Redirect from='/projects' to='/project/project:id'/>

                                <Route component={NotFound404}/>
                            </Switch>
                        </div>
                    </main>
                    <Footer/>
                </Router>
                // </div>
        )
    }
}

export default App;
