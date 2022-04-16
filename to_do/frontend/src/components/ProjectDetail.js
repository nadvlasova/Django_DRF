import React from 'react';
import {useParams} from 'react-router-dom';


const ProjecDetailItem = ({project}) => {
    return (
        <tr>

            <td className="Line">
                {project.name}
            </td>

            <td class="Line">
                {project.id}
            </td>

        </tr>
    )
}


const ProjectDetail = ({projects}) => {
    const params = useParams();
    console.log(params)
    // let {id} = useParams();

    // let project = projects.find((project) => project.id == id);

    return (
        <div>
            <h1>{params.name}</h1>
            <a href={params.link_to_repo}>Repository:</a>
            <p>Users: {params.users_list}</p>
            <ol>
                {projects.map((item) => <ProjectDetail item={item}/>)}
            </ol>
        </div>
    )
}

export default ProjectDetail;