function FormInput({name, onChange, type, value, children}) {
    if (type === "select") {
        return <select className="form-input" id={name} name={name} onChange={onChange} value={value} required="true">
            {children}
        </select>
    }

    return <input className="form-input" type={type} id={name} name={name} placeholder={name} onChange={onChange} value={value} required="true"/>
}

export default FormInput