import React from 'react'
import {Link, useParams} from "react-router-dom";


const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.id}</td>
            <td> <Link to={`/user/${user.id}`} > {user.username}</Link> </td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>
                <button type='button'>Delete</button>
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className="table">
            <tr>
                <th>ID</th>
                <th>Login</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
            </tr>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}


export default UserList
