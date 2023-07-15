import { useState } from 'react';
import Button from './Button';
import Dice from './Dice'

function random(n) {
    return Math.ceil(Math.random() * n);
}

function App() {
    const [num, setNum] = useState(1);
    const [sum, setSum] = useState(0);
    const [gameHistory, setGameHistory] = useState([]);

    const handleRollClick = () => {
        const nextNum = random(6);
        setNum(nextNum);
        setSum(sum + nextNum);
        // gameHistory.push(nextNum);
        // setGameHistory(gameHistory);
        setGameHistory([...gameHistory, nextNum]);
    };

    const handleClearClick = () => {
        setNum(1);
        setSum(0);
        setGameHistory([]);
    };

    return (
        <div>
            <div>
                <Button onClick={handleRollClick}>던지기</Button>
                <Button onClick={handleClearClick}>처음부터</Button>
            </div>
            <div>
                <h2>나</h2>
                <Dice color="blue" num={num} />
                <h2>총점</h2>
                <p>{sum}</p>
                <h2>기록</h2>
                <p>{gameHistory.join(', ')}</p>
            </div>
            {/* 프롭을 추가할 때 숫자를 사용하려면 중괄호로 감쌓아야 함 */}
        </div>
    );
}

export default App; // 다른 파일에서도 사용가능하도록