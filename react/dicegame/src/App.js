import Dice from './Dice'

function App() {
    return (
        <div>
            <Dice color="red" num={2} />
            {/* 프롭을 추가할 때 숫자를 사용하려면 중괄호로 감쌓아야 함 */}
        </div>
    );
}

export default App; // 다른 파일에서도 사용가능하도록