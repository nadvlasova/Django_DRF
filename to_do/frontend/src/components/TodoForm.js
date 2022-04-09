import React from "react";
import projects from "./Projects";

class TODOForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name_project: {}, text: '', creator: []}
    }

    handleTODOChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'project': {}
            })
            return;
        }
        let projects = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            projects.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'project': projects
        })
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
                    <label htmlFor="project">Проект</label>
                    <select className="select" name="name_project" multiple
                            onChange={(event) => this.handleChange(event)}>
                        {this.props.todos.map((item) => <option value={item.id}> {item.name_project.name}</option>)}

                    </select>
                </div>
                <div className="form-group">
                    <label for="text">Содержание</label>
                    <input type="text" className="form-control" name="text"
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="creator">Создатель</label>
                    <select className="select" name="creator" multiple
                            onChange={(event) => this.handleChange(event)}>
                        {this.props.todos.map((item) => <option value={item.id}> {item.creator}</option>)}
                    </select>
                </div>
                {/*<div className="form-group">*/}
                {/*    <label htmlFor="date_create">Сформирована</label>*/}
                {/*    <input type="datetime-local" className="form-control" name="date_create"*/}
                {/*           onChange={(event) => this.handleChange(event)}/>*/}
                {/*</div>*/}
                {/*<div className="form-group">*/}
                {/*    <label htmlFor="date_update">Обновлена</label>*/}
                {/*    <input type="datetime-local" className="form-control" name="date_update"*/}
                {/*           onChange={(event) => this.handleChange(event)}/>*/}
                {/*</div>*/}
                <input type="submit" className="btn btn-primary btn-lg btn-block" value="Save"/>
            </form>
        );
    }
}

export default TODOForm