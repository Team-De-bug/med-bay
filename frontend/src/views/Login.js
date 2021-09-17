import Form from "../components/Form/Form"

function Login() {

    const fields = [
        {name: "username", type: "text"},
        {name: "password", type: "password"}
    ]

    return(
        <Form title="Staff Login" submitLabel="Login" fields={fields}/>
    )
}

export default Login