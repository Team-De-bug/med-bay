import { useEffect, useState } from "react";
import FormInput from "./Input/FormInput";

function Form(props) {

    const {submitLabel, fields, title} = props

    const [formValue, setFormValue] = useState({})

    function handleChange(event) {
        setFormValue({
            ...formValue,
            [event.target.name]: event.target.value 
        })
    }

    useEffect(() => {
        console.log(formValue);
    }, [formValue])

    function handleSubmit(e) {
		e.preventDefault();
        console.log(e.target.value)
    }
    
    let formFields = fields.map(field => {
        let options = field.options && field.options.map(optionItem => {
            return (<option key={field.name} value={optionItem}>{optionItem.toUpperCase()}</option>)
        })
        console.log(options);
        return (<>
            <FormInput key={field.name} name={field.name} type={field.type} onChange={handleChange} value={formValue[field.name]}>
				{options}
			</FormInput>
        </>)
    })

    return( 
        <div id="form-window">
            <div id="form-title">
                <label id="form-label">{title}</label>
            </div>
            {/* <span id="form-error">{{form.non_field_errors.as_text}}</span> */}
            <form id="form" onSubmit={handleSubmit}>
                {/* {% csrf_token %} */}
                {formFields}
                <input id="submit-btn" type="submit" value={submitLabel} />
            </form>
        </div>
    )
}

export default Form