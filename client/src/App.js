import { BrowserRouter, Link, Routes, Route} from "react-router-dom";

import Nav from "./Nav";

import HomePage from "./HomePage";
import ProgramInstructionsPage from "./ProgramInstructionsPage";
import RobotUtilsPage from "./RobotUtilsPage";
import ManualModePage from "./ManualModePage";

import './styles/App.css';

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <Nav/>

        <section className="app-body">
          <Routes>

          <Route path="/" element={<HomePage/>} />
          <Route path="/program-instructions" element={<ProgramInstructionsPage />} />
          <Route path="/robot-utils" element={<RobotUtilsPage />} />
          <Route path="/manual-mode" element={<ManualModePage />} />

          </Routes>
        </section>

      </div>
    </BrowserRouter>
  );
}

export default App;
