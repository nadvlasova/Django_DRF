import React from 'react'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.link_to_repo}</td>
            <td>{project.users_list}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table className="table">
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Link</th>
                <th>Users_list</th>
            </tr>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}

export default ProjectList