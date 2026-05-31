from healthcheck import health_check

def test_health_check_returns_healthy():
    result = health_check()
    assert result["status"] == "healthy"

def test_health_check_has_version():
    result = health_check()
    assert "version" in result
