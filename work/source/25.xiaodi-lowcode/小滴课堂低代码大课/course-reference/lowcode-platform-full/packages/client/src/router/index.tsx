import { createHashRouter } from "react-router-dom";
import Editor from "~/pages/editor";
import Home from "~/pages/index";
import DataCount from "~/pages/dataCount";
import Release from "~/pages/release";
import Preview from "~/pages/preview";
import LoginOrRegister from "~/pages/loginOrRegister";

export const router = createHashRouter([
  {
    path: "/",
    element: <Home />,
    children: [
      {
        path: "/login_or_register",
        element: <LoginOrRegister />,
      },
      {
        path: "/editor",
        element: <Editor />,
      },
      {
        path: "/dataCount",
        element: <DataCount />,
      },
      {
        path: "/preview",
        element: <Preview />,
      },
      {
        path: "/release",
        element: <Release />,
      },
    ],
  },
]);
