import React, {Component, useEffect} from 'react';
import {Link, useParams} from 'react-router-dom';
import projects from "./Projects";
import {jsx} from "react/cjs/react-jsx-runtime.profiling.min";


// export const ProjectDetail.jsx : useEffect(() => {getProject(id).then(setProject) }, [item.id]) {
//     let {id} = useParams();
//     getProject(id)
//
//     return (
//         <div>
//             <h2>{item.name}</h2>
//             <p>{item.link_to_repo}</p>
//             <p>Users: {item.users_list}</p>
//             <ol>
//                 {/*{projects.map((item) => <ProjectDetail item={item}/>)}*/}
//             </ol>
//         </div>
//     )
//
// }
// export default ProjectDetail


export const ProjectDetail = ({getProject, item}) => {
    let {id} = useParams();
    useEffect(() => getProject(id), [id])

    return (
        <div>
            <h2>{item.name}</h2>
            <p>{item.link_to_repo}</p>
            <p>Users: {item.users_list}</p>
            <ol>
                {/*{projects.map((item) => <ProjectDetail item={item}/>)}*/}
            </ol>
        </div>
    )

}
export default ProjectDetail






// export default class ProjectDetail extends Component {
//
//     render () {
//         return (
//             <divv>
//                 <p>test</p>
//                 <p></p>
//                 {/*<p>{this.props.projects}</p>*/}
//                 <p>test</p>
//             </divv>
//         )
//     }
// }


// const ProjectDetail = ({projects, getProject}) => {
//     // const id = useParams();
//     let project = projects.find(project => {
//         return project.id === getProject
//
//     })
//
//     console.log(project)
// }
//
// export default ProjectDetail

// class ProjectDetail extends React.Component {
// constructor(props) {
//     super(props);
//     this.state = {name: '', link_to_repo: '', users_list: []}
// }
//
// render() {
//     return (
//         <div>
//             <td>1</td>
//             <td>2</td>
//             <td>3</td>
//         </div>
//     );
// }
// }

// export default ProjectDetail;

// const ProjectDetail = ({ match }) => {
//     const {
//         params: { id },
//     } = match;
//     const project = projects.find(({ id }) => id === project.id);
//
//     return (
//         <div>
//             id: <strong>{project.name}</strong>
//             <p>{project.description}</p>
//         </div>
//     );
// };
// export default ProjectDetail;

// const ProjectDetailItem = ({projects}) => {
//     const id = useParams();
//     // project = getProject(id)
//     let item = projects.find((project) => project.id === id);
//     // console.log(project)
//     // {projects.map((project) => <ProjectDetailItem project={project}/>)}
//     console.log(item)
//     return (
//         <tr>
//             <td>1</td>
//             {/*<td>{project._id}</td>*/}
//             {/*<td>{project.name}</td>*/}
//             {/*<td>{project.link_to_repo}</td>*/}
//             {/*<td>{project.users_list}</td>*/}
//
//         </tr>
//     )
// }


// const ProjectDetail = ({projects}) => {
//     const params = useParams();
//     console.log(params)
//     // let {id} = useParams();
//     // let project = projects.find((project) => project.id == id);
//
//     return (
//         <div>
//             <h1>{params.name}</h1>
//             <a href={params.link_to_repo}>Repository:</a>
//             <p>Users: {params.users_list}</p>
//             <ol>
//                 {projects.map((item) => <ProjectDetail item={item}/>)}
//             </ol>
//         </div>
//     )
// }
// export default ProjectDetail

