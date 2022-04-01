import React from "react";

class TODOForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name_project: '', text: '', creator: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
        console.log(event.target.name, event.target.value)
    }

    handleSubmit(event) {
        this.props.createTODO(this.state.name_project, this.state.text, this.state.creator)
        console.log(this.state.name_project)
        console.log(this.state.text)
        console.log(this.state.creator)
        event.preventDefault()
    }


    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">Название проекта</label>
                    <input type="text" className="form-control" name="name_project"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="text">Содержание</label>
                    <input type="text" className="form-control" name="text"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="creator">Создатель</label>
                    <input type="number" className="form-control" name="creator"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default TODOForm