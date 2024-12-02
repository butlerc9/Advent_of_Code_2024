from report_safety_analyser import report_safety_analyser

def test_sample_reports():
    
    assert report_safety_analyser([7,6,4,2,1]) is True
    assert report_safety_analyser([1,2,7,8,9]) is False
    assert report_safety_analyser([9,7,6,2,1]) is False
    assert report_safety_analyser([1,3,2,4,5]) is False
    assert report_safety_analyser([8,6,4,4,1]) is False
    assert report_safety_analyser([1,3,6,7,9]) is True