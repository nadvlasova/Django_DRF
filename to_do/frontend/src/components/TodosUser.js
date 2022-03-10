import React from "react";
import { useParams} from "react-router-dom";



const TodoItem = ({todo, creators}) => {
    return (
        <tr>
            <td>{todo.name_project}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.creators.map((creatorID) => {return creators.find((creators) => creators.id === creatorID).username})}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}

const TodoListUser = ({todos, creators}) => {

    let { id } = useParams()
    console.log(id)

    let filtered_item = todos.filter((todo => todo.creators.includes(parseInt(id))))

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
            {filtered_item.map((todo) => <TodoItem todo={todo} creators={creators}/>)}
        </table>
    )
}

export default TodoListUser;