import React from 'react'


class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {login: '', password: ''}  // состояние, в котором будут храниться login и password
    }
    //event.target — это input, name будет либо login, либо password, а value — соответствующее введённое значение
    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    // связываем этот метод с input’ами
    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="login" placeholder="login" value={this.state.login}
                       onChange={(event) => this.handleChange(event)}/>
                <input type="password" name="password" placeholder="password" value={this.state.password}
                       onChange={(event) => this.handleChange(event)}/>
                <input type="submit" value="Login"/>
            </form>
        );
    }
}

export default LoginForm
