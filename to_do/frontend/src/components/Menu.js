// import React from "react";
// // import UserList from "./User";
// import {Link} from "react-router-dom";
//
//
//
// function NavbarItem({name, href}) {
//     return (
//         <li className="nav-item active">
//             <Link className="nav-link" to={href}>{name}</Link>
//         </li>
//     )
// }
//
//
// export default function Navbar({navbarItems}) {
//     return (
//         <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
//             <a className="navbar-brand" href="#">GeekBrains</a>
//             <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
//                     aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
//                 <span className="navbar-toggler-icon"> </span>
//             </button>
//             <div className="collapse navbar-collapse" id="navbarCollapse">
//                 <ul className="navbar-nav mr-auto">
//                     <li className="nav-item active">
//                         {navbarItems.map((item) => <NavbarItem name={item.name} href={item.href}/>)}
//                     </li>
//                 </ul>
//                 <form className="form-inline mt-2 mt-md-0">
//                     {/*<button onClick={()=>this.is_authenticated()}>Login</button>*/}
//                     <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search"/>
//                     <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
//                 </form>
//             </div>
//         </nav>
//     )
// }

