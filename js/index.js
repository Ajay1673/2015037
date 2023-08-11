async function getTrain(){
    const response = await fetch('http://20.244.56.144:80/interview/trains/2344')
    const result = await response.json()
    console.log(result)
}
getTrain()