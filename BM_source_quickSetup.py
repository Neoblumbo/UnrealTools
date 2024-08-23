import unreal

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

index = 2

def deleteExistingAssets (connectorIndex):
    # Deletes existing Blackmagic assets based on input data
    
    # Delete Blackmagic source
    bmSource = unreal.EditorAssetLibrary.load_asset("/Game/BlackmagicCapture/BlackmagicSource/BlackmagicSource_" + str(connectorIndex))
    if bmSource:
        unreal.EditorAssetLibrary.delete_asset(bmSource.get_path_name())
    
    # Delete Blackmagic player
    bmPlayer = unreal.EditorAssetLibrary.load_asset("/Game/BlackmagicCapture/BlackmagicSource/BlackmagicPlayer_" + str(connectorIndex))
    if bmPlayer:
        unreal.EditorAssetLibrary.delete_asset(bmPlayer.get_path_name())
    
    # Delete Blackmagic texture
    bmTexture = unreal.EditorAssetLibrary.load_asset("/Game/BlackmagicCapture/BlackmagicSource/BlackmagicTexture_" + str(connectorIndex))
    if bmTexture:
        unreal.EditorAssetLibrary.delete_asset(bmTexture.get_path_name())

def createBMsource (connectorIndex):
    # Creates a new Blacakmagic source actor based on input data
    # Returns the new Blackmagic source actor
    
    factory = unreal.BlackmagicMediaSourceFactoryNew()
    outPath = "/Game/BlackmagicCapture/BlackmagicSource"
    assetName = "BlackmagicSource_" + str(connectorIndex)
    
    # factory.set_editor_property("ParentClass", unreal.Actor)
    new_asset = asset_tools.create_asset(assetName, outPath, unreal.BlackmagicMediaSource, factory)
    new_asset.get_editor_property("media_configuration").get_editor_property("media_connection").set_editor_property("port_identifier", connectorIndex)
    
    
    unreal.EditorAssetLibrary.save_loaded_asset(new_asset)
    return new_asset
    
def createMediaPlayer(connectorIndex, bmSource):
    # Creates a new media player actor
    # Returns the new media player actor
    
    # factory = unreal.MediaPlayerFactory()
    outPath = "/Game/BlackmagicCapture/BlackmagicSource"
    assetName = "BlackmagicPlayer_" + str(connectorIndex)
    
    new_asset = asset_tools.create_asset(assetName, outPath, unreal.MediaPlayer, None)
    
    # this function works just need to figure out how to get the object reference if the object was not just created
    new_asset.open_source(bmSource)
    
    unreal.EditorAssetLibrary.save_loaded_asset(new_asset)

def createMediaTexture(connectorIndex):
    # Creates a new media texture actor
    # Returns the new media texture actor
    
    # factory = unreal.MediaTextureFactoryNew()
    outPath = "/Game/BlackmagicCapture/BlackmagicSource"
    assetName = "BlackmagicTexture_" + str(connectorIndex)
    
    new_asset = asset_tools.create_asset(assetName, outPath, unreal.MediaTexture, None)
    new_asset.set_editor_property("media_player", unreal.EditorAssetLibrary.load_asset("/Game/BlackmagicCapture/BlackmagicSource/BlackmagicPlayer_" + str(connectorIndex)))
    unreal.EditorAssetLibrary.save_loaded_asset(new_asset)

deleteExistingAssets(index)    
createMediaPlayer(index, createBMsource(index))
createMediaTexture(index)
