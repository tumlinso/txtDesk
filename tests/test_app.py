from txtdesk.app import main


def test_bootstrap_entry_point(capsys) -> None:
    main()

    assert capsys.readouterr().out == "txtDesk is in its repository-foundation phase.\n"
