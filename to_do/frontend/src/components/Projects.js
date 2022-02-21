import React from 'react'
import {Link, useParams} from "react-router-dom";
// import {Link} from "react-router-dom";


const ProjectListItem = ({project}) => {
    let link_to = `/project/${project.id}`
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.link_to_repo}</td>
            <td><Link to={link_to}>Detail</Link></td>
        </tr>
    )
}

export const ProjectList = ({projects}) => {
    return (
        <table className="table">
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Repository</th>
                <th>Users_list</th>
            </tr>
            {projects.map((project) => <ProjectListItem project={project}/>)}
        </table>
    )
}

const ProjectUserItem = ({item}) => {
    return (
        <li>
            {item.username} ({item.email}
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
            <p>1</p>
            Users:
            <ol>
                {users.map((user) => <ProjectUserItem item={user}/>)}
            </ol>
        </div>
    )
}

export default {ProjectList, ProjectDetail}
// export default ProjectList
