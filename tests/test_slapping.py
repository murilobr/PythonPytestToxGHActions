from slapping.slap_that_like_button import LikeState, slap_many


def test_slaps():
    assert slap_many(LikeState.empty, "") is LikeState.empty
    assert slap_many(LikeState.empty, "l") is LikeState.liked
    assert slap_many(LikeState.empty, "d") is LikeState.disliked
    assert slap_many(LikeState.empty, "ll") is LikeState.empty
    assert slap_many(LikeState.empty, "dd") is LikeState.empty
    assert slap_many(LikeState.empty, "ld") is LikeState.disliked
    assert slap_many(LikeState.empty, "dl") is LikeState.liked
    assert slap_many(LikeState.empty, "ldd") is LikeState.empty
    assert slap_many(LikeState.empty, "lldd") is LikeState.empty
    assert slap_many(LikeState.empty, "ddl") is LikeState.liked
