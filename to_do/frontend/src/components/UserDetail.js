import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.id}</td>
            <td>{user.username}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>

        </tr>
    )
}


            {users.map((user) => <UserItem user={user} deleteUser={deleteUser}/>)}
