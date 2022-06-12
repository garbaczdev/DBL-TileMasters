
import {getThemedIcon} from './icons';

function NotFoundPage({darkTheme}) {
    const Icon = getThemedIcon("SmallLogo", darkTheme);
    return (
        <div className="not-found-page subpage">
            <Icon />
            <h1 className="outline-color">Sorry, this page does not exist!</h1>
        </div>
    );
  }
  
  export default NotFoundPage;