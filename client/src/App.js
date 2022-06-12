import React from 'react';

import {Route, Routes, useLocation} from "react-router-dom";
import { AnimatePresence } from "framer-motion";
import {NotificationContainer} from 'react-notifications';

import {FadedDiv} from "./AnimatedRoute";

import Nav from "./Nav";
import ModePrompt from "./ModePrompt";

import HomePage from "./HomePage";
import ProgramInstructionsPage from "./ProgramInstructionsPage";
import RobotUtilsPage from "./RobotUtilsPage";
import ManualModePage from "./ManualModePage";
import LogsPage from "./LogsPage";
import ProgramInstructionsTutorialPage from './ProgramInstructionsTutorialPage';
import NotFoundPage from './NotFoundPage';

import './styles/App.css';
import './styles/Notofications.css';
import 'reactjs-popup/dist/index.css';


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
  {
    path: "/program-instructions/tutorial",
    component: ProgramInstructionsTutorialPage
  },
]


function App({dataFetcher}) {

  const [darkTheme, setDarkTheme] = React.useState(true);

  const location = useLocation();

  return (
      <div className="app">
        <NotificationContainer className="notification-container" />
        <Nav darkTheme={darkTheme} setDarkTheme={setDarkTheme}/>

        <AnimatePresence exitBeforeEnter initial={false}>
          <Routes location={location} key={location.key}>
            {
              subpages.map(page => 
                <Route path={page.path} key={page.path} element={
                  <FadedDiv>
                    {<page.component darkTheme={darkTheme} dataFetcher={dataFetcher}/>}
                  </FadedDiv>
                  }
                />
                )
            }
            <Route path="*" element={<NotFoundPage darkTheme={darkTheme}/>} />
          </Routes>
        </AnimatePresence>

        <ModePrompt dataFetcher={dataFetcher}/>
      </div>
  );
}

export default App;
