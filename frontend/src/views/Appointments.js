function CaseContainer(props) {

    const {caseItem} = props
    const dateValue = caseItem.patient.appointed_date
    const apDate = `${dateValue.getDate()}/${dateValue.getMonth()}/${dateValue.getFullYear()} ${dateValue.getHours()%12}:${dateValue.getMinutes()} ${dateValue.getHours() > 12 ? "PM" : "AM"}`

    return(
        <div key={caseItem.id} className="container" style={{cursor: "pointer"}}>
            <label className="item-detail-label patient-detail-label">Name:</label>
            <input className="item-detail" id="name" type="text" value={caseItem.patient.name} readOnly /><br/>
            <label className="item-detail-label">Age:</label>
            <input className="item-detail" id="age" type="text" value={caseItem.patient.age} pattern="[0-9]+" readOnly /><br/>
            <label className="item-detail-label">Gender:</label>
            <input className="item-detail" id="gender" type="text" value={caseItem.patient.gender.toUpperCase()} size="1" readOnly /><br/>
            <label className="item-detail-label">Appointment Date:</label>
            <input className="item-detail" id="date" type="text" value={apDate} readOnly />
        </div>
    )
}

function Appointments() {

    const cases = [
        {
            id: 1,
            patient: {
                name: "EEEEEEEEEE",
                age: 12,
                gender: "Male",
                appointed_date: new Date(2021, 9, 17, 21, 0, 0, 0)
            }
        },
        {
            id: 2,
            patient: {
                name: "EEEEEEEEEE",
                age: 12,
                gender: "Male",
                appointed_date: new Date(2021, 9, 17, 21, 0, 0, 0)
            }
        }
    ]

    let caseContainers = cases.map((caseItem) => {
        return(
            <CaseContainer caseItem={caseItem} key={caseItem.id}/>
        )
    })

    return(
        <div className="root-container">
            <h3 className="list-title">Doctor's Dashboard</h3><br/>
            <h4 className="list-title">Appointed Patients</h4><br/>
            <div className="list-container">
                { cases.length > 0
                    ? caseContainers
                    : <div className="container" style={{cursor: "pointer"}}>
                        <label className="item-detail-label">No Appointments For Today</label>
                    </div>
                }
            </div>
        </div>
    )
}

export default Appointments