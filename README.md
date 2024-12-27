# Steps involved
	1)Generate synthetic discharge summary or progress note.<br>
	2)Use langchain and prompt engineering to extract clinical data from this generated synthetic
discharge summary / progress note.<br>
	3)Convert this extracted clinical data in FHIR format and the FHIR Resources to be used are
		a.Patient
		b.Observation
		c.Practitioner
		d.AllergyIntolerance
		e.Problem
		f.Procedure
		g.FamilyMemberHistory
		h.MedicationStatement
		i.Careplan<br>
	4)Store the extracted data in a Postgresql or MongoDB database.<br>
 	5)Host the entire project in Github.<br>
