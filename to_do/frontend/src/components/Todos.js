import React from 'react'


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.name_project}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.creators}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
        <table className="table">
            <tr>
                <th>Name Project</th>
                <th>Text</th>
                <th>Date Create</th>
                <th>Date Update</th>
                <th>Creators</th>
                <th>Active</th>
            </tr>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList