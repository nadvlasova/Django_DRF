import React from 'react'
import {Link} from "react-router-dom";
import Projects from "./Projects";


const TodoItem = ({todo, deleteTODO}) => {
    return (
        <tr>
            <td key={todo.id}>{todo.name_project.name}</td>
            <td key={todo.id}>{todo.text}</td>
            <td key={todo.id}>{todo.date_create}</td>
            <td key={todo.id}>{todo.date_update}</td>
            <td key={todo.id}>{todo.creator}</td>
            {/*<td>{todo.is_active}</td>*/}
            <td>
                <button onClick={() => deleteTODO(todo.id)} type='button'>Open</button>
            </td>
        </tr>
    )
}

const TodoList = ({todos, deleteTODO}) => {
    return (
        <div>
            <table className="table">
                <tr>
                    <th>Name Project</th>
                    <th>Text</th>
                    <th>Date Create</th>
                    <th>Date Update</th>
                    <th>Creators</th>
                    <th>Active</th>
                </tr>
                {todos.map((todo) => <TodoItem todo={todo} deleteTODO={deleteTODO}/>)}
            </table>
            <Link to={'/todos/create'}>Create</Link>
        </div>
    )
}

export default TodoList