import Board from './Board';
import { useState } from 'react';
import Button from './Button';

function random(n) {
    return Math.ceil(Math.random() * n);
}

function App() {
    const [myHistory, setMyHistory] = useState([]);
    const [otherHistory, setOtherHistory] = useState([]);

    const handleRollClick = () => {
        const nextMyNum = random(6);
        const nextOtherNum = random(6);
        // gameHistory.push(nextNum);
        // setGameHistory(gameHistory);
        // -> 사실 이 방식은 잘못된 방식, 기존 배열을 칭하기에, 그 배열의 주소를 가르킴
        setMyHistory([...myHistory, nextMyNum]);
        setOtherHistory([...otherHistory, nextOtherNum]);
    };

    const handleClearClick = () => {
        setMyHistory([]);
        setOtherHistory([]);
    };

    return (
        <div className="App">
            <div>
                <Button className="App-button" color="blue" onClick={handleRollClick}>던지기</Button>
                <Button className="App-button" color="red" onClick={handleClearClick}>처음부터</Button>
            </div>
            <div>
                <Board name='나' color='blue' gameHistory={myHistory}/>
                <Board name='상대' color='red'  gameHistory={otherHistory}/>
            </div>
        </div>
    );
}

export default App;