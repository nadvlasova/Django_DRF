import React from 'react'
import {Link, useParams} from "react-router-dom";



const ProjectListItem = ({project, deleteProject}) => {
    let link_to = `/project/${project.id}`
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td><Link to={project.link_to_repo}>{project.link_to_repo}</Link></td>
            <td>{project.users_list}</td>
            <td><Link to={link_to}>Detail</Link></td>
            <td>
                <button onClick={() => deleteProject(project.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

export const ProjectList = ({projects, deleteProject}) => {
    return (
        <div>
            <table className="table">
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Repository</th>
                    <th>Users_list</th>
                    <th>Detail</th>
                </tr>
                {projects.map((project) => <ProjectListItem project={project} deleteProject={deleteProject}/>)}
            </table>
            <Link to={'/projects/create'}>Create</Link>
        </div>
    )
}

const ProjectUserItem = ({user}) => {
    // console.log(item)
    return (
        <li>
            {user.username} ({user.email}
        </li>
    )
}

export const ProjectDetail = ({getProject, item}) => {
    let {id} = useParams();
    getProject(id)
    let users = item.users ? item.users : []
    console.log(id)
    return (
        <div>
            <h1>{item.name}</h1>
            Repository: <a href={item.link_to_repo}>{item.link_to_repo}</a>
            <p>Users:</p>
            <ol>
                {users.map((user) => <ProjectUserItem user={user}/>)}
            </ol>
        </div>
    )
}

export default {ProjectList, ProjectDetail}
// export default ProjectList
