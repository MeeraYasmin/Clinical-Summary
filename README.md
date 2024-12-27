# Steps involved
	1)Generate synthetic discharge summary or progress note.
	2)Use langchain and prompt engineering to extract clinical data from this generated synthetic discharge summary / progress note.
	3)Convert this extracted clinical data in FHIR format and the FHIR Resources to be used are
		a.Patient
		b.Observation
		c.Practitioner
		d.AllergyIntolerance
		e.Problem
		f.Procedure
		g.FamilyMemberHistory
		h.MedicationStatement
		i.Careplan
	4)Store the extracted data in a Postgresql or MongoDB database.
 	5)Host the entire project in Github.
