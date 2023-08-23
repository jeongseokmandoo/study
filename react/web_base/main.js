// fetch('https://learn.codeit.kr/api/members')
//     .then((response) => response.text())
//     .then((result) => { console.log(result); });

// 

// const member = {
//     name: 'Alice',
//     email: 'alice@codeitmall.lr',
//     department: 'marketing',
// };

fetch('https://learn.codeit.kr/api/members/2', {
    method: 'DELETE',
    // body: JSON.stringify(member),
    //옵션 객체/get 아니면 필요함
})
    .then((response) => response.text())
    .then((result) => { console.log(result); });