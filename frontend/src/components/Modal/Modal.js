import "./modal.css"

function Modal(props) {
	if(!props.show){
		return null
	}

	return (
		<div className="modal">
			<div className="modal-content">
				<div className="modal-header">
					<h4 className="model-title">{props.title}</h4>
				</div>
				<div className="modal-body">
					{props.children}
				</div>
				<div className="modal-footer">
					{props.close && <button>Close</button>}
					{props.ok && <button>Ok</button>}
					{props.cancel && <button>Cancel</button>}
				</div>
			</div>
		</div>
	)
}

export default Modal