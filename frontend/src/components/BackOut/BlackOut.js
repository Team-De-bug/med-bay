function BlackOut(props) {
	return(
		<div id={`black-out-${props.id}`} className="patient-black-out" onClick={props.onClick}>
			{props.children}
		</div>
	)
}

export default BlackOut