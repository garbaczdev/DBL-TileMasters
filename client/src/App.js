import React from 'react';

import {Route, Routes, useLocation} from "react-router-dom";
import { AnimatePresence } from "framer-motion";

import {FadedDiv} from "./AnimatedRoute";

import Nav from "./Nav";

import HomePage from "./HomePage";
import ProgramInstructionsPage from "./ProgramInstructionsPage";
import RobotUtilsPage from "./RobotUtilsPage";
import ManualModePage from "./ManualModePage";
import LogsPage from "./LogsPage";

import './styles/App.css';


const subpages = [
  {
    path: "/",
    component: HomePage
  },
  {
    path: "/program-instructions",
    component: ProgramInstructionsPage
  },
  {
    path: "/robot-utils",
    component: RobotUtilsPage
  },
  {
    path: "/manual-mode",
    component: ManualModePage
  },
  {
    path: "/logs",
    component: LogsPage
  },
]


function App() {

  const [darkTheme, setDarkTheme] = React.useState(true);

  const location = useLocation();

  return (
      <div className="app">
        <Nav darkTheme={darkTheme} setDarkTheme={setDarkTheme}/>

        <section className="app-body">
          <AnimatePresence exitBeforeEnter initial={false}>
            <Routes location={location} key={location.key}>
              {
                subpages.map(page => 
                  <Route path={page.path} key={page.path} element={<FadedDiv>{<page.component darkTheme={darkTheme}/>}</FadedDiv>}/>
                  )
              }
            </Routes>
          </AnimatePresence>
        </section>

      </div>
  );
}

export default App;
