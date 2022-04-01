import React from 'react';
// import logo from './logo.svg';
import {Route, Link, Switch, Redirect, BrowserRouter as Router} from "react-router-dom";

import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'

import UserList from "./components/User.js";
// import {UserList, UserDetail} from "./components/User.js";
import {ProjectList, ProjectDetail} from "./components/Projects.js";
import TodoList from "./components/Todos.js";
import Navbar from "./components/Menu.js";
import Footer from "./components/Footer.js";
import NotFound404 from "./components/NotFound404.js";
import LoginForm from "./components/Auth.js";
import axios from "axios";
import Cookies from 'universal-cookie';
import ProjectForm from "./components/ProjectForm";
import TODOForm from "./components/TodoForm";


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
            'todos': [],
            'token': '',

        }
    }

    createProject(name, link_to_repo, user) {
        const headers = this.get_headers()
        const data = {name: name, link_to_repo: link_to_repo, users_list: user}
        axios.post('http://127.0.0.1:8000/api/projects/', data, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({projects: []})

        })

    }

    createTODO(name_project, text, creator) {
        const headers = this.get_headers()
        const data = {name_project: name_project, text: text, creator: creator}
        axios.post('http://127.0.0.1:8000/api/todos/', data, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({todos: []})

        })

    }


    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }

    deleteTODO(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todos/${id}`, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
        // this.setState({'token': token})
        // console.log(this.set_token)
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_cookies() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        console.log(token)
        this.setState({'token': token}, () => this.load_data())
        // this.setState({'token': token})
    }


    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
                console.log(response.data)
            }).catch(error => alert('Неверный логин или пароль!'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json',
            // 'Accept': 'application/json; version=v'
        }
        // console.log(this.is_authenticated())
        if (this.is_authenticated()) {
            // console.log(`Token ${this.state.token}`)
            headers['Authorization'] = `Token ${this.state.token}`
        }
        return headers
    }

    getProject(id) {
        axios.get(get_url(`projects/${id}`))
            .then(response => {
                // console.log(response.data)
                this.setState({project: response.data})
            }).catch(error => console.log(error))
    }

    load_data() {
        const headers = this.get_headers()
        console.log(this.get_headers())
        axios.get(get_url('usersapp/'), {headers})
            .then(response => {
                this.setState({users: response.data})
            }).catch(error => {
            console.log(error)
            this.setState({'users': []})
        })

        axios.get(get_url('projects/'), {headers})
            .then(response => {
                this.setState({projects: response.data})
            }).catch(error => {
            console.log(error)
            this.setState({'projects': []})
        })

        axios.get(get_url('todos/'))
            .then(response => {
                this.setState({todos: response.data})
            }).catch(error => {
            console.log(error)
            this.setState({'todos': []})
        })
    }

    componentDidMount() {
        this.get_token_from_cookies()
        // this.load_data()
    }

    render() {
        return (
            <div>
                <Router>
                    <header>
                        {/*<Navbar navbarItems={this.state.navbarItems}/>*/}
                        <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-warning">
                            <a className="navbar-brand" href="#">GeekBrains</a>
                            <ul className="navbar-nav mr-auto">
                                <li><Link to='/'>Users</Link></li>
                                <li><Link to='/projects'>Projects</Link></li>
                                <li><Link to='/todos'>Todos</Link></li>
                                <li> {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>}
                                </li>
                            </ul>
                        </nav>
                    </header>
                    <main role="main" class="flex-shrink-0">
                        <div className="container">
                            <Switch>
                                {/*<Route exact path='/'> <UserList users={this.state.users}/> </Route>*/}

                                <Route exact path='/' component={() => <UserList users={this.state.users}
                                                                                 deleteUser={(id) => this.deleteUser(id)}/>}/>


                                <Route exact path='/projects'> <ProjectList projects={this.state.projects}
                                                                            deleteProject={(id) => this.deleteProject(id)}/></Route>

                                <Route exact path='/projects/create'> <ProjectForm users_list={this.state.users}
                                                                                   createProject={(name, link_to_repo, user) => this.createProject(name, link_to_repo, user)}/></Route>


                                <Route exact path='/todos'> <TodoList todos={this.state.todos}
                                                                      deleteTODO={(id) => this.deleteTODO(id)}/></Route>
                                <Route exact path='/todos/create'> <TODOForm todos={this.state.todos}
                                                                             createTODO={(name_project, text, creator) => this.createTODO(name_project, text, creator)}/></Route>


                                <Route exact path='/login'> <LoginForm get_token={(username,
                                                                                   password) => this.get_token(username, password)}/>
                                </Route>


                                <Route path="/project/:id"
                                       children={<ProjectDetail getProject={(id) => this.getProject(id)}
                                                                item={this.state.project}/>}/>

                                <Redirect from='/projects' to='/project/project:id'/>
                                <Redirect from='/' to='/user:id'/>

                                <Route component={NotFound404}/>
                            </Switch>
                        </div>
                    </main>
                    <Footer/>
                </Router>
            </div>
        )
    }
}

export default App;
