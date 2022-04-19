import React from 'react'
import {Link} from "react-router-dom";



const TodoItem = ({todo, deleteTODO}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.name_project}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.creator}</td>
            {/*<td>{todo.is_active.value}</td>*/}

            <td>

                    <button onClick={() => deleteTODO(todo.id)} type='button'>Open </button>

            </td>
        </tr>
    )
}

const TodoList = ({todos, deleteTODO}) => {
    return (
        <div>
            <table className="table">
                <tr>
                    <th>ID</th>
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