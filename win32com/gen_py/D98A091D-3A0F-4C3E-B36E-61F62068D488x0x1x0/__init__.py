# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.00
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Tue Nov 17 17:18:30 2015
"""Autodesk Inventor Object Library"""
makepy_version = '0.5.00'
python_version = 0x2070af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{D98A091D-3A0F-4C3E-B36E-61F62068D488}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	kASideDefault                 =106241     # from enum ASideFaceStatusEnum
	kASideSick                    =106242     # from enum ASideFaceStatusEnum
	kASideUpToDate                =106243     # from enum ASideFaceStatusEnum
	kHigh                         =69379      # from enum AccuracyEnum
	kLow                          =69377      # from enum AccuracyEnum
	kMedium                       =69378      # from enum AccuracyEnum
	kVeryHigh                     =69380      # from enum AccuracyEnum
	kActivationAction             =2          # from enum ActionTypeEnum
	kAllActions                   =-1         # from enum ActionTypeEnum
	kDeleteAction                 =1          # from enum ActionTypeEnum
	kMoveAction                   =16         # from enum ActionTypeEnum
	kNoAction                     =0          # from enum ActionTypeEnum
	kReorderAction                =4          # from enum ActionTypeEnum
	kRestructureAction            =8          # from enum ActionTypeEnum
	kAddInLicenseStatusAvailable  =76290      # from enum AddInLicenseStatusEnum
	kAddInLicenseStatusUnavailable=76291      # from enum AddInLicenseStatusEnum
	kAddInLicenseStatusUnlicensed =76289      # from enum AddInLicenseStatusEnum
	kLoadBehaviorUnknown          =94727      # from enum AddInLoadBehaviorEnum
	kLoadImmediately              =94721      # from enum AddInLoadBehaviorEnum
	kLoadOnDemand                 =94726      # from enum AddInLoadBehaviorEnum
	kLoadWithAssemblies           =94723      # from enum AddInLoadBehaviorEnum
	kLoadWithDrawings             =94725      # from enum AddInLoadBehaviorEnum
	kLoadWithParts                =94722      # from enum AddInLoadBehaviorEnum
	kLoadWithPresentations        =94724      # from enum AddInLoadBehaviorEnum
	kHorizontalAlignment          =64257      # from enum AlignmentTypeEnum
	kVerticalAlignment            =64258      # from enum AlignmentTypeEnum
	kAdjacent                     =73473      # from enum AlternateUnitsDisplayTypeEnum
	kAdjacentWithBracketsForAlternate=73475      # from enum AlternateUnitsDisplayTypeEnum
	kAdjacentWithBracketsForPrimary=73474      # from enum AlternateUnitsDisplayTypeEnum
	kCrossSectionAnalysis         =73986      # from enum AnalysisTypeEnum
	kCurvatureAnalysis            =73987      # from enum AnalysisTypeEnum
	kDraftAnalysis                =73988      # from enum AnalysisTypeEnum
	kNoAnalysis                   =73985      # from enum AnalysisTypeEnum
	kSurfaceAnalysis              =73989      # from enum AnalysisTypeEnum
	kZebraAnalysis                =73990      # from enum AnalysisTypeEnum
	kDirectedSolution             =78593      # from enum AngleConstraintSolutionTypeEnum
	kReferenceVectorSolution      =78595      # from enum AngleConstraintSolutionTypeEnum
	kUndirectedSolution           =78594      # from enum AngleConstraintSolutionTypeEnum
	kDegreesAngularPrecision      =42250      # from enum AngularPrecisionEnum
	kEightDecimalPlacesAngularPrecision=42249      # from enum AngularPrecisionEnum
	kFiveDecimalPlacesAngularPrecision=42246      # from enum AngularPrecisionEnum
	kFourDecimalPlacesAngularPrecision=42245      # from enum AngularPrecisionEnum
	kMinutesAngularPrecision      =42251      # from enum AngularPrecisionEnum
	kOneDecimalPlaceAngularPrecision=42242      # from enum AngularPrecisionEnum
	kSecondsAngularPrecision      =42252      # from enum AngularPrecisionEnum
	kSecondsFourDecimalPlaceAngularPrecision=42256      # from enum AngularPrecisionEnum
	kSecondsOneDecimalPlaceAngularPrecision=42253      # from enum AngularPrecisionEnum
	kSecondsThreeDecimalPlaceAngularPrecision=42255      # from enum AngularPrecisionEnum
	kSecondsTwoDecimalPlaceAngularPrecision=42254      # from enum AngularPrecisionEnum
	kSevenDecimalPlacesAngularPrecision=42248      # from enum AngularPrecisionEnum
	kSixDecimalPlacesAngularPrecision=42247      # from enum AngularPrecisionEnum
	kThreeDecimalPlacesAngularPrecision=42244      # from enum AngularPrecisionEnum
	kTwoDecimalPlacesAngularPrecision=42243      # from enum AngularPrecisionEnum
	kZeroDecimalPlaceAngularPrecision=42241      # from enum AngularPrecisionEnum
	kBodyAppearance               =100611     # from enum AppearanceSourceTypeEnum
	kComponentOccurrenceAppearance=100615     # from enum AppearanceSourceTypeEnum
	kFeatureAppearance            =100610     # from enum AppearanceSourceTypeEnum
	kMaterialAppearance           =100614     # from enum AppearanceSourceTypeEnum
	kOverrideAppearance           =100609     # from enum AppearanceSourceTypeEnum
	kPartAppearance               =100612     # from enum AppearanceSourceTypeEnum
	kWeldsAppearance              =100613     # from enum AppearanceSourceTypeEnum
	kPlugInApplicationAddIn       =1796       # from enum ApplicationAddInTypeEnum
	kStandardApplicationAddIn     =1794       # from enum ApplicationAddInTypeEnum
	kTranslationApplicationAddIn  =1795       # from enum ApplicationAddInTypeEnum
	kUnknownApplicationAddIn      =1793       # from enum ApplicationAddInTypeEnum
	kDarkColorTheme               =87042      # from enum ApplicationFrameColorTypeEnum
	kLightColorTheme              =87041      # from enum ApplicationFrameColorTypeEnum
	kAngleArcDimension            =65539      # from enum ArcDimensionTypeEnum
	kArcLengthArcDimension        =65540      # from enum ArcDimensionTypeEnum
	kChordLengthArcDimension      =65541      # from enum ArcDimensionTypeEnum
	kDiametricArcDimension        =65538      # from enum ArcDimensionTypeEnum
	kRadialArcDimension           =65537      # from enum ArcDimensionTypeEnum
	kAsStyleArrowheadType         =71937      # from enum ArrowheadTypeEnum
	kBlankArrowheadType           =71939      # from enum ArrowheadTypeEnum
	kCircleArrowheadType          =71947      # from enum ArrowheadTypeEnum
	kClosedArrowheadType          =71940      # from enum ArrowheadTypeEnum
	kDatum45BlankArrowheadType    =71956      # from enum ArrowheadTypeEnum
	kDatum45FilledArrowheadType   =71957      # from enum ArrowheadTypeEnum
	kDatum60BlankArrowheadType    =71954      # from enum ArrowheadTypeEnum
	kDatum60FilledArrowheadType   =71955      # from enum ArrowheadTypeEnum
	kFilledArrowheadType          =71941      # from enum ArrowheadTypeEnum
	kFlaredArrowheadType          =71944      # from enum ArrowheadTypeEnum
	kHalf1FilledArrowheadType     =71942      # from enum ArrowheadTypeEnum
	kHalf1FlaredArrowheadType     =71945      # from enum ArrowheadTypeEnum
	kHalf2FilledArrowheadType     =71943      # from enum ArrowheadTypeEnum
	kHalf2FlaredArrowheadType     =71946      # from enum ArrowheadTypeEnum
	kLargeDotArrowheadType        =71950      # from enum ArrowheadTypeEnum
	kNoneArrowheadType            =71948      # from enum ArrowheadTypeEnum
	kObliqueArrowheadType         =71951      # from enum ArrowheadTypeEnum
	kOpenArrowheadType            =71938      # from enum ArrowheadTypeEnum
	kOriginArrowheadType          =71952      # from enum ArrowheadTypeEnum
	kSmallDotArrowheadType        =71949      # from enum ArrowheadTypeEnum
	kThickLineArrowheadType       =71953      # from enum ArrowheadTypeEnum
	kBetweenTwoFacesOriginDefinitionType=106499     # from enum AssemblyJointOriginDefinitionTypeEnum
	kInferOriginDefinitionType    =106497     # from enum AssemblyJointOriginDefinitionTypeEnum
	kOffsetOriginDefinitionType   =106498     # from enum AssemblyJointOriginDefinitionTypeEnum
	kBallJointType                =102406     # from enum AssemblyJointTypeEnum
	kCylindricalJointType         =102404     # from enum AssemblyJointTypeEnum
	kPlanarJointType              =102405     # from enum AssemblyJointTypeEnum
	kRigidJointType               =102401     # from enum AssemblyJointTypeEnum
	kRotationalJointType          =102402     # from enum AssemblyJointTypeEnum
	kSlideJointType               =102403     # from enum AssemblyJointTypeEnum
	kTextureTypeBitmap            =99588      # from enum AssetTextureTypeEnum
	kTextureTypeChecker           =99585      # from enum AssetTextureTypeEnum
	kTextureTypeGradient          =99586      # from enum AssetTextureTypeEnum
	kTextureTypeMarble            =99589      # from enum AssetTextureTypeEnum
	kTextureTypeNoise             =99590      # from enum AssetTextureTypeEnum
	kTextureTypeSpeckle           =99591      # from enum AssetTextureTypeEnum
	kTextureTypeTile              =99587      # from enum AssetTextureTypeEnum
	kTextureTypeUnknown           =99594      # from enum AssetTextureTypeEnum
	kTextureTypeWave              =99592      # from enum AssetTextureTypeEnum
	kTextureTypeWood              =99593      # from enum AssetTextureTypeEnum
	kAssetTypeAppearance          =99073      # from enum AssetTypeEnum
	kAssetTypeMaterial            =99074      # from enum AssetTypeEnum
	kAssetTypePhysicalProperties  =99075      # from enum AssetTypeEnum
	kAssetTypeUnknown             =99076      # from enum AssetTypeEnum
	kAssetValueTextureType        =99336      # from enum AssetValueTypeEnum
	kAssetValueTypeBoolean        =99329      # from enum AssetValueTypeEnum
	kAssetValueTypeChoice         =99331      # from enum AssetValueTypeEnum
	kAssetValueTypeColor          =99335      # from enum AssetValueTypeEnum
	kAssetValueTypeFilename       =99334      # from enum AssetValueTypeEnum
	kAssetValueTypeFloat          =99332      # from enum AssetValueTypeEnum
	kAssetValueTypeInteger        =99330      # from enum AssetValueTypeEnum
	kAssetValueTypeReference      =99337      # from enum AssetValueTypeEnum
	kAssetValueTypeString         =99333      # from enum AssetValueTypeEnum
	kAssetValueUnknownType        =99338      # from enum AssetValueTypeEnum
	kElectricallyBondedConnectionType=93169      # from enum BIMCableTrayConnectionTypeEnum
	kUndefinedConnectionType      =93170      # from enum BIMCableTrayConnectionTypeEnum
	kModelOriginOrientationType   =103682     # from enum BIMComponentOrientationTypeEnum
	kUserCoordinateSystemOrientationType=103683     # from enum BIMComponentOrientationTypeEnum
	kViewCubeOrientationType      =103681     # from enum BIMComponentOrientationTypeEnum
	kCompressionConduitConnectionType=93153      # from enum BIMConduitConnectionTypeEnum
	kGluedConduitConnectionType   =93154      # from enum BIMConduitConnectionTypeEnum
	kSetScrewConduitConnectionType=93155      # from enum BIMConduitConnectionTypeEnum
	kThreadedConduitConnectionType=93156      # from enum BIMConduitConnectionTypeEnum
	kUndefinedConduitConnectionType=93157      # from enum BIMConduitConnectionTypeEnum
	kBIMCableTrayConnectorType    =92929      # from enum BIMConnectorDefinitionTypeEnum
	kBIMConduitConnectorType      =92930      # from enum BIMConnectorDefinitionTypeEnum
	kBIMDuctConnectorType         =92931      # from enum BIMConnectorDefinitionTypeEnum
	kBIMElectricalConnectorType   =92932      # from enum BIMConnectorDefinitionTypeEnum
	kBIMPipeConnectorType         =92933      # from enum BIMConnectorDefinitionTypeEnum
	kCircularShapeConnector       =92675      # from enum BIMConnectorShapeEnum
	kOvalShapeConnector           =92676      # from enum BIMConnectorShapeEnum
	kRectangularShapeConnector    =92674      # from enum BIMConnectorShapeEnum
	kUndefinedShapeConnector      =92673      # from enum BIMConnectorShapeEnum
	kBandedDuctConnectionType     =93137      # from enum BIMDuctConnectionTypeEnum
	kClippedDuctConnectionType    =93138      # from enum BIMDuctConnectionTypeEnum
	kFlangeDuctConnectionType     =93139      # from enum BIMDuctConnectionTypeEnum
	kMasticDuctConnectionType     =93140      # from enum BIMDuctConnectionTypeEnum
	kOverCollarDuctConnectionType =93141      # from enum BIMDuctConnectionTypeEnum
	kRawEdgeDuctConnectionType    =93142      # from enum BIMDuctConnectionTypeEnum
	kSlipDriveDuctConnectionType  =93143      # from enum BIMDuctConnectionTypeEnum
	kSlipJointDuctConnectionType  =93144      # from enum BIMDuctConnectionTypeEnum
	kUndefinedDuctConnectionType  =93145      # from enum BIMDuctConnectionTypeEnum
	kVanStoneDuctConnectionType   =93146      # from enum BIMDuctConnectionTypeEnum
	kCalculatedDuctFlowConfigurationType=93105      # from enum BIMDuctFlowConfigurationEnum
	kPresetDuctFlowConfigurationType=93106      # from enum BIMDuctFlowConfigurationEnum
	kSystemDuctFlowConfigurationType=93107      # from enum BIMDuctFlowConfigurationEnum
	kKCoefficientDuctLossMethodType=93122      # from enum BIMDuctLossMethodEnum
	kNoneDuctLossMethodType       =93121      # from enum BIMDuctLossMethodEnum
	kSpecificLossDuctLossMethodType=93123      # from enum BIMDuctLossMethodEnum
	kExhaustDuctSystemType        =93089      # from enum BIMDuctSystemTypeEnum
	kOtherDuctSystemType          =93090      # from enum BIMDuctSystemTypeEnum
	kReturnDuctSystemType         =93091      # from enum BIMDuctSystemTypeEnum
	kSupplyDuctSystemType         =93092      # from enum BIMDuctSystemTypeEnum
	kUndefinedDuctSystemType      =93093      # from enum BIMDuctSystemTypeEnum
	kLaggingPowerFactorStateType  =93057      # from enum BIMElectricalPowerFactorStateEnum
	kLeadingPowerFactorStateType  =93058      # from enum BIMElectricalPowerFactorStateEnum
	kCommunicationElectricalSystemType=93073      # from enum BIMElectricalSystemTypeEnum
	kControlsElectricalSystemType =93074      # from enum BIMElectricalSystemTypeEnum
	kDataElectricalSystemType     =93075      # from enum BIMElectricalSystemTypeEnum
	kFireAlarmElectricalSystemType=93076      # from enum BIMElectricalSystemTypeEnum
	kNurseCallElectricalSystemType=93077      # from enum BIMElectricalSystemTypeEnum
	kPowerBalancedElectricalSystemType=93078      # from enum BIMElectricalSystemTypeEnum
	kPowerUnbalancedElectricalSystemType=93079      # from enum BIMElectricalSystemTypeEnum
	kSecurityElectricalSystemType =93080      # from enum BIMElectricalSystemTypeEnum
	kTelephoneElectricalSystemType=93081      # from enum BIMElectricalSystemTypeEnum
	kUndefinedElectricalSystemType=93082      # from enum BIMElectricalSystemTypeEnum
	kBiDirectionalFlowDirectionType=93041      # from enum BIMFlowDirectionEnum
	kInFlowDirectionType          =93042      # from enum BIMFlowDirectionEnum
	kOutFlowDirectionType         =93043      # from enum BIMFlowDirectionEnum
	kBrazedPipeConnectionType     =93009      # from enum BIMPipeConnectionTypeEnum
	kButtWeldedPipeConnectionType =93010      # from enum BIMPipeConnectionTypeEnum
	kCapillaryPipeConnectionType  =93011      # from enum BIMPipeConnectionTypeEnum
	kCompressionPipeConnectionType=93012      # from enum BIMPipeConnectionTypeEnum
	kCouplingPipeConnectionType   =93013      # from enum BIMPipeConnectionTypeEnum
	kCrimpedPipeConnectionType    =93014      # from enum BIMPipeConnectionTypeEnum
	kFlangePipeConnectionType     =93015      # from enum BIMPipeConnectionTypeEnum
	kFusionPipeConnectionType     =93016      # from enum BIMPipeConnectionTypeEnum
	kGluedPipeConnectionType      =93017      # from enum BIMPipeConnectionTypeEnum
	kGroovedPipeConnectionType    =93018      # from enum BIMPipeConnectionTypeEnum
	kSlipJointPipeConnectionType  =93019      # from enum BIMPipeConnectionTypeEnum
	kSocketWeldedPipeConnectionType=93020      # from enum BIMPipeConnectionTypeEnum
	kSolderedPipeConnectionType   =93021      # from enum BIMPipeConnectionTypeEnum
	kThreadedPipeConnectionType   =93022      # from enum BIMPipeConnectionTypeEnum
	kUndefinedPipeConnectionType  =93023      # from enum BIMPipeConnectionTypeEnum
	kCalculatedFlowConfigurationType=92993      # from enum BIMPipeFlowConfigurationEnum
	kFixtureUnitsFlowConfigurationType=92996      # from enum BIMPipeFlowConfigurationEnum
	kPresetFlowConfigurationType  =92994      # from enum BIMPipeFlowConfigurationEnum
	kSystemFlowConfigurationType  =92995      # from enum BIMPipeFlowConfigurationEnum
	kKCoefficientPipeLossMethodType=92978      # from enum BIMPipeLossMethodEnum
	kNonePipeLossMethodType       =92977      # from enum BIMPipeLossMethodEnum
	kSpecificLossPipeLossMethodType=92979      # from enum BIMPipeLossMethodEnum
	kDomesticColdWaterPipeSystemType=92945      # from enum BIMPipeSystemTypeEnum
	kDomesticHotWaterPipeSystemType=92946      # from enum BIMPipeSystemTypeEnum
	kFireProtectionDryPipeSystemType=92947      # from enum BIMPipeSystemTypeEnum
	kFireProtectionOtherPipeSystemType=92948      # from enum BIMPipeSystemTypeEnum
	kFireProtectionPreActionPipeSystemType=92949      # from enum BIMPipeSystemTypeEnum
	kFireProtectionWetPipeSystemType=92950      # from enum BIMPipeSystemTypeEnum
	kHydronicReturnPipeSystemType =92951      # from enum BIMPipeSystemTypeEnum
	kHydronicSupplyPipeSystemType =92952      # from enum BIMPipeSystemTypeEnum
	kOtherPipeSystemType          =92953      # from enum BIMPipeSystemTypeEnum
	kSanitaryPipeSystemType       =92954      # from enum BIMPipeSystemTypeEnum
	kUndefinedPipeSystemType      =92955      # from enum BIMPipeSystemTypeEnum
	kEachBOMQuantity              =52225      # from enum BOMQuantityTypeEnum
	kParameterBOMQuantity         =52226      # from enum BOMQuantityTypeEnum
	kDefaultBOMStructure          =51969      # from enum BOMStructureEnum
	kInseparableBOMStructure      =51974      # from enum BOMStructureEnum
	kNormalBOMStructure           =51970      # from enum BOMStructureEnum
	kPhantomBOMStructure          =51971      # from enum BOMStructureEnum
	kPurchasedBOMStructure        =51973      # from enum BOMStructureEnum
	kReferenceBOMStructure        =51972      # from enum BOMStructureEnum
	kVariesBOMStructure           =51975      # from enum BOMStructureEnum
	kModelDataBOMViewType         =62465      # from enum BOMViewTypeEnum
	kPartsOnlyBOMViewType         =62467      # from enum BOMViewTypeEnum
	kStructuredBOMViewType        =62466      # from enum BOMViewTypeEnum
	kCullCCW                      =96771      # from enum BackFaceCullingEnum
	kCullCW                       =96770      # from enum BackFaceCullingEnum
	kCullNone                     =96769      # from enum BackFaceCullingEnum
	kGradientBackgroundType       =52738      # from enum BackgroundTypeEnum
	kImageBackgroundType          =52739      # from enum BackgroundTypeEnum
	kOneColorBackgroundType       =52737      # from enum BackgroundTypeEnum
	kBottomDirection              =48386      # from enum BalloonDirectionEnum
	kLeftDirection                =48387      # from enum BalloonDirectionEnum
	kRightDirection               =48388      # from enum BalloonDirectionEnum
	kTopDirection                 =48385      # from enum BalloonDirectionEnum
	kCircularWithOneEntryBalloonType=48129      # from enum BalloonTypeEnum
	kCircularWithTwoEntriesBalloonType=48130      # from enum BalloonTypeEnum
	kHexagonBalloonType           =48131      # from enum BalloonTypeEnum
	kLinearBalloonType            =48132      # from enum BalloonTypeEnum
	kNoneBalloonType              =48133      # from enum BalloonTypeEnum
	kSketchedSymbolBalloonType    =48134      # from enum BalloonTypeEnum
	kBarControlButton             =22785      # from enum BarControlTypeEnum
	kBarControlPopUp              =22786      # from enum BarControlTypeEnum
	kCompositeOutputType          =90115      # from enum BaseFeatureOutputTypeEnum
	kSolidOutputType              =90114      # from enum BaseFeatureOutputTypeEnum
	kSurfaceOutputType            =90113      # from enum BaseFeatureOutputTypeEnum
	kBendingAngleType             =81665      # from enum BendAngleTypeEnum
	kDefaultAngleType             =81667      # from enum BendAngleTypeEnum
	kOpenAngleType                =81666      # from enum BendAngleTypeEnum
	kCenterlineOfBend             =75777      # from enum BendLocationEnum
	kEndOfBend                    =75779      # from enum BendLocationEnum
	kStartOfBend                  =75778      # from enum BendLocationEnum
	kDefaultBendOrder             =151021569  # from enum BendOrderSourceTypeEnum
	kDuplicateOverrideBendOrder   =151021571  # from enum BendOrderSourceTypeEnum
	kOverrideBendOrder            =151021570  # from enum BendOrderSourceTypeEnum
	kArcLengthAndAngleBendPart    =83457      # from enum BendPartTypeEnum
	kRadiusAndAngleBendPart       =83458      # from enum BendPartTypeEnum
	kRadiusAndArcLengthBendPart   =83459      # from enum BendPartTypeEnum
	kBendPositionAdjacentFace     =75010      # from enum BendPositionEnum
	kBendPositionInnerEdgeOffset  =75013      # from enum BendPositionEnum
	kBendPositionInsideBendFace   =75011      # from enum BendPositionEnum
	kBendPositionOuterEdgeOffset  =75014      # from enum BendPositionEnum
	kBendPositionOutsideBaseFace  =75009      # from enum BendPositionEnum
	kBendPositionTangentToSideFace=75012      # from enum BendPositionEnum
	kDefaultBendReliefShape       =27907      # from enum BendReliefShapeEnum
	kRoundBendReliefShape         =27906      # from enum BendReliefShapeEnum
	kStraightBendReliefShape      =27905      # from enum BendReliefShapeEnum
	kTearBendReliefShape          =27908      # from enum BendReliefShapeEnum
	kArcBendTransition            =28164      # from enum BendTransitionEnum
	kDefaultBendTransition        =28165      # from enum BendTransitionEnum
	kIntersectionBendTransition   =28162      # from enum BendTransitionEnum
	kNoBendTransition             =28161      # from enum BendTransitionEnum
	kStraightLineBendTransition   =28163      # from enum BendTransitionEnum
	kTrimToBendBendTransition     =28166      # from enum BendTransitionEnum
	kBooleanTypeDifference        =74241      # from enum BooleanTypeEnum
	kBooleanTypeIntersect         =74243      # from enum BooleanTypeEnum
	kBooleanTypeUnion             =74242      # from enum BooleanTypeEnum
	kBorderLabelModeAlphabetical  =29953      # from enum BorderLabelModeEnum
	kBorderLabelModeNone          =29955      # from enum BorderLabelModeEnum
	kBorderLabelModeNumeric       =29954      # from enum BorderLabelModeEnum
	kHeadBossType                 =94210      # from enum BossTypeEnum
	kThreadBossType               =94209      # from enum BossTypeEnum
	kContinuousBoundaryPatchCondition=63491      # from enum BoundaryPatchConditionEnum
	kFreeBoundaryPatchCondition   =63489      # from enum BoundaryPatchConditionEnum
	kTangentBoundaryPatchCondition=63490      # from enum BoundaryPatchConditionEnum
	kHorizontalBreakOrientation   =84225      # from enum BreakOrientationEnum
	kVerticalBreakOrientation     =84226      # from enum BreakOrientationEnum
	kFromPointBreakOutType        =117492737  # from enum BreakOutDepthTypeEnum
	kThroughPartBreakOutType      =117492740  # from enum BreakOutDepthTypeEnum
	kToHoleBreakOutType           =117492739  # from enum BreakOutDepthTypeEnum
	kToSketchBreakOutType         =117492738  # from enum BreakOutDepthTypeEnum
	kRectangularBreakStyle        =84481      # from enum BreakStyleEnum
	kStructuralBreakStyle         =84482      # from enum BreakStyleEnum
	kActivateDisplayState         =46850      # from enum BrowserNodeDisplayStateEnum
	kAdaptiveDisplayState         =46858      # from enum BrowserNodeDisplayStateEnum
	kAdaptiveErrorDisplayState    =46860      # from enum BrowserNodeDisplayStateEnum
	kAdaptiveWarningDisplayState  =46859      # from enum BrowserNodeDisplayStateEnum
	kBoldDisplayState             =46868      # from enum BrowserNodeDisplayStateEnum
	kCheckBoxDisplayState         =46855      # from enum BrowserNodeDisplayStateEnum
	kComatoseDisplayState         =46853      # from enum BrowserNodeDisplayStateEnum
	kContactSetDisplayState       =46861      # from enum BrowserNodeDisplayStateEnum
	kCyclicDisplayState           =46865      # from enum BrowserNodeDisplayStateEnum
	kDefaultDisplayState          =46849      # from enum BrowserNodeDisplayStateEnum
	kExcludeDisplayState          =46866      # from enum BrowserNodeDisplayStateEnum
	kGrayCheckBoxDisplayState     =46867      # from enum BrowserNodeDisplayStateEnum
	kIndependantAdaptivityDisplayState=46863      # from enum BrowserNodeDisplayStateEnum
	kReferencedDocNeedsUpdateDisplayState=46864      # from enum BrowserNodeDisplayStateEnum
	kRollbackEditDisplayState     =46851      # from enum BrowserNodeDisplayStateEnum
	kSickDisplayState             =46852      # from enum BrowserNodeDisplayStateEnum
	kSuppressDisplayState         =46854      # from enum BrowserNodeDisplayStateEnum
	kUnresolvedDisplayState       =46856      # from enum BrowserNodeDisplayStateEnum
	kUpdateRequiredDisplayState   =46857      # from enum BrowserNodeDisplayStateEnum
	kYellowCheckBoxDisplayState   =46862      # from enum BrowserNodeDisplayStateEnum
	kAlwaysDisplayText            =43010      # from enum ButtonDisplayEnum
	kDisplayTextInLearningMode    =43011      # from enum ButtonDisplayEnum
	kNoTextWithIcon               =43009      # from enum ButtonDisplayEnum
	kAcceptButtonType             =2          # from enum ButtonTypeEnum
	kCancelButtonType             =1          # from enum ButtonTypeEnum
	kEditButtonType               =4          # from enum ButtonTypeEnum
	kNoneCachedGraphics           =103169     # from enum CachedGraphicsStatusEnum
	kOutOfDateCachedGraphics      =103170     # from enum CachedGraphicsStatusEnum
	kUpToDateCachedGraphics       =103171     # from enum CachedGraphicsStatusEnum
	kBisectorCenterlineType       =62978      # from enum CenterlineTypeEnum
	kCenteredPatternCenterlineType=62980      # from enum CenterlineTypeEnum
	kRegularCenterlineType        =62977      # from enum CenterlineTypeEnum
	kWorkFeatureCenterlineType    =62979      # from enum CenterlineTypeEnum
	kCenterOfGravityCentermarkType=63237      # from enum CentermarkTypeEnum
	kPunchFeatureCentermarkType   =63238      # from enum CentermarkTypeEnum
	kRecoveredPunchFeatureCentermarkType=63239      # from enum CentermarkTypeEnum
	kRegularCentermarkType        =63233      # from enum CentermarkTypeEnum
	kWorkFeatureCentermarkType    =63234      # from enum CentermarkTypeEnum
	kDistance                     =26881      # from enum ChamferDefinitionTypeEnum
	kDistanceAndAngle             =26882      # from enum ChamferDefinitionTypeEnum
	kTwoDistances                 =26883      # from enum ChamferDefinitionTypeEnum
	kDiametricCircleDimension     =65793      # from enum CircleDimensionTypeEnum
	kRadialCircleDimension        =65794      # from enum CircleDimensionTypeEnum
	kPreviewClientGraphics        =45314      # from enum ClientGraphicsTypeEnum
	kTransientClientGraphics      =45313      # from enum ClientGraphicsTypeEnum
	kOverallColor                 =19460      # from enum ColorBindingEnum
	kPerItemColors                =19459      # from enum ColorBindingEnum
	kPerStripColors               =19458      # from enum ColorBindingEnum
	kPerVertexColors              =19457      # from enum ColorBindingEnum
	kAutomaticColorSource         =79106      # from enum ColorSourceTypeEnum
	kLayerColorSource             =79107      # from enum ColorSourceTypeEnum
	kOverrideColorSource          =79105      # from enum ColorSourceTypeEnum
	kButtonPopupCommandBar        =43269      # from enum CommandBarTypeEnum
	kPopUpCommandBar              =43266      # from enum CommandBarTypeEnum
	kRegularCommandBar            =43265      # from enum CommandBarTypeEnum
	kSplitButtonCommandBar        =43267      # from enum CommandBarTypeEnum
	kSplitButtonMRUCommandBar     =43268      # from enum CommandBarTypeEnum
	kAddParametersCommand         =2342       # from enum CommandIDEnum
	kAddPointCommand              =2080       # from enum CommandIDEnum
	kAddPolygonCommand            =2059       # from enum CommandIDEnum
	kAnimateCommand               =2196       # from enum CommandIDEnum
	kCenterPointArcCommand        =2073       # from enum CommandIDEnum
	kCenterPointCircleCommand     =2068       # from enum CommandIDEnum
	kConsCoincidentCommand        =2097       # from enum CommandIDEnum
	kConsCollinearCommand         =2099       # from enum CommandIDEnum
	kConsConcentricCommand        =2098       # from enum CommandIDEnum
	kConsEqualCommand             =2102       # from enum CommandIDEnum
	kConsFixCommand               =2103       # from enum CommandIDEnum
	kConsHorizontalCommand        =2100       # from enum CommandIDEnum
	kConsParallelCommand          =2089       # from enum CommandIDEnum
	kConsPerpendicularCommand     =2088       # from enum CommandIDEnum
	kConsSymmetricCommand         =2371       # from enum CommandIDEnum
	kConsTangentCommand           =2096       # from enum CommandIDEnum
	kConsVerticalCommand          =2101       # from enum CommandIDEnum
	kCreate3DBendCommand          =2361       # from enum CommandIDEnum
	kCreate3DLineCommand          =2360       # from enum CommandIDEnum
	kCreate3DSketchCommand        =2167       # from enum CommandIDEnum
	kCreate3QuarterSectionViewCommand=2183       # from enum CommandIDEnum
	kCreateAreaFillCommand        =2108       # from enum CommandIDEnum
	kCreateAutoDimCommand         =2162       # from enum CommandIDEnum
	kCreateAuxiliaryViewCommand   =2199       # from enum CommandIDEnum
	kCreateBaselineDimensionCommand=2079       # from enum CommandIDEnum
	kCreateBendCommand            =2150       # from enum CommandIDEnum
	kCreateBreakoutViewCommand    =2122       # from enum CommandIDEnum
	kCreateBrokenViewCommand      =2076       # from enum CommandIDEnum
	kCreateCaterpillarCommand     =2111       # from enum CommandIDEnum
	kCreateCenterLineBisectorCommand=2313       # from enum CommandIDEnum
	kCreateCenterLineCommand      =2310       # from enum CommandIDEnum
	kCreateCenterMarkCommand      =2309       # from enum CommandIDEnum
	kCreateCenteredPatternCommand =2320       # from enum CommandIDEnum
	kCreateChamferCommand         =2117       # from enum CommandIDEnum
	kCreateCircularPatternCommand =2131       # from enum CommandIDEnum
	kCreateCoilCommand            =2115       # from enum CommandIDEnum
	kCreateComponentCommand       =2168       # from enum CommandIDEnum
	kCreateContourFlangeCommand   =2161       # from enum CommandIDEnum
	kCreateCornerChamferCommand   =2152       # from enum CommandIDEnum
	kCreateCornerRoundCommand     =2151       # from enum CommandIDEnum
	kCreateCornerSeamCommand      =2149       # from enum CommandIDEnum
	kCreateCutCommand             =2147       # from enum CommandIDEnum
	kCreateDecalCommand           =2107       # from enum CommandIDEnum
	kCreateDerivedPartCommand     =2129       # from enum CommandIDEnum
	kCreateDesignElementCommand   =2121       # from enum CommandIDEnum
	kCreateDetailViewCommand      =2201       # from enum CommandIDEnum
	kCreateDraftViewCommand       =2304       # from enum CommandIDEnum
	kCreateDrawingViewCommand     =2197       # from enum CommandIDEnum
	kCreateEmbossCommand          =2094       # from enum CommandIDEnum
	kCreateEndTreatmentCommand    =2123       # from enum CommandIDEnum
	kCreateEquationParamCommand   =2061       # from enum CommandIDEnum
	kCreateExtrudeCommand         =2050       # from enum CommandIDEnum
	kCreateFaceCommand            =2146       # from enum CommandIDEnum
	kCreateFaceDraftCommand       =2118       # from enum CommandIDEnum
	kCreateFilletCommand          =2116       # from enum CommandIDEnum
	kCreateFlangeCommand          =2148       # from enum CommandIDEnum
	kCreateFlatPatternCommand     =2145       # from enum CommandIDEnum
	kCreateFoldCommand            =2160       # from enum CommandIDEnum
	kCreateGeneralDimensionCommand=2306       # from enum CommandIDEnum
	kCreateGroundedWorkPointCommand=2095       # from enum CommandIDEnum
	kCreateHalfSectionViewCommand =2182       # from enum CommandIDEnum
	kCreateHemCommand             =2153       # from enum CommandIDEnum
	kCreateHoleCommand            =2113       # from enum CommandIDEnum
	kCreateHoleTableFromViewCommand=2077       # from enum CommandIDEnum
	kCreateHoleTableGroupCommand  =2210       # from enum CommandIDEnum
	kCreateInterfaceCommand       =2178       # from enum CommandIDEnum
	kCreateIntersectionCurveCommand=2372       # from enum CommandIDEnum
	kCreateKnitSurfaceCommand     =2092       # from enum CommandIDEnum
	kCreateLoftCommand            =2053       # from enum CommandIDEnum
	kCreateMateConstraintCommand  =2078       # from enum CommandIDEnum
	kCreateMirrorCommand          =2132       # from enum CommandIDEnum
	kCreateNewSheetCommand        =2305       # from enum CommandIDEnum
	kCreateOrdinateDimensionCommand=2307       # from enum CommandIDEnum
	kCreatePresentationViewCommand=2193       # from enum CommandIDEnum
	kCreateProjectedViewCommand   =2198       # from enum CommandIDEnum
	kCreatePunchCommand           =2075       # from enum CommandIDEnum
	kCreateQuarterSectionViewCommand=2181       # from enum CommandIDEnum
	kCreateRectPatternCommand     =2130       # from enum CommandIDEnum
	kCreateRevisionTableCommand   =2125       # from enum CommandIDEnum
	kCreateRevisionTagCommand     =2126       # from enum CommandIDEnum
	kCreateRevolveCommand         =2051       # from enum CommandIDEnum
	kCreateRibCommand             =2064       # from enum CommandIDEnum
	kCreateSectionViewCommand     =2200       # from enum CommandIDEnum
	kCreateSelectedHoleTableCommand=2226       # from enum CommandIDEnum
	kCreateShellCommand           =2114       # from enum CommandIDEnum
	kCreateSingleOrdinateDimCommand=2369       # from enum CommandIDEnum
	kCreateSketchChamferCommand   =2163       # from enum CommandIDEnum
	kCreateSketchCommand          =2049       # from enum CommandIDEnum
	kCreateSketchMirrorCommand    =2060       # from enum CommandIDEnum
	kCreateSplitCommand           =2119       # from enum CommandIDEnum
	kCreateSweepCommand           =2052       # from enum CommandIDEnum
	kCreateTextCommand            =2106       # from enum CommandIDEnum
	kCreateTextStylesCommand      =2062       # from enum CommandIDEnum
	kCreateThreadCommand          =2164       # from enum CommandIDEnum
	kCreateUnsectionedViewCommand =2184       # from enum CommandIDEnum
	kCreateWeldSymbolCommand      =2322       # from enum CommandIDEnum
	kCreateWorkAxisCommand        =2134       # from enum CommandIDEnum
	kCreateWorkPlaneCommand       =2133       # from enum CommandIDEnum
	kCreateWorkPointCommand       =2135       # from enum CommandIDEnum
	kDefaultCommand               =2048       # from enum CommandIDEnum
	kDeleteFaceCommand            =2090       # from enum CommandIDEnum
	kDeselAuthorCommand           =2359       # from enum CommandIDEnum
	kDesignViewsCommand           =2192       # from enum CommandIDEnum
	kEditFixedWorkPointCommand    =2127       # from enum CommandIDEnum
	kEditSketchCoordCommand       =2065       # from enum CommandIDEnum
	kEditThreadCommand            =2165       # from enum CommandIDEnum
	kEditTweaksCommand            =2312       # from enum CommandIDEnum
	kEditViewCommand              =2124       # from enum CommandIDEnum
	kEllipseCommand               =2070       # from enum CommandIDEnum
	kExtendBodyCommand            =2137       # from enum CommandIDEnum
	kFileOpenCommand              =2057       # from enum CommandIDEnum
	kFileSaveCommand              =2140       # from enum CommandIDEnum
	kFileSaveCopyAsCommand        =2056       # from enum CommandIDEnum
	kFillHatchSketchRegionCommand =2166       # from enum CommandIDEnum
	kFormatDimStylesCommand       =2370       # from enum CommandIDEnum
	kIncludeGeometry3DCommand     =2368       # from enum CommandIDEnum
	kInsertBalloonAllCommand      =2340       # from enum CommandIDEnum
	kInsertBalloonCommand         =2339       # from enum CommandIDEnum
	kInsertDatumIdentifierCommand =2325       # from enum CommandIDEnum
	kInsertDatumTargetCircleCommand=2327       # from enum CommandIDEnum
	kInsertDatumTargetLeaderCommand=2326       # from enum CommandIDEnum
	kInsertDatumTargetLineCommand =2328       # from enum CommandIDEnum
	kInsertDatumTargetPointCommand=2329       # from enum CommandIDEnum
	kInsertDatumTargetRectCommand =2336       # from enum CommandIDEnum
	kInsertDesignElementCommand   =2128       # from enum CommandIDEnum
	kInsertFeatureControlFrameCommand=2323       # from enum CommandIDEnum
	kInsertFeatureIdentifierCommand=2324       # from enum CommandIDEnum
	kInsertHoleNotesCommand       =2308       # from enum CommandIDEnum
	kInsertImageCommand           =2109       # from enum CommandIDEnum
	kInsertImportCommand          =2074       # from enum CommandIDEnum
	kInsertLeaderTextCommand      =2338       # from enum CommandIDEnum
	kInsertPartsListCommand       =2341       # from enum CommandIDEnum
	kInsertSurfaceTextureCommand  =2321       # from enum CommandIDEnum
	kInsertTableCommand           =2373       # from enum CommandIDEnum
	kInsertTextCommand            =2337       # from enum CommandIDEnum
	kLineCommand                  =2066       # from enum CommandIDEnum
	kLookAtViewCommand            =2355       # from enum CommandIDEnum
	kMeasureCommand               =2058       # from enum CommandIDEnum
	kModifyStandardSettingsCommand=2242       # from enum CommandIDEnum
	kMoveComponentCommand         =2179       # from enum CommandIDEnum
	kMoveFaceCommand              =2136       # from enum CommandIDEnum
	kPanCommand                   =2353       # from enum CommandIDEnum
	kPatternComponentCommand      =2169       # from enum CommandIDEnum
	kPlaceComponentCommand        =2054       # from enum CommandIDEnum
	kPlaceConstraintCommand       =2176       # from enum CommandIDEnum
	kPopupBrowserFiltersCommand   =2185       # from enum CommandIDEnum
	kPreciseViewRotationCommand   =2195       # from enum CommandIDEnum
	kProjectCutEdgesCommand       =2112       # from enum CommandIDEnum
	kProjectGeometryCommand       =2105       # from enum CommandIDEnum
	kProjectViewEdgesCommand      =2110       # from enum CommandIDEnum
	kPushBackLocalBOMItemNumbersCommand=2139       # from enum CommandIDEnum
	kRebuildPartCommand           =2055       # from enum CommandIDEnum
	kRefreshViewCommand           =2138       # from enum CommandIDEnum
	kReplaceAllComponentsCommand  =2170       # from enum CommandIDEnum
	kReplaceComponentCommand      =2177       # from enum CommandIDEnum
	kReplaceFaceCommand           =2091       # from enum CommandIDEnum
	kRotateCommand                =2354       # from enum CommandIDEnum
	kRotateComponentCommand       =2180       # from enum CommandIDEnum
	kRotateViewCommand            =2311       # from enum CommandIDEnum
	kSheetMetalSettingsCommand    =2144       # from enum CommandIDEnum
	kShowConstraintsCommand       =2104       # from enum CommandIDEnum
	kSketchExtendCommand          =2084       # from enum CommandIDEnum
	kSketchFilletCommand          =2083       # from enum CommandIDEnum
	kSketchGeneralDimCommand      =2087       # from enum CommandIDEnum
	kSketchOffsetCommand          =2086       # from enum CommandIDEnum
	kSketchTrimCommand            =2085       # from enum CommandIDEnum
	kSplineCommand                =2067       # from enum CommandIDEnum
	kTangentArcCommand            =2072       # from enum CommandIDEnum
	kTangentCircleCommand         =2069       # from enum CommandIDEnum
	kThickenCommand               =2093       # from enum CommandIDEnum
	kThreePointArcCommand         =2071       # from enum CommandIDEnum
	kThreePointRectangleCommand   =2082       # from enum CommandIDEnum
	kTweakComponentsCommand       =2194       # from enum CommandIDEnum
	kTwoPointRectangleCommand     =2081       # from enum CommandIDEnum
	kViewCatalogCommand           =2120       # from enum CommandIDEnum
	kViewHiddenEdgeCommand        =2357       # from enum CommandIDEnum
	kViewShadedCommand            =2358       # from enum CommandIDEnum
	kViewWireframeCommand         =2356       # from enum CommandIDEnum
	kZoomAllCommand               =2344       # from enum CommandIDEnum
	kZoomCommand                  =2343       # from enum CommandIDEnum
	kZoomSelectCommand            =2352       # from enum CommandIDEnum
	kZoomWindowCommand            =2345       # from enum CommandIDEnum
	kEditMaskCmdType              =57         # from enum CommandTypesEnum
	kFileOperationsCmdType        =4          # from enum CommandTypesEnum
	kFilePropertyEditCmdType      =8          # from enum CommandTypesEnum
	kNonShapeEditCmdType          =32         # from enum CommandTypesEnum
	kQueryOnlyCmdType             =2          # from enum CommandTypesEnum
	kReferencesChangeCmdType      =64         # from enum CommandTypesEnum
	kSchemaChangeCmdType          =128        # from enum CommandTypesEnum
	kShapeEditCmdType             =1          # from enum CommandTypesEnum
	kUpdateWithReferencesCmdType  =16         # from enum CommandTypesEnum
	kEqualToComparisonType        =60417      # from enum ComparisonTypeEnum
	kGreaterThanComparisonType    =60420      # from enum ComparisonTypeEnum
	kGreaterThanOrEqualToComparisonType=60422      # from enum ComparisonTypeEnum
	kLessThanComparisonType       =60419      # from enum ComparisonTypeEnum
	kLessThanOrEqualToComparisonType=60421      # from enum ComparisonTypeEnum
	kNotEqualToComparisonType     =60418      # from enum ComparisonTypeEnum
	kIncrementAsAmountOfValue     =94465      # from enum ConstraintIncrementTypeEnum
	kIncrementAsNumberOfSteps     =94466      # from enum ConstraintIncrementTypeEnum
	kHorizontalAndVertical        =104962     # from enum ConstraintInferencePriorityEnum
	kParallelAndPerpendicular     =104961     # from enum ConstraintInferencePriorityEnum
	kHorizontalAndVerticalPriority=50434      # from enum ConstraintPriorityEnum
	kNonePriority                 =50435      # from enum ConstraintPriorityEnum
	kParallelAndPerpendicularPriority=50433      # from enum ConstraintPriorityEnum
	kFullyConstrainedConstraintStatus=51713      # from enum ConstraintStatusEnum
	kOverConstrainedConstraintStatus=51715      # from enum ConstraintStatusEnum
	kUnderConstrainedConstraintStatus=51714      # from enum ConstraintStatusEnum
	kUnknownConstraintStatus      =51716      # from enum ConstraintStatusEnum
	kInsideContainment            =30978      # from enum ContainmentEnum
	kOnContainment                =30979      # from enum ContainmentEnum
	kOutsideContainment           =30980      # from enum ContainmentEnum
	kUnknownContainment           =30977      # from enum ContainmentEnum
	kInventorDesktopAccess        =81153      # from enum ContentCenterAccessOptionEnum
	kVaultOrProductstreamServerAccess=81154      # from enum ContentCenterAccessOptionEnum
	kNewer                        =2          # from enum ContentCenterInstanceStatusEnum
	kNotFound                     =8          # from enum ContentCenterInstanceStatusEnum
	kOlder                        =1          # from enum ContentCenterInstanceStatusEnum
	kUpToDate                     =4          # from enum ContentCenterInstanceStatusEnum
	kRSCFamilyHealthMissingCatParamMap=80179      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithAuthorTableAndCategory=80183      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithCategory=80181      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithTable=80180      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithTableAndCategory=80182      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthRequiresReAuthor=80177      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthTableUpdateIncomplete=80178      # from enum ContentCenterRSCResultEnum
	kRSCInstancingDifferentFamily =80195      # from enum ContentCenterRSCResultEnum
	kRSCInstancingDifferentMember =80196      # from enum ContentCenterRSCResultEnum
	kRSCInstancingFeatureSuppressFail=80199      # from enum ContentCenterRSCResultEnum
	kRSCInstancingInvalidMemberValue=80202      # from enum ContentCenterRSCResultEnum
	kRSCInstancingLongFilename    =80198      # from enum ContentCenterRSCResultEnum
	kRSCInstancingMaterialNotFound=80197      # from enum ContentCenterRSCResultEnum
	kRSCInstancingMissingFileWritePermission=80194      # from enum ContentCenterRSCResultEnum
	kRSCInstancingThreadCreateFail=80201      # from enum ContentCenterRSCResultEnum
	kRSCInstancingThreadFeatureNotFound=80200      # from enum ContentCenterRSCResultEnum
	kRSCInstancingUnknownError    =80193      # from enum ContentCenterRSCResultEnum
	kRSCNoError                   =80129      # from enum ContentCenterRSCResultEnum
	kRSCNoTPAddInLoadedForTPPart  =80162      # from enum ContentCenterRSCResultEnum
	kRSCPartIsTPPipe              =80161      # from enum ContentCenterRSCResultEnum
	kRSCReplaceFailed             =80209      # from enum ContentCenterRSCResultEnum
	kRSCUnknownFailed             =80145      # from enum ContentCenterRSCResultEnum
	kContentFeatureFamily         =2          # from enum ContentFamilyTypeEnum
	kContentPartFamily            =1          # from enum ContentFamilyTypeEnum
	kContentCategoryType          =57089      # from enum ContentItemTypeEnum
	kContentFamilyType            =57090      # from enum ContentItemTypeEnum
	kContentMemberType            =57091      # from enum ContentItemTypeEnum
	kCustomContent                =2          # from enum ContentLibraryComponentTypeBits
	kStandardContent              =1          # from enum ContentLibraryComponentTypeBits
	kDoNotRefreshOutOfDateParts   =3          # from enum ContentMemberRefreshEnum
	kRefreshOutOfDateParts        =2          # from enum ContentMemberRefreshEnum
	kUseDefaultRefreshSetting     =1          # from enum ContentMemberRefreshEnum
	kContentConsumer              =0          # from enum ContentUserRoleEnum
	kContentEditor                =1          # from enum ContentUserRoleEnum
	kContentPublisher             =2          # from enum ContentUserRoleEnum
	kCurvatureContinuity          =61954      # from enum ContinuityTypeEnum
	kTangentContinuity            =61953      # from enum ContinuityTypeEnum
	kButtonDefinition             =42753      # from enum ControlDefinitionTypeEnum
	kComboBoxDefinition           =42754      # from enum ControlDefinitionTypeEnum
	kMacroControlDefinition       =42755      # from enum ControlDefinitionTypeEnum
	kButtonControl                =45061      # from enum ControlTypeEnum
	kButtonPopupControl           =45058      # from enum ControlTypeEnum
	kComboBoxControl              =45062      # from enum ControlTypeEnum
	kGalleryControl               =45066      # from enum ControlTypeEnum
	kMacroControl                 =45063      # from enum ControlTypeEnum
	kPopupControl                 =45057      # from enum ControlTypeEnum
	kSeparatorControl             =45065      # from enum ControlTypeEnum
	kSplitButtonControl           =45060      # from enum ControlTypeEnum
	kSplitButtonMRUControl        =45059      # from enum ControlTypeEnum
	kTogglePopupControl           =45067      # from enum ControlTypeEnum
	kUnknownControl               =45064      # from enum ControlTypeEnum
	kXYPlane                      =87297      # from enum CoordinateSystemPlaneEnum
	kXZPlane                      =87298      # from enum CoordinateSystemPlaneEnum
	kYZPlane                      =87299      # from enum CoordinateSystemPlaneEnum
	kCartesian                    =98561      # from enum CoordinateSystemTypeEnum
	kCylindrical                  =98563      # from enum CoordinateSystemTypeEnum
	kPolar                        =98562      # from enum CoordinateSystemTypeEnum
	kSpherical                    =98564      # from enum CoordinateSystemTypeEnum
	kCornerFaceEdgeDistance       =79106      # from enum CornerDefinitionTypeEnum
	kCornerMaxDistance            =79105      # from enum CornerDefinitionTypeEnum
	kArcWeldCornerReliefShape     =28425      # from enum CornerReliefShapeEnum
	kDefaultCornerReliefShape     =28422      # from enum CornerReliefShapeEnum
	kFullRoundCornerReliefShape   =28428      # from enum CornerReliefShapeEnum
	kIntersectionCornerReliefShape=28427      # from enum CornerReliefShapeEnum
	kLinearWeldReliefShape        =28421      # from enum CornerReliefShapeEnum
	kNoReplacementCornerReliefShape=28426      # from enum CornerReliefShapeEnum
	kRoundCornerReliefShape       =28417      # from enum CornerReliefShapeEnum
	kRoundWithRadiusCornerReliefShape=28429      # from enum CornerReliefShapeEnum
	kSquareCornerReliefShape      =28418      # from enum CornerReliefShapeEnum
	kTearCornerReliefShape        =28419      # from enum CornerReliefShapeEnum
	kTrimToBendReliefShape        =28420      # from enum CornerReliefShapeEnum
	kCornerNoOverlap              =76034      # from enum CornerTypeEnum
	kCornerOverlap                =76033      # from enum CornerTypeEnum
	kCornerReverseOverlap         =76035      # from enum CornerTypeEnum
	kCursorHotSpotBottomCenter    =47880      # from enum CursorHotSpotEnum
	kCursorHotSpotBottomLeft      =47879      # from enum CursorHotSpotEnum
	kCursorHotSpotBottomRight     =47881      # from enum CursorHotSpotEnum
	kCursorHotSpotDefault         =47882      # from enum CursorHotSpotEnum
	kCursorHotSpotMiddleCenter    =47877      # from enum CursorHotSpotEnum
	kCursorHotSpotMiddleLeft      =47876      # from enum CursorHotSpotEnum
	kCursorHotSpotMiddleRight     =47878      # from enum CursorHotSpotEnum
	kCursorHotSpotTopCenter       =47874      # from enum CursorHotSpotEnum
	kCursorHotSpotTopLeft         =47873      # from enum CursorHotSpotEnum
	kCursorHotSpotTopRight        =47875      # from enum CursorHotSpotEnum
	kCursorBuiltInArrow           =47621      # from enum CursorTypeEnum
	kCursorBuiltInArrowCursor     =47622      # from enum CursorTypeEnum
	kCursorBuiltInCommonSketchDrag=47636      # from enum CursorTypeEnum
	kCursorBuiltInCrosshair       =47623      # from enum CursorTypeEnum
	kCursorBuiltInCursorSelComp   =47624      # from enum CursorTypeEnum
	kCursorBuiltInCursorSelTrail  =47625      # from enum CursorTypeEnum
	kCursorBuiltInDynpan          =47626      # from enum CursorTypeEnum
	kCursorBuiltInDynzoom         =47627      # from enum CursorTypeEnum
	kCursorBuiltInLineCursor      =47628      # from enum CursorTypeEnum
	kCursorBuiltInLookat          =47629      # from enum CursorTypeEnum
	kCursorBuiltInMeasureCmd      =47630      # from enum CursorTypeEnum
	kCursorBuiltInPushpinCursor   =47631      # from enum CursorTypeEnum
	kCursorBuiltInSelectArrow     =47633      # from enum CursorTypeEnum
	kCursorBuiltInSelectView      =47634      # from enum CursorTypeEnum
	kCursorBuiltInSketch          =47635      # from enum CursorTypeEnum
	kCursorBuiltInSketch3DEditCursor=47632      # from enum CursorTypeEnum
	kCursorBuiltInZoom            =47637      # from enum CursorTypeEnum
	kCursorBuiltInZoomSel         =47638      # from enum CursorTypeEnum
	kCursorTypeCustom             =47619      # from enum CursorTypeEnum
	kCursorTypeDefault            =47617      # from enum CursorTypeEnum
	kCursorTypeWindows            =47618      # from enum CursorTypeEnum
	kBSplineCurve2d               =5256       # from enum Curve2dTypeEnum
	kCircleCurve2d                =5252       # from enum Curve2dTypeEnum
	kCircularArcCurve2d           =5253       # from enum Curve2dTypeEnum
	kEllipseFullCurve2d           =5254       # from enum Curve2dTypeEnum
	kEllipticalArcCurve2d         =5255       # from enum Curve2dTypeEnum
	kLineCurve2d                  =5250       # from enum Curve2dTypeEnum
	kLineSegmentCurve2d           =5251       # from enum Curve2dTypeEnum
	kPolylineCurve2d              =5257       # from enum Curve2dTypeEnum
	kUnknownCurve2d               =5249       # from enum Curve2dTypeEnum
	kExplicit                     =98306      # from enum CurveEquationTypeEnum
	kParametric                   =98305      # from enum CurveEquationTypeEnum
	CurveGeometryForm_NURBS       =1          # from enum CurveGeometryFormEnum
	CurveGeometryForm_Not_NURBS   =2          # from enum CurveGeometryFormEnum
	kBSplineCurve                 =5128       # from enum CurveTypeEnum
	kCircleCurve                  =5124       # from enum CurveTypeEnum
	kCircularArcCurve             =5125       # from enum CurveTypeEnum
	kEllipseFullCurve             =5126       # from enum CurveTypeEnum
	kEllipticalArcCurve           =5127       # from enum CurveTypeEnum
	kLineCurve                    =5122       # from enum CurveTypeEnum
	kLineSegmentCurve             =5123       # from enum CurveTypeEnum
	kPolylineCurve                =5129       # from enum CurveTypeEnum
	kUnknownCurve                 =5121       # from enum CurveTypeEnum
	kDegreesAnglePrecision        =85522      # from enum CustomPropertyPrecisionEnum
	kEightDecimalPlacesPrecision  =85513      # from enum CustomPropertyPrecisionEnum
	kEighthsFractionalLengthPrecision=85517      # from enum CustomPropertyPrecisionEnum
	kFiveDecimalPlacesPrecision   =85510      # from enum CustomPropertyPrecisionEnum
	kFourDecimalPlacesPrecision   =85509      # from enum CustomPropertyPrecisionEnum
	kHalfFractionalLengthPrecision=85515      # from enum CustomPropertyPrecisionEnum
	kMinutesAnglePrecision        =85523      # from enum CustomPropertyPrecisionEnum
	kOneDecimalPlacePrecision     =85506      # from enum CustomPropertyPrecisionEnum
	kOneTwentyEighthsFractionalLengthPrecision=85521      # from enum CustomPropertyPrecisionEnum
	kQuarterFractionalLengthPrecision=85516      # from enum CustomPropertyPrecisionEnum
	kSecondsAnglePrecision        =85524      # from enum CustomPropertyPrecisionEnum
	kSecondsFourDecimalPlaceAnglePrecision=85528      # from enum CustomPropertyPrecisionEnum
	kSecondsOneDecimalPlaceAnglePrecision=85525      # from enum CustomPropertyPrecisionEnum
	kSecondsThreeDecimalPlaceAnglePrecision=85527      # from enum CustomPropertyPrecisionEnum
	kSecondsTwoDecimalPlaceAnglePrecision=85526      # from enum CustomPropertyPrecisionEnum
	kSevenDecimalPlacesPrecision  =85512      # from enum CustomPropertyPrecisionEnum
	kSixDecimalPlacesPrecision    =85511      # from enum CustomPropertyPrecisionEnum
	kSixteenthsFractionalLengthPrecision=85518      # from enum CustomPropertyPrecisionEnum
	kSixtyFourthsFractionalLengthPrecision=85520      # from enum CustomPropertyPrecisionEnum
	kThirtySecondsFractionalLengthPrecision=85519      # from enum CustomPropertyPrecisionEnum
	kThreeDecimalPlacesPrecision  =85508      # from enum CustomPropertyPrecisionEnum
	kTwoDecimalPlacesPrecision    =85507      # from enum CustomPropertyPrecisionEnum
	kZeroDecimalPlacePrecision    =85505      # from enum CustomPropertyPrecisionEnum
	kZeroFractionalLengthPrecision=85514      # from enum CustomPropertyPrecisionEnum
	kNumberPropertyType           =85250      # from enum CustomPropertyTypeEnum
	kTextPropertyType             =85249      # from enum CustomPropertyTypeEnum
	kAccelerationImposeMotion     =96515      # from enum DSDOFImposedMotionTypeEnum
	kNoImposeMotion               =96516      # from enum DSDOFImposedMotionTypeEnum
	kPositionImposeMotion         =96513      # from enum DSDOFImposedMotionTypeEnum
	kVelocityImposeMotion         =96514      # from enum DSDOFImposedMotionTypeEnum
	kRotationDegreeOfFreedomType  =98049      # from enum DSDegreeOfFreedomTypeEnum
	kTranslationDegreeOfFreedomType=98050      # from enum DSDegreeOfFreedomTypeEnum
	kCubicRampInterpolationType   =96258      # from enum DSGraphInterpolationTypeEnum
	kCycloidInterpolationType     =96259      # from enum DSGraphInterpolationTypeEnum
	kFormulaInterpolationType     =96266      # from enum DSGraphInterpolationTypeEnum
	kHarmonicInterpolationType    =96262      # from enum DSGraphInterpolationTypeEnum
	kLinearRampInterpolationType  =96257      # from enum DSGraphInterpolationTypeEnum
	kModifiedSineInterpolationType=96263      # from enum DSGraphInterpolationTypeEnum
	kModifiedTrapezoidInterpolationType=96264      # from enum DSGraphInterpolationTypeEnum
	kPolynomialInterpolationType  =96261      # from enum DSGraphInterpolationTypeEnum
	kSineInterpolationType        =96260      # from enum DSGraphInterpolationTypeEnum
	kSplineInterpolationType      =96265      # from enum DSGraphInterpolationTypeEnum
	kDSJointType3DPointInCyl      =92981      # from enum DSJointTypeEnum
	kDSJointType3DPointInSphere   =92979      # from enum DSJointTypeEnum
	kDSJointType3DPointOnCyl      =92980      # from enum DSJointTypeEnum
	kDSJointType3DPointOnSphere   =92978      # from enum DSJointTypeEnum
	kDSJointType3DPointPlane      =92977      # from enum DSJointTypeEnum
	kDSJointType3DSphereInCyl     =92976      # from enum DSJointTypeEnum
	kDSJointType3DSphereInSphere  =92974      # from enum DSJointTypeEnum
	kDSJointType3DSphereOnCyl     =92975      # from enum DSJointTypeEnum
	kDSJointType3DSphereOnSphere  =92973      # from enum DSJointTypeEnum
	kDSJointType3DSpherePlane     =92972      # from enum DSJointTypeEnum
	kDSJointTypeAcuator           =92983      # from enum DSJointTypeEnum
	kDSJointTypeBelt1C            =92947      # from enum DSJointTypeEnum
	kDSJointTypeCurveCurveJct     =92971      # from enum DSJointTypeEnum
	kDSJointTypeCylindrical       =92939      # from enum DSJointTypeEnum
	kDSJointTypeDiscInDiscJct     =92967      # from enum DSJointTypeEnum
	kDSJointTypeDiscLineJct       =92964      # from enum DSJointTypeEnum
	kDSJointTypeDiscOnDiscJct     =92965      # from enum DSJointTypeEnum
	kDSJointTypeDiscSegmentJct    =92970      # from enum DSJointTypeEnum
	kDSJointTypeHeliCouple        =92958      # from enum DSJointTypeEnum
	kDSJointTypeHeliScrew1C       =92946      # from enum DSJointTypeEnum
	kDSJointTypeImpact3D          =92982      # from enum DSJointTypeEnum
	kDSJointTypeLinePlane         =92932      # from enum DSJointTypeEnum
	kDSJointTypeLinePlaneInv      =92938      # from enum DSJointTypeEnum
	kDSJointTypePivot             =92940      # from enum DSJointTypeEnum
	kDSJointTypePlanar3D          =92934      # from enum DSJointTypeEnum
	kDSJointTypePointInDiscJct    =92968      # from enum DSJointTypeEnum
	kDSJointTypePointLine         =92933      # from enum DSJointTypeEnum
	kDSJointTypePointLineInv      =92937      # from enum DSJointTypeEnum
	kDSJointTypePointLineJct      =92963      # from enum DSJointTypeEnum
	kDSJointTypePointOnDiscJct    =92966      # from enum DSJointTypeEnum
	kDSJointTypePointPlane        =92931      # from enum DSJointTypeEnum
	kDSJointTypePointPlaneInv     =92936      # from enum DSJointTypeEnum
	kDSJointTypePointSegmentJct   =92969      # from enum DSJointTypeEnum
	kDSJointTypePrismatic         =92941      # from enum DSJointTypeEnum
	kDSJointTypeRigidity          =92929      # from enum DSJointTypeEnum
	kDSJointTypeRollConeInCone1C  =92952      # from enum DSJointTypeEnum
	kDSJointTypeRollConeOnCone1C  =92951      # from enum DSJointTypeEnum
	kDSJointTypeRollConeOnPlane1C =92950      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscInDisc1C  =92949      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscInDisc2C  =92945      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscLine1C    =92953      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscLine2C    =92943      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscOnDisc1C  =92948      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscOnDisc2C  =92944      # from enum DSJointTypeEnum
	kDSJointTypeRollDiskCurve2C   =92961      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscCurve1C   =92962      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscInDisc1C  =92954      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscLine1C    =92956      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscOnDisc1C  =92955      # from enum DSJointTypeEnum
	kDSJointTypeSlidPointCurve1C  =92960      # from enum DSJointTypeEnum
	kDSJointTypeSlidPointDisk1C   =92957      # from enum DSJointTypeEnum
	kDSJointTypeSpatial           =92930      # from enum DSJointTypeEnum
	kDSJointTypeSpherical         =92935      # from enum DSJointTypeEnum
	kDSJointTypeUndefined         =92942      # from enum DSJointTypeEnum
	kDSJointTypeWormGearCouple    =92959      # from enum DSJointTypeEnum
	kForceLoadType                =96002      # from enum DSLoadTypeEnum
	kTorqueLoadType               =96001      # from enum DSLoadTypeEnum
	kAcceleration1ResultType      =96771      # from enum DSResultTypeEnum
	kDrivingForceUImposed1ResultType=96772      # from enum DSResultTypeEnum
	kExtentLengthResultType       =96773      # from enum DSResultTypeEnum
	kExtentVelocityResultType     =96774      # from enum DSResultTypeEnum
	kForceResultType              =96775      # from enum DSResultTypeEnum
	kForceXResultType             =96776      # from enum DSResultTypeEnum
	kForceYResultType             =96777      # from enum DSResultTypeEnum
	kForceZResultType             =96778      # from enum DSResultTypeEnum
	kMomentResultType             =96779      # from enum DSResultTypeEnum
	kMomentXResultType            =96780      # from enum DSResultTypeEnum
	kMomentYResultType            =96781      # from enum DSResultTypeEnum
	kMomentZResultType            =96782      # from enum DSResultTypeEnum
	kPosition1ResultType          =96769      # from enum DSResultTypeEnum
	kTraceAccelerationResultType  =96783      # from enum DSResultTypeEnum
	kTraceAccelerationXResultType =96784      # from enum DSResultTypeEnum
	kTraceAccelerationYResultType =96785      # from enum DSResultTypeEnum
	kTraceAccelerationZResultType =96786      # from enum DSResultTypeEnum
	kTracePositionResultType      =96787      # from enum DSResultTypeEnum
	kTracePositionXResultType     =96788      # from enum DSResultTypeEnum
	kTracePositionYResultType     =96789      # from enum DSResultTypeEnum
	kTracePositionZResultType     =96790      # from enum DSResultTypeEnum
	kTraceVelocityResultType      =96791      # from enum DSResultTypeEnum
	kTraceVelocityXResultType     =96792      # from enum DSResultTypeEnum
	kTraceVelocityYResultType     =96793      # from enum DSResultTypeEnum
	kTraceVelocityZResultType     =96794      # from enum DSResultTypeEnum
	kVelocity1ResultType          =96770      # from enum DSResultTypeEnum
	kBasicDWFPublish              =62721      # from enum DWFPublishModeEnum
	kCompleteDWFPublish           =62722      # from enum DWFPublishModeEnum
	kCustomDWFPublish             =62723      # from enum DWFPublishModeEnum
	kAutoCAD2000                  =86529      # from enum DWGFileVersionEnum
	kAutoCAD2004                  =86530      # from enum DWGFileVersionEnum
	kAutoCAD2007                  =86531      # from enum DWGFileVersionEnum
	kAutoCAD2010                  =86532      # from enum DWGFileVersionEnum
	kAutoCAD2013                  =86533      # from enum DWGFileVersionEnum
	kAddRefWatchType              =1          # from enum DebugWatchType
	kNoneWatchType                =0          # from enum DebugWatchType
	kQueryInterfaceWatchType      =4          # from enum DebugWatchType
	kReleaseWatchType             =2          # from enum DebugWatchType
	kCommaDecimalMarker           =41474      # from enum DecimalMarkerTypeEnum
	kPeriodDecimalMarker          =41473      # from enum DecimalMarkerTypeEnum
	kDWGDefaultDrawingFileType    =69633      # from enum DefaultDrawingFileTypeEnum
	kIDWDefaultDrawingFileType    =69634      # from enum DefaultDrawingFileTypeEnum
	kLastUsedDefaultLayerStyle    =69890      # from enum DefaultLayerStyleEnum
	kStandardDefaultLayerStyle    =69889      # from enum DefaultLayerStyleEnum
	kImportNonInventorDWGFile     =70146      # from enum DefaultNonInventorDWGFileOpenBehaviorEnum
	kRegularOpenNonInventorDWGFile=70145      # from enum DefaultNonInventorDWGFileOpenBehaviorEnum
	kLastUsedDefaultObjectStyle   =70402      # from enum DefaultObjectStyleEnum
	kStandardDefaultObjectStyle   =70401      # from enum DefaultObjectStyleEnum
	kDerivedBoundingBox           =27141      # from enum DerivedComponentOptionEnum
	kDerivedExcludeAll            =27138      # from enum DerivedComponentOptionEnum
	kDerivedIncludeAll            =27137      # from enum DerivedComponentOptionEnum
	kDerivedIndividualDefined     =27140      # from enum DerivedComponentOptionEnum
	kDerivedIntersect             =27142      # from enum DerivedComponentOptionEnum
	kDerivedSubtractAll           =27139      # from enum DerivedComponentOptionEnum
	kDeriveAsMultipleBodies       =80643      # from enum DerivedComponentStyleEnum
	kDeriveAsSingleBodyNoSeams    =80642      # from enum DerivedComponentStyleEnum
	kDeriveAsSingleBodyWithSeams  =80641      # from enum DerivedComponentStyleEnum
	kDeriveAsWorkSurface          =80644      # from enum DerivedComponentStyleEnum
	kDerivedRemoveNone            =88577      # from enum DerivedGeometryRemovalEnum
	kDerivedRemovePartsAndFaces   =88579      # from enum DerivedGeometryRemovalEnum
	kDerivedRemovePartsOnly       =88578      # from enum DerivedGeometryRemovalEnum
	kDerivedPatchAll              =88322      # from enum DerivedHolePatchEnum
	kDerivedPatchNone             =88321      # from enum DerivedHolePatchEnum
	kDerivedPatchRange            =88323      # from enum DerivedHolePatchEnum
	kDerivedPartMirrorPlaneXY     =27393      # from enum DerivedPartMirrorPlaneEnum
	kDerivedPartMirrorPlaneXZ     =27395      # from enum DerivedPartMirrorPlaneEnum
	kDerivedPartMirrorPlaneYZ     =27394      # from enum DerivedPartMirrorPlaneEnum
	kDerivedPartNoMirrorPlane     =27396      # from enum DerivedPartMirrorPlaneEnum
	kDerivedDrawingFilename       =29700      # from enum DerivedPropertyTypeEnum
	kDerivedDrawingFilenameAndPath=29701      # from enum DerivedPropertyTypeEnum
	kDerivedDrawingVersion        =29702      # from enum DerivedPropertyTypeEnum
	kDerivedModelFilename         =29697      # from enum DerivedPropertyTypeEnum
	kDerivedModelFilenameAndPath  =29698      # from enum DerivedPropertyTypeEnum
	kDerivedModelVersion          =29699      # from enum DerivedPropertyTypeEnum
	kDerivedNumberOfSheets        =29703      # from enum DerivedPropertyTypeEnum
	kDerivedSheetNumber           =29704      # from enum DerivedPropertyTypeEnum
	kDerivedSheetRevision         =29706      # from enum DerivedPropertyTypeEnum
	kDerivedSheetSize             =29705      # from enum DerivedPropertyTypeEnum
	kAllVisibleDesignViewType     =57349      # from enum DesignViewTypeEnum
	kLastActiveDesignViewType     =57351      # from enum DesignViewTypeEnum
	kMasterDesignViewType         =57345      # from enum DesignViewTypeEnum
	kNothingVisibleDesignViewType =57350      # from enum DesignViewTypeEnum
	kPrivateDesignViewType        =57346      # from enum DesignViewTypeEnum
	kPublicDesignViewType         =57347      # from enum DesignViewTypeEnum
	kTransientDesignViewType      =57348      # from enum DesignViewTypeEnum
	_kEditDialogStyle             =56836      # from enum DialogStyleEnum
	kFullyDockedDialogStyle       =56833      # from enum DialogStyleEnum
	kNoButtonsDialogStyle         =56835      # from enum DialogStyleEnum
	kNoTitleBarDialogStyle        =56834      # from enum DialogStyleEnum
	kAlignedAlignmentType         =50178      # from enum DimensionAlignmentTypeEnum
	kDefaultAlignmentType         =50177      # from enum DimensionAlignmentTypeEnum
	kHorizontalAlignmentType      =50179      # from enum DimensionAlignmentTypeEnum
	kVerticalAlignmentType        =50180      # from enum DimensionAlignmentTypeEnum
	kAlwaysRelaxDimensionConstraints=58115      # from enum DimensionConstraintsRelaxationEnum
	kNeverRelaxDimensionConstraints=58113      # from enum DimensionConstraintsRelaxationEnum
	kNoEquationRelaxDimensionConstraints=58114      # from enum DimensionConstraintsRelaxationEnum
	kPromptRelaxDimensionConstraints=58116      # from enum DimensionConstraintsRelaxationEnum
	kDimensionDisplayAsExpession  =34819      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsExpression =34819      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsName       =34818      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsPreciseValue=34821      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsToerance   =34820      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsTolerance  =34820      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsValue      =34817      # from enum DimensionDisplayTypeEnum
	kAlignedDim                   =19203      # from enum DimensionOrientationEnum
	kHorizontalDim                =19201      # from enum DimensionOrientationEnum
	kVerticalDim                  =19202      # from enum DimensionOrientationEnum
	kAdjacentFormat               =41985      # from enum DimensionStyleFormatEnum
	kAdjacentWithBracketsForAlternateFormat=41987      # from enum DimensionStyleFormatEnum
	kAdjacentWithBracketsForPrimaryFormat=41986      # from enum DimensionStyleFormatEnum
	kBelowFormat                  =41988      # from enum DimensionStyleFormatEnum
	kBelowWithBracketsForAlternateFormat=41990      # from enum DimensionStyleFormatEnum
	kBelowWithBracketsForPrimaryFormat=41989      # from enum DimensionStyleFormatEnum
	kNoAlternateUnits             =41991      # from enum DimensionStyleFormatEnum
	kMaintainAllTextAlignment     =55555      # from enum DimensionTextAlignmentEnum
	kMaintainCenteredTextAlignment=55554      # from enum DimensionTextAlignmentEnum
	kMaintainViewPositionAlignment=55553      # from enum DimensionTextAlignmentEnum
	kAboveForHorizontal           =101377     # from enum DimensionTextModifierEnum
	kNoModifier                   =101379     # from enum DimensionTextModifierEnum
	kOutsideDimensionLine         =101378     # from enum DimensionTextModifierEnum
	kOutsideForAngles30to210      =101380     # from enum DimensionTextModifierEnum
	kInlineAlignedDimensionText   =101123     # from enum DimensionTextOrientationEnum
	kInlineHorizontalDimensionText=101122     # from enum DimensionTextOrientationEnum
	kParallelAllAboveDimensionText=101124     # from enum DimensionTextOrientationEnum
	kParallelDimensionText        =101121     # from enum DimensionTextOrientationEnum
	kParallelFirstAboveDimensionText=101125     # from enum DimensionTextOrientationEnum
	kParallelHorizontalDimensionText=101126     # from enum DimensionTextOrientationEnum
	kAlignedDimensionType         =60161      # from enum DimensionTypeEnum
	kAngularDimensionType         =60169      # from enum DimensionTypeEnum
	kAngularForeshortenedDimensionType=60170      # from enum DimensionTypeEnum
	kArcLengthDimensionType       =60164      # from enum DimensionTypeEnum
	kArcLengthForeshortenedDimensionType=60168      # from enum DimensionTypeEnum
	kDiametricDimensionType       =60166      # from enum DimensionTypeEnum
	kHorizontalDimensionType      =60162      # from enum DimensionTypeEnum
	kLinearForeshortenedDimensionType=60167      # from enum DimensionTypeEnum
	kSymmetricDimensionType       =60165      # from enum DimensionTypeEnum
	kVerticalDimensionType        =60163      # from enum DimensionTypeEnum
	kZeroToleranceDisplayFull     =101889     # from enum DimensionZeroToleranceDisplayEnum
	kZeroToleranceDisplayNoTrailingZeros=101890     # from enum DimensionZeroToleranceDisplayEnum
	kZeroToleranceDisplayNoTrailingZerosNoSign=101891     # from enum DimensionZeroToleranceDisplayEnum
	kZeroToleranceDisplaySuppressDisplay=101892     # from enum DimensionZeroToleranceDisplayEnum
	kDirectEditDeleteOperationType=105732     # from enum DirectEditOperationTypeEnum
	kDirectEditMoveOperationType  =105729     # from enum DirectEditOperationTypeEnum
	kDirectEditRotateOperationType=105731     # from enum DirectEditOperationTypeEnum
	kDirectEditScaleOperationType =105734     # from enum DirectEditOperationTypeEnum
	kDirectEditSizeOperationType  =105730     # from enum DirectEditOperationTypeEnum
	kDirectEditUnknownOperationType=105733     # from enum DirectEditOperationTypeEnum
	kBothDirections               =771        # from enum DirectionEnum
	kInwardDirection              =770        # from enum DirectionEnum
	kOutwardDirection             =769        # from enum DirectionEnum
	kDecimalFormat                =78340      # from enum DisplayFormatEnum
	kFractionalDiagonalStackedFormat=78339      # from enum DisplayFormatEnum
	kFractionalHorizontalStackedFormat=78338      # from enum DisplayFormatEnum
	kFractionalNotStackedFormat   =78337      # from enum DisplayFormatEnum
	kHiddenEdgeRendering          =8707       # from enum DisplayModeEnum
	kIllustrationRendering        =8715       # from enum DisplayModeEnum
	kMonochromeRendering          =8713       # from enum DisplayModeEnum
	kRealisticRendering           =8709       # from enum DisplayModeEnum
	kShadedRendering              =8708       # from enum DisplayModeEnum
	kShadedWithEdgesRendering     =8710       # from enum DisplayModeEnum
	kShadedWithHiddenEdgesRendering=8707       # from enum DisplayModeEnum
	kTechnicalIllustrationRendering=8716       # from enum DisplayModeEnum
	kWatercolorRendering          =8714       # from enum DisplayModeEnum
	kWireframeNoHiddenEdges       =8711       # from enum DisplayModeEnum
	kWireframeRendering           =8706       # from enum DisplayModeEnum
	kWireframeWithHiddenEdgesRendering=8712       # from enum DisplayModeEnum
	kDefaultDisplayMode           =54273      # from enum DisplayModeSourceTypeEnum
	kOverrideDisplayMode          =54274      # from enum DisplayModeSourceTypeEnum
	kMediumDisplayQuality         =58882      # from enum DisplayQualityEnum
	kRoughDisplayQuality          =58883      # from enum DisplayQualityEnum
	kSmoothDisplayQuality         =58881      # from enum DisplayQualityEnum
	kSmootherDisplayQuality       =58884      # from enum DisplayQualityEnum
	kFrontFacing                  =26113      # from enum DisplayTransformBehaviorEnum
	kFrontFacingAndPixelScaling   =26115      # from enum DisplayTransformBehaviorEnum
	kNoTransformBehaviors         =26116      # from enum DisplayTransformBehaviorEnum
	kPixelScaling                 =26114      # from enum DisplayTransformBehaviorEnum
	kDockBottom                   =1          # from enum DockingStateEnum
	kDockLastKnown                =32         # from enum DockingStateEnum
	kDockLeft                     =2          # from enum DockingStateEnum
	kDockRight                    =4          # from enum DockingStateEnum
	kDockTop                      =8          # from enum DockingStateEnum
	kFloat                        =16         # from enum DockingStateEnum
	kInterested                   =68866      # from enum DocumentInterestTypeEnum
	kNotInterested                =68865      # from enum DocumentInterestTypeEnum
	kDocumentExpressLoadState     =103938     # from enum DocumentLoadStateEnum
	kDocumentFullLoadState        =103939     # from enum DocumentLoadStateEnum
	kDocumentLiteLoadState        =103938     # from enum DocumentLoadStateEnum
	kDocumentPartialLoadState     =103940     # from enum DocumentLoadStateEnum
	kDocumentUnknownLoadState     =103937     # from enum DocumentLoadStateEnum
	kAssemblyDocumentObject       =12291      # from enum DocumentTypeEnum
	kDesignElementDocumentObject  =12294      # from enum DocumentTypeEnum
	kDrawingDocumentObject        =12292      # from enum DocumentTypeEnum
	kForeignModelDocumentObject   =12295      # from enum DocumentTypeEnum
	kNoDocument                   =12297      # from enum DocumentTypeEnum
	kPartDocumentObject           =12290      # from enum DocumentTypeEnum
	kPresentationDocumentObject   =12293      # from enum DocumentTypeEnum
	kSATFileDocumentObject        =12296      # from enum DocumentTypeEnum
	kUnknownDocumentObject        =12289      # from enum DocumentTypeEnum
	kDoubleBend45Degree           =74754      # from enum DoubleBendTypeEnum
	kDoubleBend90Degree           =74755      # from enum DoubleBendTypeEnum
	kDoubleBendFixedEdges         =74753      # from enum DoubleBendTypeEnum
	kDoubleBendFullRadius         =74756      # from enum DoubleBendTypeEnum
	kDoubleBendNoBend             =74758      # from enum DoubleBendTypeEnum
	kDoubleBendSingle             =74757      # from enum DoubleBendTypeEnum
	kAsymmetricDraftAngles        =108291     # from enum DraftAngleConstraintTypeEnum
	kBothSidesMinDraftAngle       =108294     # from enum DraftAngleConstraintTypeEnum
	kOneWayDraftAngle             =108289     # from enum DraftAngleConstraintTypeEnum
	kSideOneMinDraftAngle         =108292     # from enum DraftAngleConstraintTypeEnum
	kSideTwoMinDraftAngle         =108293     # from enum DraftAngleConstraintTypeEnum
	kSymmetricDraftAngles         =108290     # from enum DraftAngleConstraintTypeEnum
	kANSI_DraftingStandard        =9731       # from enum DraftingStandardEnum
	kBSI_DraftingStandard         =9732       # from enum DraftingStandardEnum
	kDIN_DraftingStandard         =9733       # from enum DraftingStandardEnum
	kDefault_DraftingStandard     =9729       # from enum DraftingStandardEnum
	kGB_DraftingStandard          =9734       # from enum DraftingStandardEnum
	kGOST_DraftingStandard        =9737       # from enum DraftingStandardEnum
	kISO_DraftingStandard         =9735       # from enum DraftingStandardEnum
	kJIS_DraftingStandard         =9736       # from enum DraftingStandardEnum
	kLegacyBSI_DraftingStandard   =9738       # from enum DraftingStandardEnum
	kLegacyDIN_DraftingStandard   =9739       # from enum DraftingStandardEnum
	kLegacyGB_DraftingStandard    =9740       # from enum DraftingStandardEnum
	kLegacyISO_DraftingStandard   =9741       # from enum DraftingStandardEnum
	kLegacyJIS_DraftingStandard   =9742       # from enum DraftingStandardEnum
	kOther_DraftingStandard       =9730       # from enum DraftingStandardEnum
	kDragStateCancelDrag          =37895      # from enum DragStateEnum
	kDragStateDragHandlerSelection=37889      # from enum DragStateEnum
	kDragStateEndDrag             =37892      # from enum DragStateEnum
	kDragStateOnDrag              =37891      # from enum DragStateEnum
	kDragStateResumeDrag          =37894      # from enum DragStateEnum
	kDragStateStartDrag           =37890      # from enum DragStateEnum
	kDragStateSuspendDrag         =37893      # from enum DragStateEnum
	kBendDownEdge                 =82691      # from enum DrawingEdgeTypeEnum
	kBendExtentEdge               =82692      # from enum DrawingEdgeTypeEnum
	kBendUpEdge                   =82690      # from enum DrawingEdgeTypeEnum
	kContourRollEdge              =82697      # from enum DrawingEdgeTypeEnum
	kPunchDownEdge                =82693      # from enum DrawingEdgeTypeEnum
	kPunchUpEdge                  =82696      # from enum DrawingEdgeTypeEnum
	kTangentEdge                  =82694      # from enum DrawingEdgeTypeEnum
	kThreadEdge                   =82689      # from enum DrawingEdgeTypeEnum
	kUnknownEdge                  =82695      # from enum DrawingEdgeTypeEnum
	k12x18InDrawingSheetSize      =9999       # from enum DrawingSheetSizeEnum
	k18x24InDrawingSheetSize      =10000      # from enum DrawingSheetSizeEnum
	k24x36InDrawingSheetSize      =10001      # from enum DrawingSheetSizeEnum
	k30x42InDrawingSheetSize      =10003      # from enum DrawingSheetSizeEnum
	k36x48InDrawingSheetSize      =10002      # from enum DrawingSheetSizeEnum
	k9x12InDrawingSheetSize       =9998       # from enum DrawingSheetSizeEnum
	kA0DrawingSheetSize           =9993       # from enum DrawingSheetSizeEnum
	kA1DrawingSheetSize           =9994       # from enum DrawingSheetSizeEnum
	kA2DrawingSheetSize           =9995       # from enum DrawingSheetSizeEnum
	kA3DrawingSheetSize           =9996       # from enum DrawingSheetSizeEnum
	kA4DrawingSheetSize           =9997       # from enum DrawingSheetSizeEnum
	kADrawingSheetSize            =9987       # from enum DrawingSheetSizeEnum
	kBDrawingSheetSize            =9988       # from enum DrawingSheetSizeEnum
	kCDrawingSheetSize            =9989       # from enum DrawingSheetSizeEnum
	kCustomDrawingSheetSize       =9986       # from enum DrawingSheetSizeEnum
	kDDrawingSheetSize            =9990       # from enum DrawingSheetSizeEnum
	kDefaultDrawingSheetSize      =9985       # from enum DrawingSheetSizeEnum
	kEDrawingSheetSize            =9991       # from enum DrawingSheetSizeEnum
	kFDrawingSheetSize            =9992       # from enum DrawingSheetSizeEnum
	kAssyCompositionOutOfDateDrawingSheet=4          # from enum DrawingSheetStatusBits
	kAssyPositionOutOfDateDrawingSheet=2          # from enum DrawingSheetStatusBits
	kGeomOutOfDateDrawingSheet    =1          # from enum DrawingSheetStatusBits
	kNoDataDrawingSheet           =128        # from enum DrawingSheetStatusBits
	kParameterizedTextOutOfDateDrawingSheet=32         # from enum DrawingSheetStatusBits
	kProcessingPreciseDisplayDrawingSheet=256        # from enum DrawingSheetStatusBits
	kResourceTemplateOutOfDateDrawingSheet=16         # from enum DrawingSheetStatusBits
	kStandardOutOfDateDrawingSheet=8          # from enum DrawingSheetStatusBits
	kUnknownOutOfDateDrawingSheet =64         # from enum DrawingSheetStatusBits
	kUpToDateDrawingSheet         =0          # from enum DrawingSheetStatusBits
	kHorizontalViewAlignment      =80641      # from enum DrawingViewAlignmentEnum
	kInPositionViewAlignment      =80643      # from enum DrawingViewAlignmentEnum
	kVerticalViewAlignment        =80642      # from enum DrawingViewAlignmentEnum
	kFromBaseDrawingViewStyle     =32260      # from enum DrawingViewStyleEnum
	kHiddenLineDrawingViewStyle   =32257      # from enum DrawingViewStyleEnum
	kHiddenLineRemovedDrawingViewStyle=32258      # from enum DrawingViewStyleEnum
	kShadedDrawingViewStyle       =32259      # from enum DrawingViewStyleEnum
	kShadedHiddenLineDrawingViewStyle=32261      # from enum DrawingViewStyleEnum
	kAssociativeDraftDrawingViewType=10506      # from enum DrawingViewTypeEnum
	kAuxiliaryDrawingViewType     =10499      # from enum DrawingViewTypeEnum
	kCustomDrawingViewType        =10498      # from enum DrawingViewTypeEnum
	kDefaultDrawingViewType       =10497      # from enum DrawingViewTypeEnum
	kDetailDrawingViewType        =10502      # from enum DrawingViewTypeEnum
	kDraftDrawingViewType         =10505      # from enum DrawingViewTypeEnum
	kOLEAttachmentDrawingViewType =10500      # from enum DrawingViewTypeEnum
	kOverlayDrawingViewType       =10507      # from enum DrawingViewTypeEnum
	kProjectedDrawingViewType     =10504      # from enum DrawingViewTypeEnum
	kSectionDrawingViewType       =10503      # from enum DrawingViewTypeEnum
	kStandardDrawingViewType      =10501      # from enum DrawingViewTypeEnum
	kDriveAngleType               =100865     # from enum DriveTypeEnum
	kDriveAngularPositionType     =100868     # from enum DriveTypeEnum
	kDriveLinearPositionType      =100866     # from enum DriveTypeEnum
	kDriveOffsetType              =100867     # from enum DriveTypeEnum
	kAllConcave                   =27650      # from enum EdgeCollectionEnum
	kAllConvex                    =27651      # from enum EdgeCollectionEnum
	kTangentiallyConnected        =27649      # from enum EdgeCollectionEnum
	kUndefined                    =27652      # from enum EdgeCollectionEnum
	kEmbossEngraveFromPlane       =67331      # from enum EmbossTypeEnum
	kEmbossFromFace               =67329      # from enum EmbossTypeEnum
	kEngraveFromFace              =67330      # from enum EmbossTypeEnum
	kActivateEnvironmentState     =50945      # from enum EnvironmentStateEnum
	kRequestActivateEnvironmentState=50949      # from enum EnvironmentStateEnum
	kResumeEnvironmentState       =50947      # from enum EnvironmentStateEnum
	kSuspendEnvironmentState      =50946      # from enum EnvironmentStateEnum
	kTerminateEnvironmentState    =50948      # from enum EnvironmentStateEnum
	kAbort                        =4099       # from enum EventTimingEnum
	kAfter                        =4098       # from enum EventTimingEnum
	kBefore                       =4097       # from enum EventTimingEnum
	kExitToParent                 =63746      # from enum ExitTypeEnum
	kExitToPrevious               =63745      # from enum ExitTypeEnum
	kExitToTop                    =63747      # from enum ExitTypeEnum
	kFaceTangentiallyConnected    =40961      # from enum FaceCollectionEnum
	kFaceUndefined                =40962      # from enum FaceCollectionEnum
	kFixedEdgeFaceDraftDefinitionType=108033     # from enum FaceDraftDefinitionTypeEnum
	kFixedPlaneFaceDraftDefinitionType=108034     # from enum FaceDraftDefinitionTypeEnum
	kPartingToolFaceDraftDefinitionType=108035     # from enum FaceDraftDefinitionTypeEnum
	kFileNameMemberNameType       =81922      # from enum FactoryOptionsMemberNameTypeEnum
	kPartNumberMemberNameType     =81921      # from enum FactoryOptionsMemberNameTypeEnum
	kValueMemberNameType          =81923      # from enum FactoryOptionsMemberNameTypeEnum
	kNonePartNumberType           =82177      # from enum FactoryOptionsPartNumberTypeEnum
	kValuePartNumberType          =82178      # from enum FactoryOptionsPartNumberTypeEnum
	kConstantFamilyParameterValue =51457      # from enum FamilyParameterValueTypeEnum
	kCustomFamilyParameterValue   =51458      # from enum FamilyParameterValueTypeEnum
	kExpressionFamilyParameterValue=51459      # from enum FamilyParameterValueTypeEnum
	kMeanApproximation            =60674      # from enum FeatureApproximationTypeEnum
	kNeverTooThickApproximation   =60675      # from enum FeatureApproximationTypeEnum
	kNeverTooThinApproximation    =60676      # from enum FeatureApproximationTypeEnum
	kNoApproximation              =60673      # from enum FeatureApproximationTypeEnum
	kAnyCrossSection              =107027     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAnyLongitudinalSection       =107028     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAreaDiameter                 =107041     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAverageSize                  =107045     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kCircumferenceDiameter        =107040     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kClosingQuote                 =107014     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kCommonZone                   =107020     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kContactingFeature            =107029     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kDegree                       =107010     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kLeastSquaresAssociationCriterion=107037     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kLineElement                  =107024     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kLocalSizeDefinedByASphere    =107036     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMajorDiameter                =107022     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMaximumInscribedAssociationCriterion=107038     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMaximumSize                  =107043     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMedianSize                   =107046     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMidRangeSize                 =107047     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMinimumCircumscribedAssociationCriterion=107039     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMinimumSize                  =107044     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMinorDiameter                =107021     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kNotConvex                    =107025     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kNumero                       =107015     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kOpeningQuote                 =107013     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kOrientationConstraintOnly    =107034     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPitchDiameter                =107023     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPlaneSymbol                  =107033     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPlusMinus                    =107011     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPointSymbol                  =107031     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kRangeOfSizes                 =107048     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kSection                      =107012     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kSlopeLeft                    =107016     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kSlopeRight                   =107017     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kStraightLine                 =107032     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTOver2                       =107009     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTaperLeft                    =107018     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTaperRight                   =107019     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTwoPointSize                 =107035     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kUnequallyDisposedToleranceZone=107026     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kVariableDistance             =107030     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kVolumeDiameter               =107042     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAngleFeatureDimension        =93185      # from enum FeatureDimensionTypeEnum
	kCircularCountFeatureDimension=93186      # from enum FeatureDimensionTypeEnum
	kHoleFeatureDimension         =93187      # from enum FeatureDimensionTypeEnum
	kLinearFeatureDimension       =93188      # from enum FeatureDimensionTypeEnum
	kRadialFeatureDimension       =93189      # from enum FeatureDimensionTypeEnum
	kRectangularCountFeatureDimension=93190      # from enum FeatureDimensionTypeEnum
	kMicrosoftAccessFormat        =74497      # from enum FileFormatEnum
	kMicrosoftExcelFormat         =74498      # from enum FileFormatEnum
	kTextFileCommaDelimitedFormat =74502      # from enum FileFormatEnum
	kTextFileTabDelimitedFormat   =74501      # from enum FileFormatEnum
	kUnicodeTextFileCommaDelimitedFormat=74504      # from enum FileFormatEnum
	kUnicodeTextFileTabDelimitedFormat=74503      # from enum FileFormatEnum
	kdBASEIIIFormat               =74499      # from enum FileFormatEnum
	kdBASEIVFormat                =74500      # from enum FileFormatEnum
	kCopyFileMask                 =224        # from enum FileManagementEnum
	kDeleteFileMask               =1          # from enum FileManagementEnum
	kForceFile                    =1          # from enum FileManagementEnum
	kMoveFileMask                 =225        # from enum FileManagementEnum
	kNoForceFile                  =0          # from enum FileManagementEnum
	kOverwriteExistingFile        =32         # from enum FileManagementEnum
	kOverwriteReadOnlyFile        =128        # from enum FileManagementEnum
	kOverwriteReservedFile        =64         # from enum FileManagementEnum
	kExclusiveOwnership           =68611      # from enum FileOwnershipEnum
	kNoOwnership                  =68609      # from enum FileOwnershipEnum
	kSaveOwnership                =68610      # from enum FileOwnershipEnum
	kAssemblyFileType             =56323      # from enum FileTypeEnum
	kAssociativeCADFileType       =56328      # from enum FileTypeEnum
	kDesignElementFileType        =56326      # from enum FileTypeEnum
	kDrawingFileType              =56324      # from enum FileTypeEnum
	kForeignFileType              =56327      # from enum FileTypeEnum
	kPartFileType                 =56322      # from enum FileTypeEnum
	kPresentationFileType         =56325      # from enum FileTypeEnum
	kUnknownFileType              =56321      # from enum FileTypeEnum
	kOpenCurrentVersion           =57858      # from enum FileVersionEnum
	kOpenOldVersion               =57857      # from enum FileVersionEnum
	kRestoreOldVersionToCurrent   =57859      # from enum FileVersionEnum
	kEdgeFillet                   =61697      # from enum FilletTypeEnum
	kFaceFillet                   =61698      # from enum FilletTypeEnum
	kFullRoundFillet              =61699      # from enum FilletTypeEnum
	kBendDownFlatPatternEdge      =64005      # from enum FlatPatternEdgeTypeEnum
	kBendUpFlatPatternEdge        =64004      # from enum FlatPatternEdgeTypeEnum
	kTangentFlatPatternEdge       =64001      # from enum FlatPatternEdgeTypeEnum
	kFlatPatternBackFace          =106755     # from enum FlatPatternFaceTypeEnum
	kFlatPatternFrontFace         =106754     # from enum FlatPatternFaceTypeEnum
	kFlatPatternUnknownFace       =106753     # from enum FlatPatternFaceTypeEnum
	kFrontViewFromModel           =80388      # from enum FrontViewPlaneEnum
	kFrontViewXYPlane             =80385      # from enum FrontViewPlaneEnum
	kFrontViewXZPlane             =80387      # from enum FrontViewPlaneEnum
	kFrontViewYZPlane             =80386      # from enum FrontViewPlaneEnum
	kGDTArcLength                 =104211     # from enum GDTSymbolEnum
	kGDTBetween                   =104213     # from enum GDTSymbolEnum
	kGDTControlledRadius          =104209     # from enum GDTSymbolEnum
	kGDTDiameter                  =104199     # from enum GDTSymbolEnum
	kGDTFreeState                 =104197     # from enum GDTSymbolEnum
	kGDTLeastMaterialCondition    =104195     # from enum GDTSymbolEnum
	kGDTMaximumMaterialCondition  =104194     # from enum GDTSymbolEnum
	kGDTNoSymbol                  =104193     # from enum GDTSymbolEnum
	kGDTProjectedToleranceZone    =104196     # from enum GDTSymbolEnum
	kGDTRadius                    =104201     # from enum GDTSymbolEnum
	kGDTReference                 =104210     # from enum GDTSymbolEnum
	kGDTSphericalDiameter         =104200     # from enum GDTSymbolEnum
	kGDTSphericalRadius           =104208     # from enum GDTSymbolEnum
	kGDTStatisticalTolerance      =104212     # from enum GDTSymbolEnum
	kGDTTangentPlane              =104198     # from enum GDTSymbolEnum
	kBooleanGeneralData           =52481      # from enum GeneralDataTypeEnum
	kCollectionGeneralData        =52482      # from enum GeneralDataTypeEnum
	kDoubleGeneralData            =52483      # from enum GeneralDataTypeEnum
	kIDispatchGeneralData         =52486      # from enum GeneralDataTypeEnum
	kIntegerGeneralData           =52484      # from enum GeneralDataTypeEnum
	kStringGeneralData            =52485      # from enum GeneralDataTypeEnum
	kVTableGeneralData            =52487      # from enum GeneralDataTypeEnum
	kProjectedGeneralDimension    =72194      # from enum GeneralDimensionTypeEnum
	kTrueGeneralDimension         =72193      # from enum GeneralDimensionTypeEnum
	kAngularity                   =32         # from enum GeometricCharacteristicEnum
	kAxiality                     =524288     # from enum GeometricCharacteristicEnum
	kAxisIntersection             =32768      # from enum GeometricCharacteristicEnum
	kCircularRunout               =1024       # from enum GeometricCharacteristicEnum
	kCircularRunoutFilled         =65536      # from enum GeometricCharacteristicEnum
	kCircularity                  =4          # from enum GeometricCharacteristicEnum
	kConcentricityAndCoaxiality   =512        # from enum GeometricCharacteristicEnum
	kCylindricity                 =8192       # from enum GeometricCharacteristicEnum
	kFlatness                     =2          # from enum GeometricCharacteristicEnum
	kParallelProfile              =16384      # from enum GeometricCharacteristicEnum
	kParallelism                  =128        # from enum GeometricCharacteristicEnum
	kPerpendicularity             =64         # from enum GeometricCharacteristicEnum
	kPosition                     =256        # from enum GeometricCharacteristicEnum
	kProfileOfASection            =262144     # from enum GeometricCharacteristicEnum
	kProfileOfAnyLine             =8          # from enum GeometricCharacteristicEnum
	kProfileOfAnySurface          =16         # from enum GeometricCharacteristicEnum
	kStraightness                 =1          # from enum GeometricCharacteristicEnum
	kSymmetry                     =2048       # from enum GeometricCharacteristicEnum
	kTotalRunout                  =4096       # from enum GeometricCharacteristicEnum
	kTotalRunoutFilled            =131072     # from enum GeometricCharacteristicEnum
	kAlwaysBreakGeometricConstraints=58370      # from enum GeometricConstraintsBreakageEnum
	kNeverBreakGeometricConstraints=58369      # from enum GeometricConstraintsBreakageEnum
	kPromptBreakGeometricConstraints=58371      # from enum GeometricConstraintsBreakageEnum
	kFixedGeometryMoveableStatus  =53507      # from enum GeometryMoveableStatusEnum
	kFreeToMoveGeometryMoveableStatus=53505      # from enum GeometryMoveableStatusEnum
	kMoveableByDimensionChangeGeometryMoveableStatus=53506      # from enum GeometryMoveableStatusEnum
	kUnknownGeometryMoveableStatus=53508      # from enum GeometryMoveableStatusEnum
	kConservativeOpenGLGraphicsDriver=61443      # from enum GraphicsDriverTypeEnum
	kDirect3D10GraphicsDriver     =61445      # from enum GraphicsDriverTypeEnum
	kDirect3D11GraphicsDriver     =61446      # from enum GraphicsDriverTypeEnum
	kDirect3DGraphicsDriver       =61441      # from enum GraphicsDriverTypeEnum
	kOpenGLGraphicsDriver         =61442      # from enum GraphicsDriverTypeEnum
	kSoftwareGraphics             =61444      # from enum GraphicsDriverTypeEnum
	kCoarseRes                    =128        # from enum GraphicsLevelsOfDetailEnum
	kFullScreenHighRes            =2048       # from enum GraphicsLevelsOfDetailEnum
	kMediumRes                    =512        # from enum GraphicsLevelsOfDetailEnum
	kMereDotRes                   =8          # from enum GraphicsLevelsOfDetailEnum
	kVeryCoarseRes                =32         # from enum GraphicsLevelsOfDetailEnum
	kZoomedInHighRes              =8192       # from enum GraphicsLevelsOfDetailEnum
	kConservativeGraphicsOptimization=55299      # from enum GraphicsOptimizationEnum
	kDriverGraphicsOptimization   =55300      # from enum GraphicsOptimizationEnum
	kFullGraphicsOptimization     =55298      # from enum GraphicsOptimizationEnum
	kRecommendedGraphicsOptimization=55297      # from enum GraphicsOptimizationEnum
	kAllGraphicsSelectable        =25347      # from enum GraphicsSelectabilityEnum
	kNoGraphicsSelectable         =25345      # from enum GraphicsSelectabilityEnum
	kSomeGraphicsSelectable       =25346      # from enum GraphicsSelectabilityEnum
	kCompatibilityGraphicsSetting =91651      # from enum GraphicsSettingTypeEnum
	kConservativeGraphicsSetting  =91652      # from enum GraphicsSettingTypeEnum
	kPerformanceGraphicsSetting   =91650      # from enum GraphicsSettingTypeEnum
	kQualityGraphicsSetting       =91649      # from enum GraphicsSettingTypeEnum
	kAllGraphicsVisible           =25091      # from enum GraphicsVisibilityEnum
	kNoGraphicsVisible            =25089      # from enum GraphicsVisibilityEnum
	kSomeGraphicsVisible          =25090      # from enum GraphicsVisibilityEnum
	kGroundShadow                 =69122      # from enum GroundShadowEnum
	kNoGroundShadow               =69121      # from enum GroundShadowEnum
	kXRayGroundShadow             =69123      # from enum GroundShadowEnum
	kEventCanceled                =515        # from enum HandlingCodeEnum
	kEventHandled                 =513        # from enum HandlingCodeEnum
	kEventNotHandled              =514        # from enum HandlingCodeEnum
	kHeadingAtBottom              =46338      # from enum HeadingPlacementEnum
	kHeadingAtTop                 =46337      # from enum HeadingPlacementEnum
	kNoHeading                    =46339      # from enum HeadingPlacementEnum
	kBeyondStopNodeHealth         =11785      # from enum HealthStatusEnum
	kCannotComputeHealth          =11783      # from enum HealthStatusEnum
	kDeletedHealth                =11782      # from enum HealthStatusEnum
	kDriverLostHealth             =11780      # from enum HealthStatusEnum
	kInErrorHealth                =11781      # from enum HealthStatusEnum
	kInconsistentHealth           =11786      # from enum HealthStatusEnum
	kInvalidLimitsHealth          =11789      # from enum HealthStatusEnum
	kJointDOFLockedHealth         =11790      # from enum HealthStatusEnum
	kNewlyAddedHealth             =11788      # from enum HealthStatusEnum
	kOutOfDateHealth              =11779      # from enum HealthStatusEnum
	kRedundantHealth              =11787      # from enum HealthStatusEnum
	kSuppressedHealth             =11784      # from enum HealthStatusEnum
	kUnknownHealth                =11777      # from enum HealthStatusEnum
	kUpToDateHealth               =11778      # from enum HealthStatusEnum
	kHeightDatumInner             =75522      # from enum HeightDatumTypeEnum
	kHeightDatumInnerOrtho        =75525      # from enum HeightDatumTypeEnum
	kHeightDatumOuter             =75521      # from enum HeightDatumTypeEnum
	kHeightDatumOuterOrtho        =75524      # from enum HeightDatumTypeEnum
	kHeightDatumTangent           =75523      # from enum HeightDatumTypeEnum
	kDoubleHemType                =75268      # from enum HemTypeEnum
	kRolledHemType                =75267      # from enum HemTypeEnum
	kSingleHemType                =75265      # from enum HemTypeEnum
	kTeardropHemType              =75266      # from enum HemTypeEnum
	kNumberOfHolesInFeature       =83969      # from enum HoleNoteQuantityEnum
	kNumberOfLikeHolesNormalToView=83970      # from enum HoleNoteQuantityEnum
	kConcentricPlacementType      =48899      # from enum HolePlacementTypeEnum
	kLinearPlacementType          =48898      # from enum HolePlacementTypeEnum
	kPointPlacementType           =48900      # from enum HolePlacementTypeEnum
	kSketchPlacementType          =48897      # from enum HolePlacementTypeEnum
	kCBoreDepthHoleProperty       =77569      # from enum HolePropertyEnum
	kCBoreDiameterHoleProperty    =77570      # from enum HolePropertyEnum
	kCSinkAngleHoleProperty       =77571      # from enum HolePropertyEnum
	kCSinkDepthHoleProperty       =77572      # from enum HolePropertyEnum
	kCSinkDiameterHoleProperty    =77573      # from enum HolePropertyEnum
	kCustomDesignationHoleProperty=77574      # from enum HolePropertyEnum
	kCustomHoleProperty           =77594      # from enum HolePropertyEnum
	kDescriptionHoleProperty      =77575      # from enum HolePropertyEnum
	kFastenerTypeHoleProperty     =77578      # from enum HolePropertyEnum
	kFasternerFitHoleProperty     =77576      # from enum HolePropertyEnum
	kFasternerSizeHoleProperty    =77577      # from enum HolePropertyEnum
	kHoleDepthHoleProperty        =77580      # from enum HolePropertyEnum
	kHoleDiameterHoleProperty     =77581      # from enum HolePropertyEnum
	kHoleHoleProperty             =77579      # from enum HolePropertyEnum
	kPunchAngleHoleProperty       =77582      # from enum HolePropertyEnum
	kPunchDepthHoleProperty       =77583      # from enum HolePropertyEnum
	kPunchDirectionHoleProperty   =77584      # from enum HolePropertyEnum
	kPunchIdHoleProperty          =77585      # from enum HolePropertyEnum
	kQuantityHoleProperty         =77586      # from enum HolePropertyEnum
	kTapDrillDiameterHoleProperty =77587      # from enum HolePropertyEnum
	kThreadClassHoleProperty      =77588      # from enum HolePropertyEnum
	kThreadDepthHoleProperty      =77589      # from enum HolePropertyEnum
	kThreadDesignationHoleProperty=77590      # from enum HolePropertyEnum
	kThreadPitchHoleProperty      =77591      # from enum HolePropertyEnum
	kXDIMHoleProperty             =77592      # from enum HolePropertyEnum
	kYDIMHoleProperty             =77593      # from enum HolePropertyEnum
	kFeatureTypeHoleTable         =77827      # from enum HoleTableTypeEnum
	kSelectionTypeHoleTable       =77826      # from enum HoleTableTypeEnum
	kViewTypeHoleTable            =77825      # from enum HoleTableTypeEnum
	kCounterBoreHole              =21507      # from enum HoleTypeEnum
	kCounterSinkHole              =21506      # from enum HoleTypeEnum
	kDrilledHole                  =21505      # from enum HoleTypeEnum
	kSpotFaceHole                 =21508      # from enum HoleTypeEnum
	kAlignTextCenter              =19969      # from enum HorizontalTextAlignmentEnum
	kAlignTextLeft                =19970      # from enum HorizontalTextAlignmentEnum
	kAlignTextRight               =19971      # from enum HorizontalTextAlignmentEnum
	kDataDropIOMechanism          =13058      # from enum IOMechanismEnum
	kFileBrowseIOMechanism        =13059      # from enum IOMechanismEnum
	kPasteSpecialIOMechanism      =13060      # from enum IOMechanismEnum
	kUnspecifiedIOMechanism       =13057      # from enum IOMechanismEnum
	kAmberColorTheme              =87554      # from enum IconsColorTypeEnum
	kCobaltColorTheme             =87553      # from enum IconsColorTypeEnum
	kCentimeterUnitsType          =110084     # from enum ImportUnitsTypeEnum
	kFootUnitsType                =110083     # from enum ImportUnitsTypeEnum
	kInchUnitsType                =110082     # from enum ImportUnitsTypeEnum
	kMeterUnitsType               =110086     # from enum ImportUnitsTypeEnum
	kMicronUnitsType              =110087     # from enum ImportUnitsTypeEnum
	kMillimeterUnitsType          =110085     # from enum ImportUnitsTypeEnum
	kSourceUnitsType              =110081     # from enum ImportUnitsTypeEnum
	kAImportedAsMultibodyPart     =108546     # from enum ImportedAssemblyOrganizationTypeEnum
	kImportedAsAssembly           =108545     # from enum ImportedAssemblyOrganizationTypeEnum
	kImportedAsCompositeFeaturePart=108547     # from enum ImportedAssemblyOrganizationTypeEnum
	kAExcludedStatus              =109570     # from enum ImportedModelEntityStatusEnum
	kImportedAsIndividualSurfacesStatus=109571     # from enum ImportedModelEntityStatusEnum
	kIncludedStatus               =109569     # from enum ImportedModelEntityStatusEnum
	kAliasEntityType              =109825     # from enum ImportedModelEntityTypeEnum
	kAliasLayerEntityType         =109826     # from enum ImportedModelEntityTypeEnum
	kAliasSurfaceEntityType       =109827     # from enum ImportedModelEntityTypeEnum
	kAssemblyEntityType           =109828     # from enum ImportedModelEntityTypeEnum
	kPartEntityType               =109829     # from enum ImportedModelEntityTypeEnum
	kSolidEntityType              =109830     # from enum ImportedModelEntityTypeEnum
	kSurfaceEntityType            =109831     # from enum ImportedModelEntityTypeEnum
	kMeshesModelGeometryType      =4          # from enum ImportedModelGeometryTypeEnum
	kSolidsModelGeometryType      =1          # from enum ImportedModelGeometryTypeEnum
	kSurfacesModelGeometryType    =2          # from enum ImportedModelGeometryTypeEnum
	kWiresModelGeometryType       =8          # from enum ImportedModelGeometryTypeEnum
	kImportedAsCompositeFeatures  =108802     # from enum ImportedSurfaceOrganizationTypeEnum
	kImportedAsSingleCompositeFeature=108803     # from enum ImportedSurfaceOrganizationTypeEnum
	kImportedAsSurfaceBodies      =108801     # from enum ImportedSurfaceOrganizationTypeEnum
	kWorkAxesWorkGeometryType     =4          # from enum ImportedWorkGeometryTypeEnum
	kWorkPlanesWorkGeometryType   =1          # from enum ImportedWorkGeometryTypeEnum
	kWorkPointsWorkGeometryType   =2          # from enum ImportedWorkGeometryTypeEnum
	kAmountOfValueIncrement       =102913     # from enum IncrementTypeEnum
	kNumberOfStepsIncrement       =102914     # from enum IncrementTypeEnum
	kInferredLine                 =24834      # from enum InferredTypeEnum
	kInferredPoint                =24835      # from enum InferredTypeEnum
	kNoInference                  =24833      # from enum InferredTypeEnum
	kAngularEndsInspectionBorder  =79362      # from enum InspectionDimensionShapeEnum
	kNoInspectionBorder           =79361      # from enum InspectionDimensionShapeEnum
	kRoundedEndsInspectionBorder  =79363      # from enum InspectionDimensionShapeEnum
	kGeometryIntent               =58116      # from enum IntentTypeEnum
	kNoPointIntent                =58117      # from enum IntentTypeEnum
	kParameterIntent              =58115      # from enum IntentTypeEnum
	kPoint2dIntent                =58114      # from enum IntentTypeEnum
	kPointEnumIntent              =58113      # from enum IntentTypeEnum
	kPointIntent                  =58118      # from enum IntentTypeEnum
	kKeyboardInteraction          =4          # from enum InteractionEventsEnum
	kMouseAndKeyboardInteraction  =6          # from enum InteractionEventsEnum
	kMouseInteraction             =2          # from enum InteractionEventsEnum
	kNoInteraction                =0          # from enum InteractionEventsEnum
	kSelectAndKeyboardInteraction =5          # from enum InteractionEventsEnum
	kSelectInteraction            =1          # from enum InteractionEventsEnum
	kAllComponentsInteractiveContact=64770      # from enum InteractiveContactAnalysisEnum
	kContactSetOnlyInteractiveContact=64769      # from enum InteractiveContactAnalysisEnum
	kSolverOffInteractiveContact  =64771      # from enum InteractiveContactAnalysisEnum
	kAllSurfacesInteractiveContact=65025      # from enum InteractiveContactSurfacesEnum
	kGeneralSurfacesInteractiveContact=65026      # from enum InteractiveContactSurfacesEnum
	kSimpleSurfacesInteractiveContact=65027      # from enum InteractiveContactSurfacesEnum
	kClassicInterface             =87810      # from enum InterfaceStyleEnum
	kRibbonInterface              =87809      # from enum InterfaceStyleEnum
	kAngularInBothDirections      =4          # from enum LayDirectionTypeEnum
	kCircularRelativeToCenter     =16         # from enum LayDirectionTypeEnum
	kMultidirectional             =8          # from enum LayDirectionTypeEnum
	kParallelToPlaneOfProjection  =1          # from enum LayDirectionTypeEnum
	kParticulateNondirectional    =64         # from enum LayDirectionTypeEnum
	kPerpendicularToPlaneOfProjection=2          # from enum LayDirectionTypeEnum
	kRadialRelativeToCenter       =32         # from enum LayDirectionTypeEnum
	kAllComponentsSuppressedLevelOfDetail=56066      # from enum LevelOfDetailEnum
	kAllContentSuppressedLevelOfDetail=56068      # from enum LevelOfDetailEnum
	kAllPartsSuppressedLevelOfDetail=56067      # from enum LevelOfDetailEnum
	kCustomLevelOfDetail          =56072      # from enum LevelOfDetailEnum
	kLastActiveLevelOfDetail      =56073      # from enum LevelOfDetailEnum
	kMasterLevelOfDetail          =56065      # from enum LevelOfDetailEnum
	kSandboxLevelOfDetail         =56069      # from enum LevelOfDetailEnum
	kSubstituteLevelOfDetail      =56071      # from enum LevelOfDetailEnum
	kTransientLevelOfDetail       =56070      # from enum LevelOfDetailEnum
	kDirectionalLight             =53249      # from enum LightDefinitionTypeEnum
	kPointLight                   =53250      # from enum LightDefinitionTypeEnum
	kSpotLight                    =53251      # from enum LightDefinitionTypeEnum
	kGroundPlaneSpaceLight        =52995      # from enum LightTypeEnum
	kModelSpaceLight              =52993      # from enum LightTypeEnum
	kViewSpaceLight               =52994      # from enum LightTypeEnum
	kHybridSpace                  =49923      # from enum LineDefinitionSpaceEnum
	kModelSpace                   =49922      # from enum LineDefinitionSpaceEnum
	kScreenSpace                  =49921      # from enum LineDefinitionSpaceEnum
	kDoubleLineSpacing            =45826      # from enum LineSpacingEnum
	kSingleLineSpacing            =45825      # from enum LineSpacingEnum
	kTripleLineSpacing            =45827      # from enum LineSpacingEnum
	kChainLineType                =37644      # from enum LineTypeEnum
	kContinuousLineType           =37633      # from enum LineTypeEnum
	kCustomLineType               =37649      # from enum LineTypeEnum
	kDashDottedLineType           =37638      # from enum LineTypeEnum
	kDashedDoubleDottedLineType   =37645      # from enum LineTypeEnum
	kDashedHiddenLineType         =37641      # from enum LineTypeEnum
	kDashedLineType               =37634      # from enum LineTypeEnum
	kDashedTripleDottedLineType   =37647      # from enum LineTypeEnum
	kDefaultLineType              =37648      # from enum LineTypeEnum
	kDottedLineType               =37636      # from enum LineTypeEnum
	kDoubleDashDoubleDottedLineType=37639      # from enum LineTypeEnum
	kDoubleDashedChainLineType    =37637      # from enum LineTypeEnum
	kDoubleDashedDottedLineType   =37646      # from enum LineTypeEnum
	kDoubleDashedTripleDottedLineType=37640      # from enum LineTypeEnum
	kLongDashDottedLineType       =37642      # from enum LineTypeEnum
	kLongDashTripleDottedLineType =37643      # from enum LineTypeEnum
	kLongDashedDoubleDottedLineType=37635      # from enum LineTypeEnum
	kRangeLineWeight              =66050      # from enum LineWeightTypeEnum
	kTrueLineWeight               =66049      # from enum LineWeightTypeEnum
	kDiametricLinearDimension     =66306      # from enum LinearDimensionTypeEnum
	kRegularLinearDimension       =66305      # from enum LinearDimensionTypeEnum
	kSymmetricLinearDimension     =66307      # from enum LinearDimensionTypeEnum
	kEightDecimalPlacesLinearPrecision=41737      # from enum LinearPrecisionEnum
	kEighthsFractionalLinearPrecision=41741      # from enum LinearPrecisionEnum
	kFiveDecimalPlacesLinearPrecision=41734      # from enum LinearPrecisionEnum
	kFourDecimalPlacesLinearPrecision=41733      # from enum LinearPrecisionEnum
	kHalfFractionalLinearPrecision=41739      # from enum LinearPrecisionEnum
	kOneDecimalPlaceLinearPrecision=41730      # from enum LinearPrecisionEnum
	kOneTwentyEighthsFractionalLinearPrecision=41745      # from enum LinearPrecisionEnum
	kQuarterFractionalLinearPrecision=41740      # from enum LinearPrecisionEnum
	kSevenDecimalPlacesLinearPrecision=41736      # from enum LinearPrecisionEnum
	kSixDecimalPlacesLinearPrecision=41735      # from enum LinearPrecisionEnum
	kSixteenthsFractionalLinearPrecision=41742      # from enum LinearPrecisionEnum
	kSixtyFourthsFractionalLinearPrecision=41744      # from enum LinearPrecisionEnum
	kThirtySecondsFractionalLinearPrecision=41743      # from enum LinearPrecisionEnum
	kThreeDecimalPlacesLinearPrecision=41732      # from enum LinearPrecisionEnum
	kTwoDecimalPlacesLinearPrecision=41731      # from enum LinearPrecisionEnum
	kZeroDecimalPlaceLinearPrecision=41729      # from enum LinearPrecisionEnum
	kZeroFractionalLinearPrecision=41738      # from enum LinearPrecisionEnum
	kAmbiguousStatus              =16         # from enum LinkStatusEnum
	kMissingStatus                =1          # from enum LinkStatusEnum
	kOutOfDateStatus              =4          # from enum LinkStatusEnum
	kSourceNewerStatus            =8          # from enum LinkStatusEnum
	kUpToDateStatus               =2          # from enum LinkStatusEnum
	kLibraryLocation              =45060      # from enum LocationTypeEnum
	kLocalLocation                =45058      # from enum LocationTypeEnum
	kOwnerDirectoryLocation       =45062      # from enum LocationTypeEnum
	kUnknownLocation              =45061      # from enum LocationTypeEnum
	kWorkgroupLocation            =45059      # from enum LocationTypeEnum
	kWorkspaceLocation            =45057      # from enum LocationTypeEnum
	kAngleLoftCondition           =34307      # from enum LoftConditionEnum
	kDirectionLoftCondition       =34307      # from enum LoftConditionEnum
	kFreeLoftCondition            =34305      # from enum LoftConditionEnum
	kSharpPointLoftCondition      =34309      # from enum LoftConditionEnum
	kSmoothLoftCondition          =34308      # from enum LoftConditionEnum
	kTangentLoftCondition         =34306      # from enum LoftConditionEnum
	kTangentToPlaneLoftCondition  =34310      # from enum LoftConditionEnum
	kLoftWithAreaGraphSections    =60932      # from enum LoftTypeEnum
	kLoftWithCenterline           =60931      # from enum LoftTypeEnum
	kLoftWithRails                =60930      # from enum LoftTypeEnum
	kRegularLoft                  =60929      # from enum LoftTypeEnum
	kDieFormedLoftedFlange        =91137      # from enum LoftedFlangeOutputTypeEnum
	kPressBrakeChordToleranceLoftedFlange=91138      # from enum LoftedFlangeOutputTypeEnum
	kPressBrakeFacetAngleLoftedFlange=91139      # from enum LoftedFlangeOutputTypeEnum
	kPressBrakeFacetDistanceLoftedFlange=91140      # from enum LoftedFlangeOutputTypeEnum
	k_High                        =24579      # from enum MassPropertiesAccuracyEnum
	k_Low                         =24577      # from enum MassPropertiesAccuracyEnum
	k_Medium                      =24578      # from enum MassPropertiesAccuracyEnum
	k_None                        =24581      # from enum MassPropertiesAccuracyEnum
	k_VeryHigh                    =24580      # from enum MassPropertiesAccuracyEnum
	kMaterialDisplayUnitsEnglishFoot=98824      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsEnglishInch=98823      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsEnglishStandard=98822      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricCGS=98820      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricMKS=98818      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricMMNS=98819      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricStandard=98817      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricUMNS=98821      # from enum MaterialDisplayUnitsEnum
	kBetweenModifier              =128        # from enum MaterialRemovalModifierEnum
	kContinuousFeatureModifier    =8192       # from enum MaterialRemovalModifierEnum
	kDiameterModifier             =256        # from enum MaterialRemovalModifierEnum
	kEnvelopeRequirementModifier  =512        # from enum MaterialRemovalModifierEnum
	kFreeStateModifier            =16         # from enum MaterialRemovalModifierEnum
	kFromToModifier               =32768      # from enum MaterialRemovalModifierEnum
	kLeastMaterialConditionModifier=2          # from enum MaterialRemovalModifierEnum
	kMaximumMaterialConditionModifier=1          # from enum MaterialRemovalModifierEnum
	kMedianFeatureModifier        =16384      # from enum MaterialRemovalModifierEnum
	kProjectedToleranceZoneModifier=4          # from enum MaterialRemovalModifierEnum
	kReciprocityModifier          =1024       # from enum MaterialRemovalModifierEnum
	kRegardlessOfFeatureSizeModifier=32         # from enum MaterialRemovalModifierEnum
	kSquareModifier               =2048       # from enum MaterialRemovalModifierEnum
	kStatisticalToleranceModifier =64         # from enum MaterialRemovalModifierEnum
	kTangentPlaneModifier         =8          # from enum MaterialRemovalModifierEnum
	kUnequallyDisposedModifier    =4096       # from enum MaterialRemovalModifierEnum
	kAngleMeasure                 =72706      # from enum MeasureTypeEnum
	kDistanceMeasure              =72705      # from enum MeasureTypeEnum
	kDataObjectMedium             =56578      # from enum MediumTypeEnum
	kFileNameMedium               =56577      # from enum MediumTypeEnum
	kStreamMedium                 =56579      # from enum MediumTypeEnum
	kStringMedium                 =56580      # from enum MediumTypeEnum
	kEditActiveMember             =57601      # from enum MemberEditScopeEnum
	kEditAllMembers               =57602      # from enum MemberEditScopeEnum
	kMemberManagerDifferentFamily =50410517   # from enum MemberManagerErrorsEnum
	kMemberManagerDifferentMember =50410518   # from enum MemberManagerErrorsEnum
	kMemberManagerFeatureSuppressFail=50410521   # from enum MemberManagerErrorsEnum
	kMemberManagerInvalidMemberValue=50410524   # from enum MemberManagerErrorsEnum
	kMemberManagerLongFilename    =50410520   # from enum MemberManagerErrorsEnum
	kMemberManagerMaterialNotFound=50410519   # from enum MemberManagerErrorsEnum
	kMemberManagerMissingFileWritePermission=50410516   # from enum MemberManagerErrorsEnum
	kMemberManagerNoError         =50410511   # from enum MemberManagerErrorsEnum
	kMemberManagerThreadCreateFail=50410523   # from enum MemberManagerErrorsEnum
	kMemberManagerThreadFeatureNotFound=50410522   # from enum MemberManagerErrorsEnum
	kMemberManagerUnknown         =50410512   # from enum MemberManagerErrorsEnum
	kMemberManagerVaultCheckoutFail=50410514   # from enum MemberManagerErrorsEnum
	kMemberManagerVaultFileStatusFail=50410513   # from enum MemberManagerErrorsEnum
	kMemberManagerVaultGetLatestVersionFail=50410515   # from enum MemberManagerErrorsEnum
	kEventMember                  =30721      # from enum MemberTypeEnum
	kFunctionMember               =30723      # from enum MemberTypeEnum
	kPropertyMember               =30724      # from enum MemberTypeEnum
	kSubMember                    =30722      # from enum MemberTypeEnum
	kAlwaysSaveMemoryMode         =65282      # from enum MemorySavingModeEnum
	kNeverSaveMemoryMode          =65283      # from enum MemorySavingModeEnum
	kUseApplicationOptionsMemoryMode=65281      # from enum MemorySavingModeEnum
	kButton                       =95233      # from enum MiniToolbarControlTypeEnum
	kCheckBox                     =95234      # from enum MiniToolbarControlTypeEnum
	kComboBox                     =95235      # from enum MiniToolbarControlTypeEnum
	kDropdown                     =95236      # from enum MiniToolbarControlTypeEnum
	kLabel                        =95237      # from enum MiniToolbarControlTypeEnum
	kSeparator                    =95239      # from enum MiniToolbarControlTypeEnum
	kSlider                       =95241      # from enum MiniToolbarControlTypeEnum
	kTextEditor                   =95242      # from enum MiniToolbarControlTypeEnum
	kValueEditor                  =95240      # from enum MiniToolbarControlTypeEnum
	kThreadMajorDiameter          =21761      # from enum ModelDiameterFromThreadEnum
	kThreadMinorDiameter          =21762      # from enum ModelDiameterFromThreadEnum
	kThreadPitchDiameter          =21763      # from enum ModelDiameterFromThreadEnum
	kThreadTapDrillDiameter       =21764      # from enum ModelDiameterFromThreadEnum
	kLowerValue                   =31490      # from enum ModelValueTypeEnum
	kMedianValue                  =31492      # from enum ModelValueTypeEnum
	kNominalValue                 =31489      # from enum ModelValueTypeEnum
	kUpperValue                   =31491      # from enum ModelValueTypeEnum
	kLeftMouseButton              =1          # from enum MouseButtonEnum
	kMiddleMouseButton            =4          # from enum MouseButtonEnum
	kNoneMouseButton              =0          # from enum MouseButtonEnum
	kRightMouseButton             =2          # from enum MouseButtonEnum
	kDragEnter                    =15617      # from enum MouseDragStateEnum
	kDragLeave                    =15618      # from enum MouseDragStateEnum
	kDragOver                     =15619      # from enum MouseDragStateEnum
	kDragUnknown                  =15620      # from enum MouseDragStateEnum
	kDirectionAndDistanceMoveType =91393      # from enum MoveFaceTypeEnum
	kFreeMoveType                 =91395      # from enum MoveFaceTypeEnum
	kPlanarMoveType               =91394      # from enum MoveFaceTypeEnum
	kAllAboveLandingLine          =101634     # from enum MultiLineDimensionTextEnum
	kAllAboveLandingLineWithUnderline=101635     # from enum MultiLineDimensionTextEnum
	kFirstLineAboveLandingLine    =101636     # from enum MultiLineDimensionTextEnum
	kFirstLineCenteredOnLandingLine=101633     # from enum MultiLineDimensionTextEnum
	kJISAlignment                 =101637     # from enum MultiLineDimensionTextEnum
	kSemiIsolatedMode             =36355      # from enum MultiUserModeEnum
	kSemiIsolatedNoCheckoutMode   =36356      # from enum MultiUserModeEnum
	kSharedMode                   =36354      # from enum MultiUserModeEnum
	kSingleUserMode               =36353      # from enum MultiUserModeEnum
	kVaultMode                    =36357      # from enum MultiUserModeEnum
	kHomePageContentType          =107521     # from enum MyHomeContentTypeEnum
	kTeamWebContentType           =107522     # from enum MyHomeContentTypeEnum
	kOverallNormal                =19716      # from enum NormalBindingEnum
	kPerItemNormals               =19715      # from enum NormalBindingEnum
	kPerStripNormals              =19714      # from enum NormalBindingEnum
	kPerVertexNormals             =19713      # from enum NormalBindingEnum
	kLowercaseAlphaNumbering      =61186      # from enum NumberingSchemeEnum
	kNumericNumbering             =61185      # from enum NumberingSchemeEnum
	kUppercaseAlphaNumbering      =61187      # from enum NumberingSchemeEnum
	kCircularConicalFaceOGSGeometryType=100105     # from enum OGSGeometryTypeEnum
	kCircularCylindricalFaceOGSGeometryType=100103     # from enum OGSGeometryTypeEnum
	kCircularEdgeOGSGeometryType  =100099     # from enum OGSGeometryTypeEnum
	kEllipticCylindricalFaceOGSGeometryType=100104     # from enum OGSGeometryTypeEnum
	kEllipticalConicalFaceOGSGeometryType=100106     # from enum OGSGeometryTypeEnum
	kEllipticalEdgeOGSGeometryType=100100     # from enum OGSGeometryTypeEnum
	kLinearEdgeOGSGeometryType    =100098     # from enum OGSGeometryTypeEnum
	kPlanarFaceOGSGeometryType    =100102     # from enum OGSGeometryTypeEnum
	kSphericalFaceOGSGeometryType =100107     # from enum OGSGeometryTypeEnum
	kSplineEdgeOGSGeometryType    =100101     # from enum OGSGeometryTypeEnum
	kSplineFaceOGSGeometryType    =100108     # from enum OGSGeometryTypeEnum
	kToroidalFaceOGSGeometryType  =100109     # from enum OGSGeometryTypeEnum
	kUnknownOGSGeometryType       =100097     # from enum OGSGeometryTypeEnum
	kLineListOGSPrimitiveType     =99843      # from enum OGSPrimitiveTypeEnum
	kLineStripOGSPrimitiveType    =99844      # from enum OGSPrimitiveTypeEnum
	kNoneOGSPrimitiveType         =99841      # from enum OGSPrimitiveTypeEnum
	kPointListOGSPrimitiveType    =99842      # from enum OGSPrimitiveTypeEnum
	kTriangleListOGSPrimitiveType =99845      # from enum OGSPrimitiveTypeEnum
	kTriangleStripOGSPrimitiveType=99846      # from enum OGSPrimitiveTypeEnum
	kBodyOGSSceneNodeType         =100355     # from enum OGSSceneNodeTypeEnum
	kComponentOGSSceneNodeType    =100354     # from enum OGSSceneNodeTypeEnum
	kUnknownOGSSceneNodeType      =100353     # from enum OGSSceneNodeTypeEnum
	kOLEDocumentEmbeddingObject   =3330       # from enum OLEDocumentTypeEnum
	kOLEDocumentLinkObject        =3331       # from enum OLEDocumentTypeEnum
	kOLEDocumentUnknownObject     =3329       # from enum OLEDocumentTypeEnum
	kDefaultOLEVerb               =3076       # from enum OLEVerbEnum
	kEditOpenOLEVerb              =3073       # from enum OLEVerbEnum
	kHideOLEVerb                  =3075       # from enum OLEVerbEnum
	kShowOLEVerb                  =3074       # from enum OLEVerbEnum
	k3dAViewObject                =83956224   # from enum ObjectTypeEnum
	kASideDefinition              =151025152  # from enum ObjectTypeEnum
	kASideDefinitions             =151024896  # from enum ObjectTypeEnum
	kAliasFreeformFeatureObject   =84011264   # from enum ObjectTypeEnum
	kAliasFreeformFeatureProxyObject=84011008   # from enum ObjectTypeEnum
	kAliasFreeformFeaturesObject  =84011520   # from enum ObjectTypeEnum
	kAnalysisManagerObject        =50417152   # from enum ObjectTypeEnum
	kAnalyticEdgeWorkAxisDefObject=83979520   # from enum ObjectTypeEnum
	kAngleConstraintObject        =100665088  # from enum ObjectTypeEnum
	kAngleConstraintProxyObject   =100675584  # from enum ObjectTypeEnum
	kAngleExtentObject            =83918080   # from enum ObjectTypeEnum
	kAngleiMateDefinitionObject   =83947008   # from enum ObjectTypeEnum
	kAngleiMateDefinitionProxyObject=83947136   # from enum ObjectTypeEnum
	kAngularGeneralDimensionObject=117474816  # from enum ObjectTypeEnum
	kAngularModelDimensionDefinitionObject=84025600   # from enum ObjectTypeEnum
	kAngularModelDimensionObject  =84022784   # from enum ObjectTypeEnum
	kAngularModelDimensionsObject =84022016   # from enum ObjectTypeEnum
	kAnnotationPlaneDefinitionObject=84029696   # from enum ObjectTypeEnum
	kAnnotationPlaneDefinitionsEnumeratorObject=84029952   # from enum ObjectTypeEnum
	kAnnotationPlaneObject        =84027904   # from enum ObjectTypeEnum
	kAnnotationPlanesObject       =84027648   # from enum ObjectTypeEnum
	kApplicationAddInObject       =50336000   # from enum ObjectTypeEnum
	kApplicationAddInSiteObject   =50336768   # from enum ObjectTypeEnum
	kApplicationAddInsObject      =50335744   # from enum ObjectTypeEnum
	kApplicationEventsObject      =50333184   # from enum ObjectTypeEnum
	kApplicationObject            =50331904   # from enum ObjectTypeEnum
	kApprenticeDrawingPrintManagerObject=50391040   # from enum ObjectTypeEnum
	kApprenticePrintManagerObject =50390784   # from enum ObjectTypeEnum
	kApprenticeServerDocumentObject=50340736   # from enum ObjectTypeEnum
	kApprenticeServerDocumentsObject=50340864   # from enum ObjectTypeEnum
	kApprenticeServerDrawingDocumentObject=117441024  # from enum ObjectTypeEnum
	kApprenticeServerObject       =50341120   # from enum ObjectTypeEnum
	kArcLengthDimConstraintObject =84014336   # from enum ObjectTypeEnum
	kArcLengthDimConstraintProxyObject=84014448   # from enum ObjectTypeEnum
	kAssemblyComponentDefinitionObject=100663808  # from enum ObjectTypeEnum
	kAssemblyComponentDefinitionsObject=100664576  # from enum ObjectTypeEnum
	kAssemblyConstraintsEnumeratorObject=100664832  # from enum ObjectTypeEnum
	kAssemblyConstraintsObject    =100664320  # from enum ObjectTypeEnum
	kAssemblyEventsObject         =100667392  # from enum ObjectTypeEnum
	kAssemblyJointDefinitionObject=100706304  # from enum ObjectTypeEnum
	kAssemblyJointObject          =100706560  # from enum ObjectTypeEnum
	kAssemblyJointProxyObject     =100707072  # from enum ObjectTypeEnum
	kAssemblyJointsEnumeratorObject=100707584  # from enum ObjectTypeEnum
	kAssemblyJointsObject         =100706048  # from enum ObjectTypeEnum
	kAssemblyOptionsObject        =50386176   # from enum ObjectTypeEnum
	kAssemblySolverNodeObject     =100671488  # from enum ObjectTypeEnum
	kAssemblySolverObject         =100671232  # from enum ObjectTypeEnum
	kAssemblySymmetryConstraintObject=100707840  # from enum ObjectTypeEnum
	kAssemblySymmetryConstraintProxyObject=100708096  # from enum ObjectTypeEnum
	kAssemblyWorkAxisDefObject    =100670720  # from enum ObjectTypeEnum
	kAssemblyWorkPlaneDefObject   =100670464  # from enum ObjectTypeEnum
	kAssemblyWorkPointDefObject   =100670976  # from enum ObjectTypeEnum
	kAssetCategoriesObject        =50449152   # from enum ObjectTypeEnum
	kAssetCategoryObject          =50449408   # from enum ObjectTypeEnum
	kAssetLibrariesObject         =50447616   # from enum ObjectTypeEnum
	kAssetLibraryObject           =50447872   # from enum ObjectTypeEnum
	kAssetObject                  =50448640   # from enum ObjectTypeEnum
	kAssetTextureObject           =50452480   # from enum ObjectTypeEnum
	kAssetValueObject             =50449664   # from enum ObjectTypeEnum
	kAssetsEnumeratorObject       =50448384   # from enum ObjectTypeEnum
	kAssetsObject                 =50448128   # from enum ObjectTypeEnum
	kAttributeManagerObject       =50351872   # from enum ObjectTypeEnum
	kAttributeObject              =50352640   # from enum ObjectTypeEnum
	kAttributeSetObject           =50352384   # from enum ObjectTypeEnum
	kAttributeSetsEnumeratorObject=50361344   # from enum ObjectTypeEnum
	kAttributeSetsObject          =50352128   # from enum ObjectTypeEnum
	kAttributesEnumeratorObject   =50361600   # from enum ObjectTypeEnum
	kAutoCADBlockDefinitionObject =117495296  # from enum ObjectTypeEnum
	kAutoCADBlockDefinitionsEnumeratorObject=117496064  # from enum ObjectTypeEnum
	kAutoCADBlockDefinitionsObject=117495040  # from enum ObjectTypeEnum
	kAutoCADBlockObject           =117495808  # from enum ObjectTypeEnum
	kAutoCADBlocksObject          =117495552  # from enum ObjectTypeEnum
	kAutomatedCenterlineSettingsObject=117489920  # from enum ObjectTypeEnum
	kBIMCableTrayConnectorDefinitionObject=50440448   # from enum ObjectTypeEnum
	kBIMComponentDescriptionObject=50437376   # from enum ObjectTypeEnum
	kBIMComponentObject           =50436864   # from enum ObjectTypeEnum
	kBIMComponentPropertyObject   =50438656   # from enum ObjectTypeEnum
	kBIMComponentPropertySetObject=50438400   # from enum ObjectTypeEnum
	kBIMComponentPropertySetsObject=50438144   # from enum ObjectTypeEnum
	kBIMConduitConnectorDefinitionObject=50440192   # from enum ObjectTypeEnum
	kBIMConnectorDefinitionObject =50439168   # from enum ObjectTypeEnum
	kBIMConnectorLinkObject       =50438032   # from enum ObjectTypeEnum
	kBIMConnectorLinksObject      =50437888   # from enum ObjectTypeEnum
	kBIMConnectorObject           =50438912   # from enum ObjectTypeEnum
	kBIMConnectorsObject          =50437632   # from enum ObjectTypeEnum
	kBIMDuctConnectorDefinitionObject=50439936   # from enum ObjectTypeEnum
	kBIMElectricalConnectorDefinitionObject=50439680   # from enum ObjectTypeEnum
	kBIMExchangeServerObject      =50437120   # from enum ObjectTypeEnum
	kBIMPipeConnectorDefinitionObject=50439424   # from enum ObjectTypeEnum
	kBOMObject                    =100673792  # from enum ObjectTypeEnum
	kBOMQuantityObject            =67131136   # from enum ObjectTypeEnum
	kBOMRowObject                 =100674816  # from enum ObjectTypeEnum
	kBOMRowsEnumeratorObject      =100681984  # from enum ObjectTypeEnum
	kBOMViewObject                =100674304  # from enum ObjectTypeEnum
	kBOMViewsObject               =100674048  # from enum ObjectTypeEnum
	kBSplineCurve2dDefinitionObject=67130880   # from enum ObjectTypeEnum
	kBSplineCurveDefinitionObject =67130624   # from enum ObjectTypeEnum
	kBalloonObject                =117463040  # from enum ObjectTypeEnum
	kBalloonStyleObject           =117480960  # from enum ObjectTypeEnum
	kBalloonStylesEnumeratorObject=117480704  # from enum ObjectTypeEnum
	kBalloonTipObject             =50441728   # from enum ObjectTypeEnum
	kBalloonTipsObject            =50441472   # from enum ObjectTypeEnum
	kBalloonValueSetObject        =117463808  # from enum ObjectTypeEnum
	kBalloonValueSetsObject       =117463552  # from enum ObjectTypeEnum
	kBalloonsObject               =117462784  # from enum ObjectTypeEnum
	kBaselineDimensionSetObject   =117488896  # from enum ObjectTypeEnum
	kBaselineDimensionSetsObject  =117488640  # from enum ObjectTypeEnum
	kBendConstraintObject         =83941888   # from enum ObjectTypeEnum
	kBendConstraintProxyObject    =83942000   # from enum ObjectTypeEnum
	kBendDefinitionObject         =151006976  # from enum ObjectTypeEnum
	kBendFeatureObject            =150997504  # from enum ObjectTypeEnum
	kBendFeatureProxyObject       =151003136  # from enum ObjectTypeEnum
	kBendFeaturesObject           =150997248  # from enum ObjectTypeEnum
	kBendNoteObject               =117487616  # from enum ObjectTypeEnum
	kBendNotesObject              =117490944  # from enum ObjectTypeEnum
	kBendObject                   =151019520  # from enum ObjectTypeEnum
	kBendOptionsObject            =151009792  # from enum ObjectTypeEnum
	kBendPartFeatureObject        =83991552   # from enum ObjectTypeEnum
	kBendPartFeatureProxyObject   =83991680   # from enum ObjectTypeEnum
	kBendPartFeaturesObject       =83991808   # from enum ObjectTypeEnum
	kBendsEnumeratorObject        =151019776  # from enum ObjectTypeEnum
	kBooleanAssetValueObject      =50450944   # from enum ObjectTypeEnum
	kBorderDefinitionObject       =117446400  # from enum ObjectTypeEnum
	kBorderDefinitionsObject      =117446144  # from enum ObjectTypeEnum
	kBorderObject                 =117446656  # from enum ObjectTypeEnum
	kBossFeatureObject            =84002304   # from enum ObjectTypeEnum
	kBossFeatureProxyObject       =84002416   # from enum ObjectTypeEnum
	kBossFeaturesObject           =84002560   # from enum ObjectTypeEnum
	kBossSetObject                =84013824   # from enum ObjectTypeEnum
	kBossSetsObject               =84013568   # from enum ObjectTypeEnum
	kBoundaryPatchDefinitionObject=83989760   # from enum ObjectTypeEnum
	kBoundaryPatchFeatureObject   =83964672   # from enum ObjectTypeEnum
	kBoundaryPatchFeatureProxyObject=83965184   # from enum ObjectTypeEnum
	kBoundaryPatchFeaturesObject  =83964928   # from enum ObjectTypeEnum
	kBoundaryPatchLoopObject      =83990016   # from enum ObjectTypeEnum
	kBoundaryPatchLoopsObject     =83992832   # from enum ObjectTypeEnum
	kBreakOperationObject         =117492224  # from enum ObjectTypeEnum
	kBreakOperationsObject        =117491968  # from enum ObjectTypeEnum
	kBreakOutOperationObject      =117492736  # from enum ObjectTypeEnum
	kBreakOutOperationsObject     =117492480  # from enum ObjectTypeEnum
	kBrowserFolderObject          =50427392   # from enum ObjectTypeEnum
	kBrowserFoldersEnumeratorObject=50426880   # from enum ObjectTypeEnum
	kBrowserNodeDefinitionObject  =50384896   # from enum ObjectTypeEnum
	kBrowserNodeObject            =50384384   # from enum ObjectTypeEnum
	kBrowserNodesEnumeratorObject =50384128   # from enum ObjectTypeEnum
	kBrowserPaneObject            =50363136   # from enum ObjectTypeEnum
	kBrowserPanesObject           =50362880   # from enum ObjectTypeEnum
	kButtonDefinitionHandlerObject=50374144   # from enum ObjectTypeEnum
	kButtonDefinitionObject       =50371584   # from enum ObjectTypeEnum
	kCallOutSymbolObject          =117473280  # from enum ObjectTypeEnum
	kCameraEventsObject           =50435328   # from enum ObjectTypeEnum
	kCameraObject                 =50345472   # from enum ObjectTypeEnum
	kCategoryManagerObject        =50409984   # from enum ObjectTypeEnum
	kCellObject                   =117462528  # from enum ObjectTypeEnum
	kCenteredWidthExtentObject    =83996672   # from enum ObjectTypeEnum
	kCenterlineObject             =117479680  # from enum ObjectTypeEnum
	kCenterlinesObject            =117479424  # from enum ObjectTypeEnum
	kCentermarkObject             =117479168  # from enum ObjectTypeEnum
	kCentermarkStyleObject        =117490432  # from enum ObjectTypeEnum
	kCentermarkStylesEnumeratorObject=117490176  # from enum ObjectTypeEnum
	kCentermarksObject            =117478912  # from enum ObjectTypeEnum
	kCentroidWorkPointDefObject   =83993088   # from enum ObjectTypeEnum
	kChainDimensionSetObject      =117493248  # from enum ObjectTypeEnum
	kChainDimensionSetsObject     =117492992  # from enum ObjectTypeEnum
	kChamferFeatureObject         =83909120   # from enum ObjectTypeEnum
	kChamferFeatureProxyObject    =83956480   # from enum ObjectTypeEnum
	kChamferFeaturesObject        =83909376   # from enum ObjectTypeEnum
	kChamferNoteObject            =117488384  # from enum ObjectTypeEnum
	kChamferNotesObject           =117490688  # from enum ObjectTypeEnum
	kChangeDefinitionObject       =50389248   # from enum ObjectTypeEnum
	kChangeDefinitionsObject      =50388992   # from enum ObjectTypeEnum
	kChangeManagerObject          =50388736   # from enum ObjectTypeEnum
	kChangeProcessorObject        =50389504   # from enum ObjectTypeEnum
	kCheckPointObject             =50354432   # from enum ObjectTypeEnum
	kCheckPointsEnumeratorObject  =50354688   # from enum ObjectTypeEnum
	kChoiceAssetValueObject       =50449920   # from enum ObjectTypeEnum
	kCircularOccurrencePatternObject=100669696  # from enum ObjectTypeEnum
	kCircularOccurrencePatternProxyObject=100669824  # from enum ObjectTypeEnum
	kCircularPatternFeatureObject =83909632   # from enum ObjectTypeEnum
	kCircularPatternFeatureProxyObject=83956736   # from enum ObjectTypeEnum
	kCircularPatternFeaturesObject=83909888   # from enum ObjectTypeEnum
	kClientBrowserNodeDefinitionObject=50385152   # from enum ObjectTypeEnum
	kClientFeatureDefinitionObject=83988992   # from enum ObjectTypeEnum
	kClientFeatureElementObject   =83989504   # from enum ObjectTypeEnum
	kClientFeatureElementProxyObject=83989616   # from enum ObjectTypeEnum
	kClientFeatureElementsObject  =83989248   # from enum ObjectTypeEnum
	kClientFeatureObject          =83988736   # from enum ObjectTypeEnum
	kClientFeatureProxyObject     =83988848   # from enum ObjectTypeEnum
	kClientFeaturesObject         =83988480   # from enum ObjectTypeEnum
	kClientGraphicsCollectionObject=50356224   # from enum ObjectTypeEnum
	kClientGraphicsObject         =50356480   # from enum ObjectTypeEnum
	kClientNodeResourceObject     =50385664   # from enum ObjectTypeEnum
	kClientNodeResourcesObject    =50385920   # from enum ObjectTypeEnum
	kClientViewObject             =50368256   # from enum ObjectTypeEnum
	kClientViewsObject            =50368000   # from enum ObjectTypeEnum
	kCoilFeatureObject            =83910144   # from enum ObjectTypeEnum
	kCoilFeatureProxyObject       =83956992   # from enum ObjectTypeEnum
	kCoilFeaturesObject           =83910400   # from enum ObjectTypeEnum
	kCoincidentConstraint3DObject =83942144   # from enum ObjectTypeEnum
	kCoincidentConstraint3DProxyObject=83942256   # from enum ObjectTypeEnum
	kCoincidentConstraintObject   =83900160   # from enum ObjectTypeEnum
	kCoincidentConstraintProxyObject=83900272   # from enum ObjectTypeEnum
	kCollinearConstraint3DObject  =83966208   # from enum ObjectTypeEnum
	kCollinearConstraint3DProxyObject=83966320   # from enum ObjectTypeEnum
	kCollinearConstraintObject    =83900416   # from enum ObjectTypeEnum
	kCollinearConstraintProxyObject=83900528   # from enum ObjectTypeEnum
	kColorAssetValueObject        =50451200   # from enum ObjectTypeEnum
	kColorObject                  =50383104   # from enum ObjectTypeEnum
	kColorSchemeObject            =50399232   # from enum ObjectTypeEnum
	kColorSchemesObject           =50398976   # from enum ObjectTypeEnum
	kColumnObject                 =117461760  # from enum ObjectTypeEnum
	kColumnsObject                =117461504  # from enum ObjectTypeEnum
	kCombineFeatureObject         =84001536   # from enum ObjectTypeEnum
	kCombineFeatureProxyObject    =84001696   # from enum ObjectTypeEnum
	kCombineFeaturesObject        =84001280   # from enum ObjectTypeEnum
	kComboBoxDefinitionObject     =50372096   # from enum ObjectTypeEnum
	kCommandBarBaseCollectionObject=50375424   # from enum ObjectTypeEnum
	kCommandBarBaseObject         =50375680   # from enum ObjectTypeEnum
	kCommandBarButtonObject       =50365952   # from enum ObjectTypeEnum
	kCommandBarControlObject      =50365440   # from enum ObjectTypeEnum
	kCommandBarControlsObject     =50365184   # from enum ObjectTypeEnum
	kCommandBarListObject         =50376704   # from enum ObjectTypeEnum
	kCommandBarObject             =50364928   # from enum ObjectTypeEnum
	kCommandBarPopUpObject        =50365696   # from enum ObjectTypeEnum
	kCommandBarsObject            =50364672   # from enum ObjectTypeEnum
	kCommandCategoriesObject      =50370816   # from enum ObjectTypeEnum
	kCommandCategoryObject        =50370560   # from enum ObjectTypeEnum
	kCommandControlObject         =50425856   # from enum ObjectTypeEnum
	kCommandControlsEnumeratorObject=50426624   # from enum ObjectTypeEnum
	kCommandControlsObject        =50425600   # from enum ObjectTypeEnum
	kCommandManagerObject         =50344704   # from enum ObjectTypeEnum
	kCommandObject                =50344192   # from enum ObjectTypeEnum
	kComponentDefinitionObject    =67113264   # from enum ObjectTypeEnum
	kComponentDefinitionReferenceObject=67113520   # from enum ObjectTypeEnum
	kComponentDefinitionReferencesObject=67114800   # from enum ObjectTypeEnum
	kComponentDefinitionsEnumeratorObject=67114336   # from enum ObjectTypeEnum
	kComponentDefinitionsObject   =67114288   # from enum ObjectTypeEnum
	kComponentGraphicsObject      =50436608   # from enum ObjectTypeEnum
	kComponentOccurrenceObject    =67113776   # from enum ObjectTypeEnum
	kComponentOccurrenceProxyObject=67113888   # from enum ObjectTypeEnum
	kComponentOccurrencesEnumeratorObject=67126528   # from enum ObjectTypeEnum
	kComponentOccurrencesObject   =67114544   # from enum ObjectTypeEnum
	kCompositeConstraintObject    =100678144  # from enum ObjectTypeEnum
	kCompositeiMateDefinitionObject=83948800   # from enum ObjectTypeEnum
	kCompositeiMateDefinitionProxyObject=83948864   # from enum ObjectTypeEnum
	kConcentricConstraint3DObject =84008960   # from enum ObjectTypeEnum
	kConcentricConstraint3DProxyObject=84009072   # from enum ObjectTypeEnum
	kConcentricConstraintObject   =83900672   # from enum ObjectTypeEnum
	kConcentricConstraintProxyObject=83900784   # from enum ObjectTypeEnum
	kConcentricHolePlacementDefinitionObject=83967232   # from enum ObjectTypeEnum
	kConstraintLimitsObject       =100699904  # from enum ObjectTypeEnum
	kContentCenterConfigurationObject=50400256   # from enum ObjectTypeEnum
	kContentCenterDialogEventsObject=50409472   # from enum ObjectTypeEnum
	kContentCenterDialogObject    =50409216   # from enum ObjectTypeEnum
	kContentCenterEventsObject    =50420224   # from enum ObjectTypeEnum
	kContentCenterObject          =50392320   # from enum ObjectTypeEnum
	kContentCenterOptionsObject   =50421248   # from enum ObjectTypeEnum
	kContentFamiliesEnumeratorObject=50423296   # from enum ObjectTypeEnum
	kContentFamilyObject          =50421760   # from enum ObjectTypeEnum
	kContentQueryObject           =50393088   # from enum ObjectTypeEnum
	kContentTableCellObject       =50421504   # from enum ObjectTypeEnum
	kContentTableColumnObject     =50422528   # from enum ObjectTypeEnum
	kContentTableColumnsObject    =50423040   # from enum ObjectTypeEnum
	kContentTableRowObject        =50422016   # from enum ObjectTypeEnum
	kContentTableRowsObject       =50422272   # from enum ObjectTypeEnum
	kContentTreeViewNodeObject    =50423808   # from enum ObjectTypeEnum
	kContentTreeViewNodesEnumeratorObject=50423552   # from enum ObjectTypeEnum
	kContourFlangeDefinitionObject=151014144  # from enum ObjectTypeEnum
	kContourFlangeFeatureObject   =151001856  # from enum ObjectTypeEnum
	kContourFlangeFeatureProxyObject=151005184  # from enum ObjectTypeEnum
	kContourFlangeFeaturesObject  =151001600  # from enum ObjectTypeEnum
	kContourRollFeatureObject     =151020800  # from enum ObjectTypeEnum
	kContourRollFeatureProxyObject=151021056  # from enum ObjectTypeEnum
	kContourRollFeaturesObject    =151021312  # from enum ObjectTypeEnum
	kControlDefinitionEventsObject=50390016   # from enum ObjectTypeEnum
	kControlDefinitionsObject     =50371328   # from enum ObjectTypeEnum
	kCoreCavityDefinitionObject   =84009728   # from enum ObjectTypeEnum
	kCoreCavityFeatureObject      =84010240   # from enum ObjectTypeEnum
	kCoreCavityFeatureProxyObject =84009984   # from enum ObjectTypeEnum
	kCoreCavityFeaturesObject     =84010496   # from enum ObjectTypeEnum
	kCornerChamferDefinitionObject=151011584  # from enum ObjectTypeEnum
	kCornerChamferFeatureObject   =151000320  # from enum ObjectTypeEnum
	kCornerChamferFeatureProxyObject=151004416  # from enum ObjectTypeEnum
	kCornerChamferFeaturesObject  =151000064  # from enum ObjectTypeEnum
	kCornerDefinitionObject       =151010816  # from enum ObjectTypeEnum
	kCornerFeatureObject          =150996992  # from enum ObjectTypeEnum
	kCornerFeatureProxyObject     =151002880  # from enum ObjectTypeEnum
	kCornerFeaturesObject         =150996736  # from enum ObjectTypeEnum
	kCornerOptionsObject          =151010048  # from enum ObjectTypeEnum
	kCornerRoundDefinitionObject  =151011072  # from enum ObjectTypeEnum
	kCornerRoundEdgeSetObject     =151011328  # from enum ObjectTypeEnum
	kCornerRoundFeatureObject     =150999808  # from enum ObjectTypeEnum
	kCornerRoundFeatureProxyObject=151004160  # from enum ObjectTypeEnum
	kCornerRoundFeaturesObject    =150999552  # from enum ObjectTypeEnum
	kCosmeticBendFeatureObject    =151021824  # from enum ObjectTypeEnum
	kCosmeticBendFeatureProxyObject=151022080  # from enum ObjectTypeEnum
	kCosmeticBendFeaturesObject   =151022336  # from enum ObjectTypeEnum
	kCosmeticWeldObject           =100673024  # from enum ObjectTypeEnum
	kCosmeticWeldsObject          =100672256  # from enum ObjectTypeEnum
	kCurveAndEntityWorkPointDefObject=83952128   # from enum ObjectTypeEnum
	kCurveGraphicsObject          =50414848   # from enum ObjectTypeEnum
	kCustomConstraint3DObject     =83973120   # from enum ObjectTypeEnum
	kCustomConstraint3DProxyObject=83973232   # from enum ObjectTypeEnum
	kCustomConstraintObject       =100673536  # from enum ObjectTypeEnum
	kCustomConstraintProxyObject  =100677632  # from enum ObjectTypeEnum
	kCustomParameterGroupObject   =50401536   # from enum ObjectTypeEnum
	kCustomParameterGroupsObject  =50398464   # from enum ObjectTypeEnum
	kCustomPropertyFormat         =50430720   # from enum ObjectTypeEnum
	kCustomTableObject            =117461248  # from enum ObjectTypeEnum
	kCustomTablesObject           =117460992  # from enum ObjectTypeEnum
	kCutAcrossBendsExtentObject   =83993344   # from enum ObjectTypeEnum
	kCutDefinitionObject          =151010304  # from enum ObjectTypeEnum
	kCutFeatureObject             =150998016  # from enum ObjectTypeEnum
	kCutFeatureProxyObject        =151003392  # from enum ObjectTypeEnum
	kCutFeaturesObject            =150997760  # from enum ObjectTypeEnum
	kDSDegreeOfFreedomObject      =100703744  # from enum ObjectTypeEnum
	kDSDegreesOfFreedomObject     =100703488  # from enum ObjectTypeEnum
	kDSJointDefinitionObject      =100703232  # from enum ObjectTypeEnum
	kDSJointObject                =100701184  # from enum ObjectTypeEnum
	kDSJointsObject               =100700928  # from enum ObjectTypeEnum
	kDSLoadDefinitionObject       =100702464  # from enum ObjectTypeEnum
	kDSLoadObject                 =100702208  # from enum ObjectTypeEnum
	kDSLoadsObject                =100701952  # from enum ObjectTypeEnum
	kDSResultObject               =100704256  # from enum ObjectTypeEnum
	kDSResultsObject              =100704000  # from enum ObjectTypeEnum
	kDSSettingsObject             =100704512  # from enum ObjectTypeEnum
	kDSValueGraphObject           =100702976  # from enum ObjectTypeEnum
	kDSValueObject                =100702720  # from enum ObjectTypeEnum
	kDWGArcObject                 =84041472   # from enum ObjectTypeEnum
	kDWGArcProxyObject            =84041728   # from enum ObjectTypeEnum
	kDWGArcsEnumeratorObject      =84041216   # from enum ObjectTypeEnum
	kDWGBlockDefinitionObject     =84040704   # from enum ObjectTypeEnum
	kDWGBlockDefinitionProxyObject=84040960   # from enum ObjectTypeEnum
	kDWGBlockReferenceObject      =84040192   # from enum ObjectTypeEnum
	kDWGBlockReferenceProxyObject =84040448   # from enum ObjectTypeEnum
	kDWGBlockReferencesEnumeratorObject=84039936   # from enum ObjectTypeEnum
	kDWGEllipticalArcObject       =84042240   # from enum ObjectTypeEnum
	kDWGEllipticalArcProxyObject  =84042496   # from enum ObjectTypeEnum
	kDWGEllipticalArcsEnumeratorObject=84041984   # from enum ObjectTypeEnum
	kDWGEntitiesEnumeratorObject  =84039168   # from enum ObjectTypeEnum
	kDWGEntityObject              =84039424   # from enum ObjectTypeEnum
	kDWGEntityProxyObject         =84039680   # from enum ObjectTypeEnum
	kDWGLineObject                =84043008   # from enum ObjectTypeEnum
	kDWGLineProxyObject           =84043264   # from enum ObjectTypeEnum
	kDWGLinesEnumeratorObject     =84042752   # from enum ObjectTypeEnum
	kDWGPointObject               =84043776   # from enum ObjectTypeEnum
	kDWGPointProxyObject          =84044032   # from enum ObjectTypeEnum
	kDWGPointsEnumeratorObject    =84043520   # from enum ObjectTypeEnum
	kDWGPolyline2DObject          =84046080   # from enum ObjectTypeEnum
	kDWGPolyline2DProxyObject     =84048128   # from enum ObjectTypeEnum
	kDWGPolyline3DObject          =84048640   # from enum ObjectTypeEnum
	kDWGPolyline3DProxyObject     =84048896   # from enum ObjectTypeEnum
	kDWGPolylineObject            =84044544   # from enum ObjectTypeEnum
	kDWGPolylineProxyObject       =84044800   # from enum ObjectTypeEnum
	kDWGPolylines2DEnumeratorObject=84045824   # from enum ObjectTypeEnum
	kDWGPolylines3DEnumeratorObject=84048384   # from enum ObjectTypeEnum
	kDWGPolylinesEnumeratorObject =84044288   # from enum ObjectTypeEnum
	kDWGSplineObject              =84045312   # from enum ObjectTypeEnum
	kDWGSplineProxyObject         =84045568   # from enum ObjectTypeEnum
	kDWGSplinesEnumeratorObject   =84045056   # from enum ObjectTypeEnum
	kDecalFeatureObject           =83952640   # from enum ObjectTypeEnum
	kDecalFeatureProxyObject      =83957248   # from enum ObjectTypeEnum
	kDecalFeaturesObject          =83952896   # from enum ObjectTypeEnum
	kDefaultBorderObject          =117449728  # from enum ObjectTypeEnum
	kDeleteFaceFeatureObject      =83953152   # from enum ObjectTypeEnum
	kDeleteFaceFeatureProxyObject =83957504   # from enum ObjectTypeEnum
	kDeleteFaceFeaturesObject     =83953408   # from enum ObjectTypeEnum
	kDerivedAliasComponentObject  =84007936   # from enum ObjectTypeEnum
	kDerivedAliasComponentsObject =84007680   # from enum ObjectTypeEnum
	kDerivedAssemblyComponentObject=83930368   # from enum ObjectTypeEnum
	kDerivedAssemblyComponentsObject=83930112   # from enum ObjectTypeEnum
	kDerivedAssemblyDefinitionObject=83930624   # from enum ObjectTypeEnum
	kDerivedAssemblyOccurrenceObject=83931136   # from enum ObjectTypeEnum
	kDerivedAssemblyOccurrencesObject=83934464   # from enum ObjectTypeEnum
	kDerivedParameterObject       =50412544   # from enum ObjectTypeEnum
	kDerivedParameterTableObject  =50412032   # from enum ObjectTypeEnum
	kDerivedParameterTablesObject =50411776   # from enum ObjectTypeEnum
	kDerivedParametersObject      =50412288   # from enum ObjectTypeEnum
	kDerivedPartComponentObject   =83928832   # from enum ObjectTypeEnum
	kDerivedPartComponentsObject  =83928576   # from enum ObjectTypeEnum
	kDerivedPartCoordinateSystemDefObject=83951360   # from enum ObjectTypeEnum
	kDerivedPartDefinitionObject  =83929600   # from enum ObjectTypeEnum
	kDerivedPartEntitiesObject    =83929088   # from enum ObjectTypeEnum
	kDerivedPartEntityObject      =83929344   # from enum ObjectTypeEnum
	kDerivedPartTransformDefObject=83951104   # from enum ObjectTypeEnum
	kDerivedPartUniformScaleDefObject=83950848   # from enum ObjectTypeEnum
	kDesignProjectManagerObject   =50401024   # from enum ObjectTypeEnum
	kDesignProjectObject          =50379008   # from enum ObjectTypeEnum
	kDesignProjectsObject         =50401280   # from enum ObjectTypeEnum
	kDesignViewRepresentationObject=100679424  # from enum ObjectTypeEnum
	kDesignViewRepresentationsObject=100679168  # from enum ObjectTypeEnum
	kDetailDrawingViewObject      =117474304  # from enum ObjectTypeEnum
	kDiameterDimConstraintObject  =83906560   # from enum ObjectTypeEnum
	kDiameterDimConstraintProxyObject=83906672   # from enum ObjectTypeEnum
	kDiameterGeneralDimensionObject=117475328  # from enum ObjectTypeEnum
	kDiameterModelDimensionDefinitionObject=84026112   # from enum ObjectTypeEnum
	kDiameterModelDimensionObject =84023296   # from enum ObjectTypeEnum
	kDiameterModelDimensionsObject=84022528   # from enum ObjectTypeEnum
	kDimensionConstraints3DObject =83970560   # from enum ObjectTypeEnum
	kDimensionConstraintsObject   =83905280   # from enum ObjectTypeEnum
	kDimensionStyleObject         =117452800  # from enum ObjectTypeEnum
	kDimensionStylesEnumeratorObject=117453056  # from enum ObjectTypeEnum
	kDimensionTextObject          =117464320  # from enum ObjectTypeEnum
	kDirectEditDeleteOperationObject=84036096   # from enum ObjectTypeEnum
	kDirectEditDeleteOperationProxyObject=84036352   # from enum ObjectTypeEnum
	kDirectEditFeatureObject      =84033024   # from enum ObjectTypeEnum
	kDirectEditFeatureProxyObject =84033536   # from enum ObjectTypeEnum
	kDirectEditFeaturesObject     =84033280   # from enum ObjectTypeEnum
	kDirectEditMoveOperationObject=84034560   # from enum ObjectTypeEnum
	kDirectEditMoveOperationProxyObject=84034816   # from enum ObjectTypeEnum
	kDirectEditOperationObject    =84033792   # from enum ObjectTypeEnum
	kDirectEditOperationProxyObject=84034304   # from enum ObjectTypeEnum
	kDirectEditOperationsObject   =84034048   # from enum ObjectTypeEnum
	kDirectEditRotateOperationObject=84035584   # from enum ObjectTypeEnum
	kDirectEditRotateOperationProxyObject=84035840   # from enum ObjectTypeEnum
	kDirectEditScaleOperationObject=84049152   # from enum ObjectTypeEnum
	kDirectEditScaleOperationProxyObject=84049408   # from enum ObjectTypeEnum
	kDirectEditSizeOperationObject=84035072   # from enum ObjectTypeEnum
	kDirectEditSizeOperationProxyObject=84035328   # from enum ObjectTypeEnum
	kDirectionAndDistanceMoveDefinitionObject=84012032   # from enum ObjectTypeEnum
	kDisabledCommandListObject    =50391296   # from enum ObjectTypeEnum
	kDisplayOptionsObject         =50413312   # from enum ObjectTypeEnum
	kDisplaySettingsObject        =50435840   # from enum ObjectTypeEnum
	kDistanceAndAngleChamferDefObject=83925760   # from enum ObjectTypeEnum
	kDistanceChamferDefObject     =83925504   # from enum ObjectTypeEnum
	kDistanceExtentObject         =83917824   # from enum ObjectTypeEnum
	kDistanceHeightExtentObject   =83995648   # from enum ObjectTypeEnum
	kDockableWindowObject         =50433280   # from enum ObjectTypeEnum
	kDockableWindowsEventsObject  =50442240   # from enum ObjectTypeEnum
	kDockableWindowsObject        =50433024   # from enum ObjectTypeEnum
	kDocumentDescriptorObject     =50407936   # from enum ObjectTypeEnum
	kDocumentDescriptorsEnumeratorObject=50408192   # from enum ObjectTypeEnum
	kDocumentEventsObject         =50333440   # from enum ObjectTypeEnum
	kDocumentInterestObject       =50415616   # from enum ObjectTypeEnum
	kDocumentInterestsObject      =50415360   # from enum ObjectTypeEnum
	kDocumentObject               =50332160   # from enum ObjectTypeEnum
	kDocumentSubTypeObject        =50378496   # from enum ObjectTypeEnum
	kDocumentsEnumeratorObject    =50349824   # from enum ObjectTypeEnum
	kDocumentsObject              =50332416   # from enum ObjectTypeEnum
	kDoubleHemDefinitionObject    =151015424  # from enum ObjectTypeEnum
	kDraftAnalysesObject          =50416640   # from enum ObjectTypeEnum
	kDraftAnalysisObject          =50416896   # from enum ObjectTypeEnum
	kDraftingStandardObject       =117441792  # from enum ObjectTypeEnum
	kDragContextObject            =50440704   # from enum ObjectTypeEnum
	kDrawingBOMCellObject         =117487104  # from enum ObjectTypeEnum
	kDrawingBOMColumnObject       =117486336  # from enum ObjectTypeEnum
	kDrawingBOMColumnsObject      =117486080  # from enum ObjectTypeEnum
	kDrawingBOMObject             =117485824  # from enum ObjectTypeEnum
	kDrawingBOMRowObject          =117486848  # from enum ObjectTypeEnum
	kDrawingBOMRowsObject         =117486592  # from enum ObjectTypeEnum
	kDrawingBOMsObject            =117485568  # from enum ObjectTypeEnum
	kDrawingCurveObject           =117473792  # from enum ObjectTypeEnum
	kDrawingCurveSegmentObject    =117478144  # from enum ObjectTypeEnum
	kDrawingCurveSegmentsObject   =117477888  # from enum ObjectTypeEnum
	kDrawingCurvesEnumeratorObject=117473536  # from enum ObjectTypeEnum
	kDrawingDimensionObject       =117454848  # from enum ObjectTypeEnum
	kDrawingDimensionsObject      =117454592  # from enum ObjectTypeEnum
	kDrawingEventsObject          =117464832  # from enum ObjectTypeEnum
	kDrawingNoteObject            =117472000  # from enum ObjectTypeEnum
	kDrawingNotesObject           =117471744  # from enum ObjectTypeEnum
	kDrawingOptionsObject         =50415104   # from enum ObjectTypeEnum
	kDrawingPrintManagerObject    =50351616   # from enum ObjectTypeEnum
	kDrawingSettingsObject        =117449984  # from enum ObjectTypeEnum
	kDrawingSketchObject          =117443328  # from enum ObjectTypeEnum
	kDrawingSketchesObject        =117443584  # from enum ObjectTypeEnum
	kDrawingStandardStyleObject   =117454080  # from enum ObjectTypeEnum
	kDrawingStandardStylesEnumeratorObject=117453824  # from enum ObjectTypeEnum
	kDrawingStylesManagerObject   =117453568  # from enum ObjectTypeEnum
	kDrawingViewEventsObject      =117450496  # from enum ObjectTypeEnum
	kDrawingViewLabelObject       =117479936  # from enum ObjectTypeEnum
	kDrawingViewObject            =117441536  # from enum ObjectTypeEnum
	kDrawingViewsObject           =117442304  # from enum ObjectTypeEnum
	kDriveConstraintSettingsObject=100700160  # from enum ObjectTypeEnum
	kDriveSettingsObject          =100706816  # from enum ObjectTypeEnum
	kDynamicSimulationObject      =100700416  # from enum ObjectTypeEnum
	kDynamicSimulationsObject     =100701696  # from enum ObjectTypeEnum
	kEdgeCollectionObject         =28928      # from enum ObjectTypeEnum
	kEdgeDefinitionObject         =50429952   # from enum ObjectTypeEnum
	kEdgeDefinitionsObject        =50429696   # from enum ObjectTypeEnum
	kEdgeLoopDefinitionObject     =50428928   # from enum ObjectTypeEnum
	kEdgeLoopDefinitionsObject    =50428672   # from enum ObjectTypeEnum
	kEdgeLoopObject               =67119664   # from enum ObjectTypeEnum
	kEdgeLoopProxyObject          =67119712   # from enum ObjectTypeEnum
	kEdgeLoopsObject              =67122224   # from enum ObjectTypeEnum
	kEdgeObject                   =67120176   # from enum ObjectTypeEnum
	kEdgeProxyObject              =67120288   # from enum ObjectTypeEnum
	kEdgeUseDefinitionObject      =50429440   # from enum ObjectTypeEnum
	kEdgeUseDefinitionsObject     =50429184   # from enum ObjectTypeEnum
	kEdgeUseObject                =67119920   # from enum ObjectTypeEnum
	kEdgeUseProxyObject           =67120032   # from enum ObjectTypeEnum
	kEdgeUsesObject               =67122480   # from enum ObjectTypeEnum
	kEdgeWidthExtentObject        =83996416   # from enum ObjectTypeEnum
	kEdgesObject                  =1073963056 # from enum ObjectTypeEnum
	kEllipseRadiusDimConstraintObject=83924224   # from enum ObjectTypeEnum
	kEllipseRadiusDimConstraintProxyObject=83924336   # from enum ObjectTypeEnum
	kEmbossFeatureObject          =83953664   # from enum ObjectTypeEnum
	kEmbossFeatureProxyObject     =83957760   # from enum ObjectTypeEnum
	kEmbossFeaturesObject         =83953920   # from enum ObjectTypeEnum
	kEndOfFeaturesObject          =83969536   # from enum ObjectTypeEnum
	kEnvironmentBaseCollectionObject=50375936   # from enum ObjectTypeEnum
	kEnvironmentBaseHandlerObject =50374912   # from enum ObjectTypeEnum
	kEnvironmentBaseObject        =50376192   # from enum ObjectTypeEnum
	kEnvironmentListObject        =50390528   # from enum ObjectTypeEnum
	kEnvironmentManagerObject     =50391552   # from enum ObjectTypeEnum
	kEnvironmentObject            =50363904   # from enum ObjectTypeEnum
	kEnvironmentsObject           =50363648   # from enum ObjectTypeEnum
	kEqualLengthConstraintObject  =83901440   # from enum ObjectTypeEnum
	kEqualLengthConstraintProxyObject=83901552   # from enum ObjectTypeEnum
	kEqualRadiusConstraintObject  =83901696   # from enum ObjectTypeEnum
	kEqualRadiusConstraintProxyObject=83901808   # from enum ObjectTypeEnum
	kErrorManagerObject           =50420736   # from enum ObjectTypeEnum
	kExplodedViewObject           =134218752  # from enum ObjectTypeEnum
	kExplodedViewsObject          =134218496  # from enum ObjectTypeEnum
	kExpressionLimitsObject       =50422784   # from enum ObjectTypeEnum
	kExpressionListObject         =50433792   # from enum ObjectTypeEnum
	kExtendFeatureObject          =83977984   # from enum ObjectTypeEnum
	kExtendFeatureProxyObject     =83978496   # from enum ObjectTypeEnum
	kExtendFeaturesObject         =83978240   # from enum ObjectTypeEnum
	kExtrudeDefinitionObject      =84014080   # from enum ObjectTypeEnum
	kExtrudeFeatureObject         =83910656   # from enum ObjectTypeEnum
	kExtrudeFeatureProxyObject    =83958016   # from enum ObjectTypeEnum
	kExtrudeFeaturesObject        =83910912   # from enum ObjectTypeEnum
	kFaceCollectionObject         =40704      # from enum ObjectTypeEnum
	kFaceDefinitionObject         =50428416   # from enum ObjectTypeEnum
	kFaceDefinitionsObject        =50428160   # from enum ObjectTypeEnum
	kFaceDraftDefinitionObject    =84046336   # from enum ObjectTypeEnum
	kFaceDraftFeatureObject       =83911168   # from enum ObjectTypeEnum
	kFaceDraftFeatureProxyObject  =83958272   # from enum ObjectTypeEnum
	kFaceDraftFeaturesObject      =83911424   # from enum ObjectTypeEnum
	kFaceFeatureDefinitionObject  =151006720  # from enum ObjectTypeEnum
	kFaceFeatureObject            =151000832  # from enum ObjectTypeEnum
	kFaceFeatureProxyObject       =151004672  # from enum ObjectTypeEnum
	kFaceFeaturesObject           =151000576  # from enum ObjectTypeEnum
	kFaceObject                   =67119408   # from enum ObjectTypeEnum
	kFaceOffsetDefinitionObject   =84016640   # from enum ObjectTypeEnum
	kFaceOffsetFeatureObject      =83982080   # from enum ObjectTypeEnum
	kFaceOffsetFeatureProxyObject =83982336   # from enum ObjectTypeEnum
	kFaceOffsetFeaturesObject     =83982592   # from enum ObjectTypeEnum
	kFaceProxyObject              =67119520   # from enum ObjectTypeEnum
	kFaceShellDefinitionObject    =50427904   # from enum ObjectTypeEnum
	kFaceShellDefinitionsObject   =50427648   # from enum ObjectTypeEnum
	kFaceShellObject              =67119152   # from enum ObjectTypeEnum
	kFaceShellProxyObject         =67119264   # from enum ObjectTypeEnum
	kFaceShellsObject             =67121712   # from enum ObjectTypeEnum
	kFacesObject                  =67118592   # from enum ObjectTypeEnum
	kFactoryOptionsObject         =84001024   # from enum ObjectTypeEnum
	kFamilyManagerObject          =50410240   # from enum ObjectTypeEnum
	kFeatureBasedOccurrencePatternObject=100669184  # from enum ObjectTypeEnum
	kFeatureBasedOccurrencePatternProxyObject=100669312  # from enum ObjectTypeEnum
	kFeatureControlFrameObject    =117483008  # from enum ObjectTypeEnum
	kFeatureControlFrameRowObject =117483520  # from enum ObjectTypeEnum
	kFeatureControlFrameRowsObject=117483264  # from enum ObjectTypeEnum
	kFeatureControlFrameStyleObject=117481472  # from enum ObjectTypeEnum
	kFeatureControlFrameStylesEnumeratorObject=117481216  # from enum ObjectTypeEnum
	kFeatureControlFramesObject   =117482752  # from enum ObjectTypeEnum
	kFeatureDimensionObject       =83991296   # from enum ObjectTypeEnum
	kFeatureDimensionProxyObject  =83991408   # from enum ObjectTypeEnum
	kFeatureDimensionsObject      =83991040   # from enum ObjectTypeEnum
	kFeaturePatternElementObject  =83923968   # from enum ObjectTypeEnum
	kFeaturePatternElementProxyObject=83923974   # from enum ObjectTypeEnum
	kFeaturePatternElementsObject =83923712   # from enum ObjectTypeEnum
	kFeaturesObject               =100675328  # from enum ObjectTypeEnum
	kFileAccessEventsObject       =50335488   # from enum ObjectTypeEnum
	kFileAndReferencesCollectionObject=50334976   # from enum ObjectTypeEnum
	kFileDescriptorObject         =50407680   # from enum ObjectTypeEnum
	kFileDescriptorsEnumeratorObject=50407424   # from enum ObjectTypeEnum
	kFileDialogEventsObject       =50414592   # from enum ObjectTypeEnum
	kFileDialogObject             =50377728   # from enum ObjectTypeEnum
	kFileLocationsObject          =50339584   # from enum ObjectTypeEnum
	kFileManagerEventsObject      =50398208   # from enum ObjectTypeEnum
	kFileManagerObject            =50378240   # from enum ObjectTypeEnum
	kFileMetadataObject           =50418176   # from enum ObjectTypeEnum
	kFileObject                   =50407168   # from enum ObjectTypeEnum
	kFileOpenOptionsObject        =50436352   # from enum ObjectTypeEnum
	kFileOptionsObject            =50399488   # from enum ObjectTypeEnum
	kFileSaveAsObject             =50339328   # from enum ObjectTypeEnum
	kFileUIEventsObject           =50333952   # from enum ObjectTypeEnum
	kFilenameAssetValueObject     =50451968   # from enum ObjectTypeEnum
	kFilesEnumeratorObject        =50406912   # from enum ObjectTypeEnum
	kFilletConstantRadiusEdgeSetObject=83927040   # from enum ObjectTypeEnum
	kFilletConstantRadiusFaceSetObject=83978752   # from enum ObjectTypeEnum
	kFilletDefinitionObject       =83926272   # from enum ObjectTypeEnum
	kFilletFaceSetObject          =83978752   # from enum ObjectTypeEnum
	kFilletFeatureObject          =83911680   # from enum ObjectTypeEnum
	kFilletFeatureProxyObject     =83958528   # from enum ObjectTypeEnum
	kFilletFeaturesObject         =83911936   # from enum ObjectTypeEnum
	kFilletFullRoundSetObject     =83979008   # from enum ObjectTypeEnum
	kFilletIntermediateRadiusObject=83927552   # from enum ObjectTypeEnum
	kFilletRadiusEdgeSetObject    =83926784   # from enum ObjectTypeEnum
	kFilletSetbackObject          =83928320   # from enum ObjectTypeEnum
	kFilletSetbackVertexObject    =83928064   # from enum ObjectTypeEnum
	kFilletVariableRadiusEdgeSetObject=83927296   # from enum ObjectTypeEnum
	kFixedWorkAxisDefObject       =83892992   # from enum ObjectTypeEnum
	kFixedWorkPlaneDefObject      =83890432   # from enum ObjectTypeEnum
	kFixedWorkPointDefObject      =83895040   # from enum ObjectTypeEnum
	kFlangeDefinitionObject       =151011840  # from enum ObjectTypeEnum
	kFlangeFeatureObject          =151001344  # from enum ObjectTypeEnum
	kFlangeFeatureProxyObject     =151004928  # from enum ObjectTypeEnum
	kFlangeFeaturesObject         =151001088  # from enum ObjectTypeEnum
	kFlatBendResultObject         =151005952  # from enum ObjectTypeEnum
	kFlatBendResultsObject        =151005696  # from enum ObjectTypeEnum
	kFlatPatternFeaturesObject    =84000768   # from enum ObjectTypeEnum
	kFlatPatternObject            =151002624  # from enum ObjectTypeEnum
	kFlatPatternOrientationObject =151023872  # from enum ObjectTypeEnum
	kFlatPatternOrientationsObject=151023616  # from enum ObjectTypeEnum
	kFlatPatternPlateObject       =151024128  # from enum ObjectTypeEnum
	kFlatPatternPlatesObject      =151024384  # from enum ObjectTypeEnum
	kFlatPunchResultObject        =151006464  # from enum ObjectTypeEnum
	kFlatPunchResultsObject       =151006208  # from enum ObjectTypeEnum
	kFloatAssetValueObject        =50450176   # from enum ObjectTypeEnum
	kFlushConstraintObject        =100666368  # from enum ObjectTypeEnum
	kFlushConstraintProxyObject   =100675840  # from enum ObjectTypeEnum
	kFlushiMateDefinitionObject   =83947264   # from enum ObjectTypeEnum
	kFlushiMateDefinitionProxyObject=83947392   # from enum ObjectTypeEnum
	kFoldDefinitionObject         =151010560  # from enum ObjectTypeEnum
	kFoldFeatureObject            =150999296  # from enum ObjectTypeEnum
	kFoldFeatureProxyObject       =151003904  # from enum ObjectTypeEnum
	kFoldFeaturesObject           =150998784  # from enum ObjectTypeEnum
	kFreeDragMoveOperationObject  =84015104   # from enum ObjectTypeEnum
	kFreeMoveDefinitionObject     =84012544   # from enum ObjectTypeEnum
	kFreeformFeatureObject        =84032256   # from enum ObjectTypeEnum
	kFreeformFeatureProxyObject   =84032768   # from enum ObjectTypeEnum
	kFreeformFeaturesObject       =84032512   # from enum ObjectTypeEnum
	kFromToExtentObject           =83919360   # from enum ObjectTypeEnum
	kFromToWidthExtentObject      =83997440   # from enum ObjectTypeEnum
	kFullSweepExtentObject        =83918336   # from enum ObjectTypeEnum
	kGeneralDimensionObject       =117456896  # from enum ObjectTypeEnum
	kGeneralDimensionsEnumeratorObject=117464576  # from enum ObjectTypeEnum
	kGeneralDimensionsObject      =117455104  # from enum ObjectTypeEnum
	kGeneralNoteObject            =117472512  # from enum ObjectTypeEnum
	kGeneralNotesObject           =117472256  # from enum ObjectTypeEnum
	kGeneralOptionsObject         =50386688   # from enum ObjectTypeEnum
	kGeneralPreferencesObject     =50345216   # from enum ObjectTypeEnum
	kGenericObject                =2130706445 # from enum ObjectTypeEnum
	kGeometricConstraints3DObject =83941376   # from enum ObjectTypeEnum
	kGeometricConstraintsObject   =83899904   # from enum ObjectTypeEnum
	kGeometryIntentObject         =117474048  # from enum ObjectTypeEnum
	kGraphicsColorMapperObject    =84000512   # from enum ObjectTypeEnum
	kGraphicsColorSetObject       =50360832   # from enum ObjectTypeEnum
	kGraphicsCoordinateSetObject  =50360320   # from enum ObjectTypeEnum
	kGraphicsDataSetObject        =50360064   # from enum ObjectTypeEnum
	kGraphicsDataSetsCollectionObject=50359552   # from enum ObjectTypeEnum
	kGraphicsDataSetsObject       =50359808   # from enum ObjectTypeEnum
	kGraphicsImageSetObject       =50431744   # from enum ObjectTypeEnum
	kGraphicsIndexSetObject       =50361088   # from enum ObjectTypeEnum
	kGraphicsNodeObject           =50356736   # from enum ObjectTypeEnum
	kGraphicsNodeProxyObject      =50356896   # from enum ObjectTypeEnum
	kGraphicsNormalSetObject      =50360576   # from enum ObjectTypeEnum
	kGraphicsPreferencesObject    =50340096   # from enum ObjectTypeEnum
	kGraphicsPrimitiveObject      =50356992   # from enum ObjectTypeEnum
	kGraphicsTextureCoordinateSetObject=84000256   # from enum ObjectTypeEnum
	kGrillFeatureObject           =84002816   # from enum ObjectTypeEnum
	kGrillFeatureProxyObject      =84002928   # from enum ObjectTypeEnum
	kGrillFeaturesObject          =84003072   # from enum ObjectTypeEnum
	kGripSnapOptionsObject        =50430976   # from enum ObjectTypeEnum
	kGroundConstraint3DObject     =83965952   # from enum ObjectTypeEnum
	kGroundConstraint3DProxyObject=83966064   # from enum ObjectTypeEnum
	kGroundConstraintObject       =83901952   # from enum ObjectTypeEnum
	kGroundConstraintProxyObject  =83902064   # from enum ObjectTypeEnum
	kGroundPlaneSettingsObject    =50436096   # from enum ObjectTypeEnum
	kHardwareOptionsObject        =50406656   # from enum ObjectTypeEnum
	kHeadsUpDisplayOptionsObject  =50435584   # from enum ObjectTypeEnum
	kHelicalConstraint3DObject    =84009216   # from enum ObjectTypeEnum
	kHelicalConstraint3DProxyObject=84009328   # from enum ObjectTypeEnum
	kHelpEventsObject             =50442496   # from enum ObjectTypeEnum
	kHelpManagerObject            =50344960   # from enum ObjectTypeEnum
	kHemDefinitionObject          =151014400  # from enum ObjectTypeEnum
	kHemFeatureObject             =150998528  # from enum ObjectTypeEnum
	kHemFeatureProxyObject        =151003648  # from enum ObjectTypeEnum
	kHemFeaturesObject            =150998272  # from enum ObjectTypeEnum
	kHighlightSetObject           =50366976   # from enum ObjectTypeEnum
	kHighlightSetsObject          =50366720   # from enum ObjectTypeEnum
	kHoleFeatureObject            =83912192   # from enum ObjectTypeEnum
	kHoleFeatureProxyObject       =83958784   # from enum ObjectTypeEnum
	kHoleFeaturesObject           =83912448   # from enum ObjectTypeEnum
	kHoleNoteObject               =117487360  # from enum ObjectTypeEnum
	kHolePlacementDefinitionObject=83966464   # from enum ObjectTypeEnum
	kHoleTableCellObject          =117471232  # from enum ObjectTypeEnum
	kHoleTableColumnObject        =117470464  # from enum ObjectTypeEnum
	kHoleTableColumnsObject       =117470208  # from enum ObjectTypeEnum
	kHoleTableObject              =117469952  # from enum ObjectTypeEnum
	kHoleTableRowObject           =117470976  # from enum ObjectTypeEnum
	kHoleTableRowsObject          =117470720  # from enum ObjectTypeEnum
	kHoleTableStyleObject         =117485312  # from enum ObjectTypeEnum
	kHoleTableStylesEnumeratorObject=117485056  # from enum ObjectTypeEnum
	kHoleTablesObject             =117469696  # from enum ObjectTypeEnum
	kHoleTagObject                =117471488  # from enum ObjectTypeEnum
	kHoleTapInfoObject            =83920384   # from enum ObjectTypeEnum
	kHoleThreadNoteObject         =117491712  # from enum ObjectTypeEnum
	kHoleThreadNotesObject        =117491456  # from enum ObjectTypeEnum
	kHorizontalAlignConstraintObject=83902464   # from enum ObjectTypeEnum
	kHorizontalAlignConstraintProxyObject=83902576   # from enum ObjectTypeEnum
	kHorizontalConstraintObject   =83902208   # from enum ObjectTypeEnum
	kHorizontalConstraintProxyObject=83902320   # from enum ObjectTypeEnum
	kImportedComponentDefinitionObject=84047104   # from enum ObjectTypeEnum
	kImportedComponentObject      =84046592   # from enum ObjectTypeEnum
	kImportedComponentsObject     =84046848   # from enum ObjectTypeEnum
	kImportedDWGComponentDefinitionObject=84038912   # from enum ObjectTypeEnum
	kImportedDWGComponentObject   =84038400   # from enum ObjectTypeEnum
	kImportedDWGComponentProxyObject=84038656   # from enum ObjectTypeEnum
	kImportedGenericComponentDefinitionObject=84047872   # from enum ObjectTypeEnum
	kImportedGenericComponentObject=84049664   # from enum ObjectTypeEnum
	kImportedGenericComponentProxyObject=84049920   # from enum ObjectTypeEnum
	kImportedModelEntitiesObject  =84047360   # from enum ObjectTypeEnum
	kImportedModelEntityObject    =84047616   # from enum ObjectTypeEnum
	kInsertConstraintObject       =100665344  # from enum ObjectTypeEnum
	kInsertConstraintProxyObject  =100676096  # from enum ObjectTypeEnum
	kInsertiMateDefinitionObject  =83947520   # from enum ObjectTypeEnum
	kInsertiMateDefinitionProxyObject=83947648   # from enum ObjectTypeEnum
	kIntegerAssetValueObject      =50450432   # from enum ObjectTypeEnum
	kIntentConfigurationObject    =50416128   # from enum ObjectTypeEnum
	kInteractionEventsObject      =50353152   # from enum ObjectTypeEnum
	kInteractionGraphicsObject    =50387200   # from enum ObjectTypeEnum
	kInterferenceResultObject     =100668416  # from enum ObjectTypeEnum
	kInterferenceResultsObject    =100668160  # from enum ObjectTypeEnum
	kIntersectionCurveObject      =84026624   # from enum ObjectTypeEnum
	kIntersectionCurveProxyObject =84026736   # from enum ObjectTypeEnum
	kIntersectionCurvesObject     =84026368   # from enum ObjectTypeEnum
	kInventorVBAArgumentObject    =50370304   # from enum ObjectTypeEnum
	kInventorVBAArgumentsObject   =50370048   # from enum ObjectTypeEnum
	kInventorVBAComponentObject   =50369280   # from enum ObjectTypeEnum
	kInventorVBAComponentsObject  =50369024   # from enum ObjectTypeEnum
	kInventorVBAMemberObject      =50369792   # from enum ObjectTypeEnum
	kInventorVBAMembersObject     =50369536   # from enum ObjectTypeEnum
	kInventorVBAProjectObject     =50368768   # from enum ObjectTypeEnum
	kInventorVBAProjectsObject    =50368512   # from enum ObjectTypeEnum
	kJointOriginDWGObject         =100707331  # from enum ObjectTypeEnum
	kJointOriginEdgeObject        =100707329  # from enum ObjectTypeEnum
	kJointOriginFaceObject        =100707328  # from enum ObjectTypeEnum
	kJointOriginSketchObject      =100707330  # from enum ObjectTypeEnum
	kKeyboardEventsObject         =50354176   # from enum ObjectTypeEnum
	kKnitFeatureObject            =83954176   # from enum ObjectTypeEnum
	kKnitFeatureProxyObject       =83959040   # from enum ObjectTypeEnum
	kKnitFeaturesObject           =83954432   # from enum ObjectTypeEnum
	kLanguageToolsObject          =50415872   # from enum ObjectTypeEnum
	kLayerObject                  =117466112  # from enum ObjectTypeEnum
	kLayersEnumeratorObject       =117465856  # from enum ObjectTypeEnum
	kLayoutConstraintObject       =100699392  # from enum ObjectTypeEnum
	kLayoutConstraintProxyObject  =100699648  # from enum ObjectTypeEnum
	kLeaderNodeObject             =117477376  # from enum ObjectTypeEnum
	kLeaderNodesEnumeratorObject  =117477632  # from enum ObjectTypeEnum
	kLeaderNoteObject             =117473024  # from enum ObjectTypeEnum
	kLeaderNotesObject            =117472768  # from enum ObjectTypeEnum
	kLeaderObject                 =117475584  # from enum ObjectTypeEnum
	kLeaderStyleObject            =117480448  # from enum ObjectTypeEnum
	kLeaderStylesEnumeratorObject =117480192  # from enum ObjectTypeEnum
	kLegacyDistanceHeightExtentObject=83995904   # from enum ObjectTypeEnum
	kLevelOfDetailRepresentationObject=100679936  # from enum ObjectTypeEnum
	kLevelOfDetailRepresentationsObject=100679680  # from enum ObjectTypeEnum
	kLibraryFolderObject          =117499392  # from enum ObjectTypeEnum
	kLibraryFoldersObject         =117499648  # from enum ObjectTypeEnum
	kLibraryManagerObject         =50409728   # from enum ObjectTypeEnum
	kLibrarySketchedSymbolDefinitionObject=117498880  # from enum ObjectTypeEnum
	kLibrarySketchedSymbolDefinitionsObject=117499136  # from enum ObjectTypeEnum
	kLightObject                  =50402560   # from enum ObjectTypeEnum
	kLightingStyleObject          =50402048   # from enum ObjectTypeEnum
	kLightingStylesObject         =50401792   # from enum ObjectTypeEnum
	kLightsObject                 =50402304   # from enum ObjectTypeEnum
	kLineAndFaceWorkPointDefObject=83894272   # from enum ObjectTypeEnum
	kLineAndPlaneWorkAxisDefObject=83892736   # from enum ObjectTypeEnum
	kLineAndPointWorkAxisDefObject=83979264   # from enum ObjectTypeEnum
	kLineAndPointWorkPlaneDefObject=83888640   # from enum ObjectTypeEnum
	kLineAndTangentWorkPlaneDefObject=83889664   # from enum ObjectTypeEnum
	kLineGraphicsObject           =50357248   # from enum ObjectTypeEnum
	kLineLengthDimConstraint3DObject=83971840   # from enum ObjectTypeEnum
	kLineLengthDimConstraint3DProxyObject=83971952   # from enum ObjectTypeEnum
	kLinePlaneAndAngleWorkPlaneDefObject=83889152   # from enum ObjectTypeEnum
	kLineStripGraphicsObject      =50357504   # from enum ObjectTypeEnum
	kLineWorkAxisDefObject        =83891456   # from enum ObjectTypeEnum
	kLinearGeneralDimensionObject =117474560  # from enum ObjectTypeEnum
	kLinearHolePlacementDefinitionObject=83966976   # from enum ObjectTypeEnum
	kLinearModelDimensionDefinitionObject=84021504   # from enum ObjectTypeEnum
	kLinearModelDimensionObject   =84021760   # from enum ObjectTypeEnum
	kLinearModelDimensionsObject  =84020992   # from enum ObjectTypeEnum
	kLipFeatureObject             =84003328   # from enum ObjectTypeEnum
	kLipFeatureProxyObject        =84003440   # from enum ObjectTypeEnum
	kLipFeaturesObject            =84003584   # from enum ObjectTypeEnum
	kLoftFeatureObject            =83912704   # from enum ObjectTypeEnum
	kLoftFeatureProxyObject       =83959296   # from enum ObjectTypeEnum
	kLoftFeaturesObject           =83912960   # from enum ObjectTypeEnum
	kLoftRailObject               =83977472   # from enum ObjectTypeEnum
	kLoftRailsObject              =83977216   # from enum ObjectTypeEnum
	kLoftSectionDimensionObject   =83992576   # from enum ObjectTypeEnum
	kLoftSectionDimensionsObject  =83992320   # from enum ObjectTypeEnum
	kLoftedFlangeDefinitionObject =151023360  # from enum ObjectTypeEnum
	kLoftedFlangeFeatureObject    =151015680  # from enum ObjectTypeEnum
	kLoftedFlangeFeatureProxyObject=151016192  # from enum ObjectTypeEnum
	kLoftedFlangeFeaturesObject   =151015936  # from enum ObjectTypeEnum
	kLumpDefinitionObject         =50432768   # from enum ObjectTypeEnum
	kLumpDefinitionsObject        =50432512   # from enum ObjectTypeEnum
	kMachiningObject              =100698880  # from enum ObjectTypeEnum
	kMacroControlDefinitionObject =50372352   # from enum ObjectTypeEnum
	kMapPointCurveObject          =83945984   # from enum ObjectTypeEnum
	kMapPointCurvesObject         =83946240   # from enum ObjectTypeEnum
	kMassPropertiesObject         =50366208   # from enum ObjectTypeEnum
	kMateConstraintObject         =100665856  # from enum ObjectTypeEnum
	kMateConstraintProxyObject    =100676352  # from enum ObjectTypeEnum
	kMateiMateDefinitionObject    =83947776   # from enum ObjectTypeEnum
	kMateiMateDefinitionProxyObject=83947904   # from enum ObjectTypeEnum
	kMaterialAssetObject          =50448896   # from enum ObjectTypeEnum
	kMaterialObject               =50362368   # from enum ObjectTypeEnum
	kMaterialsEnumeratorObject    =50426368   # from enum ObjectTypeEnum
	kMaterialsObject              =50362112   # from enum ObjectTypeEnum
	kMeasureEventsObject          =50416384   # from enum ObjectTypeEnum
	kMeasureToolsObject           =50413568   # from enum ObjectTypeEnum
	kMemberManagerObject          =50410496   # from enum ObjectTypeEnum
	kMessageSectionObject         =50420992   # from enum ObjectTypeEnum
	kMidPointWorkPointDefObject   =83894784   # from enum ObjectTypeEnum
	kMidSurfaceFeatureObject      =84016128   # from enum ObjectTypeEnum
	kMidSurfaceFeatureProxyObject =84015872   # from enum ObjectTypeEnum
	kMidSurfaceFeaturesObject     =84016384   # from enum ObjectTypeEnum
	kMidSurfaceThicknessObject    =84017152   # from enum ObjectTypeEnum
	kMidSurfaceThicknessesObject  =84016896   # from enum ObjectTypeEnum
	kMidpointConstraint3DObject   =84000000   # from enum ObjectTypeEnum
	kMidpointConstraint3DProxyObject=84000112   # from enum ObjectTypeEnum
	kMidpointConstraintObject     =83902720   # from enum ObjectTypeEnum
	kMidpointConstraintProxyObject=83902832   # from enum ObjectTypeEnum
	kMiniToolbarButtonObject      =50443520   # from enum ObjectTypeEnum
	kMiniToolbarCheckBoxObject    =50443776   # from enum ObjectTypeEnum
	kMiniToolbarComboBoxObject    =50444032   # from enum ObjectTypeEnum
	kMiniToolbarControlObject     =50443264   # from enum ObjectTypeEnum
	kMiniToolbarControlsObject    =50444800   # from enum ObjectTypeEnum
	kMiniToolbarDropdownObject    =50444288   # from enum ObjectTypeEnum
	kMiniToolbarListItemObject    =50445312   # from enum ObjectTypeEnum
	kMiniToolbarObject            =50441216   # from enum ObjectTypeEnum
	kMiniToolbarSliderObject      =50446848   # from enum ObjectTypeEnum
	kMiniToolbarTextEditorObject  =50453504   # from enum ObjectTypeEnum
	kMiniToolbarValueEditorObject =50444544   # from enum ObjectTypeEnum
	kMirrorFeatureObject          =83913216   # from enum ObjectTypeEnum
	kMirrorFeatureProxyObject     =83959552   # from enum ObjectTypeEnum
	kMirrorFeaturesObject         =83913472   # from enum ObjectTypeEnum
	kModelAnnotationObject        =84020224   # from enum ObjectTypeEnum
	kModelAnnotationTextObject    =84027136   # from enum ObjectTypeEnum
	kModelAnnotationsEnumeratorObject=84030208   # from enum ObjectTypeEnum
	kModelAnnotationsObject       =84019968   # from enum ObjectTypeEnum
	kModelDatumIdentifierDefinitionObject=84031744   # from enum ObjectTypeEnum
	kModelDatumIdentifierObject   =84031488   # from enum ObjectTypeEnum
	kModelDatumIdentifiersObject  =84031232   # from enum ObjectTypeEnum
	kModelDimensionDefinitionObject=84021248   # from enum ObjectTypeEnum
	kModelDimensionObject         =84020736   # from enum ObjectTypeEnum
	kModelDimensionsObject        =84020480   # from enum ObjectTypeEnum
	kModelFeatureControlFrameDefinitionObject=84030976   # from enum ObjectTypeEnum
	kModelFeatureControlFrameObject=84024064   # from enum ObjectTypeEnum
	kModelFeatureControlFrameRowObject=84030720   # from enum ObjectTypeEnum
	kModelFeatureControlFrameRowsObject=84030464   # from enum ObjectTypeEnum
	kModelFeatureControlFramesObject=84023808   # from enum ObjectTypeEnum
	kModelHoleThreadNoteDefinitionObject=84029440   # from enum ObjectTypeEnum
	kModelHoleThreadNoteObject    =84028928   # from enum ObjectTypeEnum
	kModelHoleThreadNotesObject   =84029184   # from enum ObjectTypeEnum
	kModelLeaderNodeObject        =84024576   # from enum ObjectTypeEnum
	kModelLeaderNodesEnumeratorObject=84024832   # from enum ObjectTypeEnum
	kModelLeaderNoteDefinitionObject=84026880   # from enum ObjectTypeEnum
	kModelLeaderNoteObject        =84025088   # from enum ObjectTypeEnum
	kModelLeaderNotesObject       =84025344   # from enum ObjectTypeEnum
	kModelLeaderObject            =84024320   # from enum ObjectTypeEnum
	kModelParameterObject         =50348544   # from enum ObjectTypeEnum
	kModelParametersObject        =50347264   # from enum ObjectTypeEnum
	kModelSurfaceTextureSymbolDefinitionObject=84028416   # from enum ObjectTypeEnum
	kModelSurfaceTextureSymbolObject=84028160   # from enum ObjectTypeEnum
	kModelSurfaceTextureSymbolsObject=84028672   # from enum ObjectTypeEnum
	kModelingEventsObject         =50408704   # from enum ObjectTypeEnum
	kModelingSettingsObject       =50383872   # from enum ObjectTypeEnum
	kMouseEventsObject            =50353664   # from enum ObjectTypeEnum
	kMoveAlongRayMoveOperationObject=84015360   # from enum ObjectTypeEnum
	kMoveDefinitionObject         =84014592   # from enum ObjectTypeEnum
	kMoveFaceDefinitionObject     =84011776   # from enum ObjectTypeEnum
	kMoveFaceFeatureObject        =83967744   # from enum ObjectTypeEnum
	kMoveFaceFeatureProxyObject   =83968000   # from enum ObjectTypeEnum
	kMoveFaceFeaturesObject       =83968256   # from enum ObjectTypeEnum
	kMoveFeatureObject            =84002048   # from enum ObjectTypeEnum
	kMoveFeatureProxyObject       =84002208   # from enum ObjectTypeEnum
	kMoveFeaturesObject           =84001792   # from enum ObjectTypeEnum
	kMoveOperationObject          =84014848   # from enum ObjectTypeEnum
	kNativeBrowserNodeDefinitionObject=50387456   # from enum ObjectTypeEnum
	kNonLinearEdgeWorkPointDefObject=83979776   # from enum ObjectTypeEnum
	kNonParametricBaseFeatureObject=83920896   # from enum ObjectTypeEnum
	kNonParametricBaseFeatureProxyObject=83962112   # from enum ObjectTypeEnum
	kNonParametricBaseFeaturesObject=83945728   # from enum ObjectTypeEnum
	kNormalToCurveWorkPlaneDefObject=83951616   # from enum ObjectTypeEnum
	kNormalToSurfaceWorkAxisDefObject=83968768   # from enum ObjectTypeEnum
	kNotebookOptionsObject        =50406400   # from enum ObjectTypeEnum
	kOGSRenderItemObject          =100705536  # from enum ObjectTypeEnum
	kOGSRenderItemsEnumeratorObject=100705792  # from enum ObjectTypeEnum
	kOGSSceneNodeObject           =100705024  # from enum ObjectTypeEnum
	kOGSSceneNodesEnumeratorObject=100705280  # from enum ObjectTypeEnum
	kObjectCollectionByVariantObject=2130706444 # from enum ObjectTypeEnum
	kObjectCollectionObject       =2130706443 # from enum ObjectTypeEnum
	kObjectDefaultsStyleObject    =117454336  # from enum ObjectTypeEnum
	kObjectDefaultsStylesEnumeratorObject=117464064  # from enum ObjectTypeEnum
	kObjectVisibilityObject       =50431488   # from enum ObjectTypeEnum
	kObjectsEnumeratorByVariantObject=2130706451 # from enum ObjectTypeEnum
	kObjectsEnumeratorObject      =2130706450 # from enum ObjectTypeEnum
	kOccurrencePatternElementObject=67128832   # from enum ObjectTypeEnum
	kOccurrencePatternElementProxyObject=67128992   # from enum ObjectTypeEnum
	kOccurrencePatternElementsObject=100669952  # from enum ObjectTypeEnum
	kOccurrencePatternObject      =100668928  # from enum ObjectTypeEnum
	kOccurrencePatternsObject     =100668672  # from enum ObjectTypeEnum
	kOffsetConstraintObject       =83901184   # from enum ObjectTypeEnum
	kOffsetConstraintProxyObject  =83901296   # from enum ObjectTypeEnum
	kOffsetDimConstraintObject    =83905536   # from enum ObjectTypeEnum
	kOffsetDimConstraintProxyObject=83905648   # from enum ObjectTypeEnum
	kOffsetSplineDimConstraintObject=83972608   # from enum ObjectTypeEnum
	kOffsetSplineDimConstraintProxyObject=83972720   # from enum ObjectTypeEnum
	kOffsetWidthExtentObject      =83997184   # from enum ObjectTypeEnum
	kOrdinateDimensionObject      =117484800  # from enum ObjectTypeEnum
	kOrdinateDimensionSetObject   =117489408  # from enum ObjectTypeEnum
	kOrdinateDimensionSetsObject  =117489152  # from enum ObjectTypeEnum
	kOrdinateDimensionsEnumeratorObject=117489664  # from enum ObjectTypeEnum
	kOrdinateDimensionsObject     =117484544  # from enum ObjectTypeEnum
	kOriginIndicatorObject        =117484288  # from enum ObjectTypeEnum
	kPanelBarObject               =50372864   # from enum ObjectTypeEnum
	kParallelConstraint3DObject   =83965696   # from enum ObjectTypeEnum
	kParallelConstraint3DProxyObject=83965808   # from enum ObjectTypeEnum
	kParallelConstraintObject     =83902976   # from enum ObjectTypeEnum
	kParallelConstraintProxyObject=83903088   # from enum ObjectTypeEnum
	kParameterTableObject         =50349568   # from enum ObjectTypeEnum
	kParameterTablesObject        =50348288   # from enum ObjectTypeEnum
	kParametersEnumeratorObject   =50367488   # from enum ObjectTypeEnum
	kParametersObject             =50347008   # from enum ObjectTypeEnum
	kPartComponentDefinitionObject=83886592   # from enum ObjectTypeEnum
	kPartComponentDefinitionsObject=83887360   # from enum ObjectTypeEnum
	kPartEventsObject             =83895552   # from enum ObjectTypeEnum
	kPartFeatureObject            =83886848   # from enum ObjectTypeEnum
	kPartFeaturesEnumeratorObject =83917312   # from enum ObjectTypeEnum
	kPartFeaturesObject           =83887104   # from enum ObjectTypeEnum
	kPartOptionsObject            =50405632   # from enum ObjectTypeEnum
	kPartsListCellObject          =117445376  # from enum ObjectTypeEnum
	kPartsListColumnObject        =117444608  # from enum ObjectTypeEnum
	kPartsListColumnsObject       =117444352  # from enum ObjectTypeEnum
	kPartsListObject              =117444096  # from enum ObjectTypeEnum
	kPartsListRowObject           =117445120  # from enum ObjectTypeEnum
	kPartsListRowsObject          =117444864  # from enum ObjectTypeEnum
	kPartsListStyleObject         =117493760  # from enum ObjectTypeEnum
	kPartsListStylesEnumeratorObject=117493504  # from enum ObjectTypeEnum
	kPartsListsObject             =117443840  # from enum ObjectTypeEnum
	kPathAndGuideRailSweepDefObject=83974144   # from enum ObjectTypeEnum
	kPathAndGuideSurfaceSweepDefObject=83976704   # from enum ObjectTypeEnum
	kPathAndSectionTwistsSweepDefObject=83990272   # from enum ObjectTypeEnum
	kPathEntityObject             =83942656   # from enum ObjectTypeEnum
	kPathEntityProxyObject        =83942661   # from enum ObjectTypeEnum
	kPathObject                   =83942400   # from enum ObjectTypeEnum
	kPathProxyObject              =83942402   # from enum ObjectTypeEnum
	kPathSweepDefObject           =83973888   # from enum ObjectTypeEnum
	kPatternConstraintObject      =83905024   # from enum ObjectTypeEnum
	kPatternConstraintProxyObject =83905136   # from enum ObjectTypeEnum
	kPerpendicularConstraint3DObject=83965440   # from enum ObjectTypeEnum
	kPerpendicularConstraint3DProxyObject=83965552   # from enum ObjectTypeEnum
	kPerpendicularConstraintObject=83903232   # from enum ObjectTypeEnum
	kPerpendicularConstraintProxyObject=83903344   # from enum ObjectTypeEnum
	kPitchAndHeightCoilExtentObject=83931904   # from enum ObjectTypeEnum
	kPitchAndRevolutionCoilExtentObject=83931392   # from enum ObjectTypeEnum
	kPlanarMoveDefinitionObject   =84012288   # from enum ObjectTypeEnum
	kPlanarSketchObject           =83924736   # from enum ObjectTypeEnum
	kPlanarSketchProxyObject      =83924848   # from enum ObjectTypeEnum
	kPlanarSketchesObject         =83895296   # from enum ObjectTypeEnum
	kPlaneAndOffsetWorkPlaneDefObject=83889408   # from enum ObjectTypeEnum
	kPlaneAndPointWorkPlaneDefObject=83888896   # from enum ObjectTypeEnum
	kPlaneAndTangentWorkPlaneDefObject=83889920   # from enum ObjectTypeEnum
	kPointAndPlaneDistanceDimConstraint3DObject=83971584   # from enum ObjectTypeEnum
	kPointAndPlaneDistanceDimConstraint3DProxyObject=83971696   # from enum ObjectTypeEnum
	kPointAndPlaneWorkAxisDefObject=83892480   # from enum ObjectTypeEnum
	kPointAndTangentWorkPlaneDefObject=83968512   # from enum ObjectTypeEnum
	kPointCloudCropObject         =84038144   # from enum ObjectTypeEnum
	kPointCloudCropsObject        =84037888   # from enum ObjectTypeEnum
	kPointCloudObject             =84017408   # from enum ObjectTypeEnum
	kPointCloudPlaneObject        =84032000   # from enum ObjectTypeEnum
	kPointCloudPlaneProxyObject   =84032112   # from enum ObjectTypeEnum
	kPointCloudPointObject        =84017664   # from enum ObjectTypeEnum
	kPointCloudPointProxyObject   =84017776   # from enum ObjectTypeEnum
	kPointCloudProxyObject        =84017520   # from enum ObjectTypeEnum
	kPointCloudRegionObject       =84037120   # from enum ObjectTypeEnum
	kPointCloudRegionsObject      =84036864   # from enum ObjectTypeEnum
	kPointCloudScanObject         =84037632   # from enum ObjectTypeEnum
	kPointCloudScansObject        =84037376   # from enum ObjectTypeEnum
	kPointCloudsObject            =84036608   # from enum ObjectTypeEnum
	kPointGraphicsObject          =50358528   # from enum ObjectTypeEnum
	kPointHolePlacementDefinitionObject=83967488   # from enum ObjectTypeEnum
	kPointInferenceObject         =67129088   # from enum ObjectTypeEnum
	kPointInferenceObjectEnumerator=67129344   # from enum ObjectTypeEnum
	kPointToPointRipTypeDefObject =151023104  # from enum ObjectTypeEnum
	kPointWorkPointDefObject      =83894528   # from enum ObjectTypeEnum
	kPositionalRepresentationObject=100678912  # from enum ObjectTypeEnum
	kPositionalRepresentationsObject=100678656  # from enum ObjectTypeEnum
	kPreparationsObject           =100699136  # from enum ObjectTypeEnum
	kPresentationOptionsObject    =50434304   # from enum ObjectTypeEnum
	kPrintManagerObject           =50351360   # from enum ObjectTypeEnum
	kProfile3DObject              =83950080   # from enum ObjectTypeEnum
	kProfile3DProxyObject         =83950192   # from enum ObjectTypeEnum
	kProfileEntity3DObject        =83950592   # from enum ObjectTypeEnum
	kProfileEntity3DProxyObject   =83950704   # from enum ObjectTypeEnum
	kProfileEntityObject          =83908608   # from enum ObjectTypeEnum
	kProfileEntityProxyObject     =83908720   # from enum ObjectTypeEnum
	kProfileObject                =83898624   # from enum ObjectTypeEnum
	kProfilePath3DObject          =83950336   # from enum ObjectTypeEnum
	kProfilePath3DProxyObject     =83950448   # from enum ObjectTypeEnum
	kProfilePathObject            =83908352   # from enum ObjectTypeEnum
	kProfilePathProxyObject       =83908464   # from enum ObjectTypeEnum
	kProfileProxyObject           =83898736   # from enum ObjectTypeEnum
	kProfiles3DObject             =83949824   # from enum ObjectTypeEnum
	kProfilesObject               =83908864   # from enum ObjectTypeEnum
	kProgressBarObject            =50419968   # from enum ObjectTypeEnum
	kProgressiveToolTipObject     =50433536   # from enum ObjectTypeEnum
	kProjectAssetLibrariesObject  =50452736   # from enum ObjectTypeEnum
	kProjectAssetLibraryObject    =50452992   # from enum ObjectTypeEnum
	kProjectOptionsButtonObject   =50445056   # from enum ObjectTypeEnum
	kProjectPathObject            =50432256   # from enum ObjectTypeEnum
	kProjectPathsObject           =50432000   # from enum ObjectTypeEnum
	kProjectedCutObject           =84005632   # from enum ObjectTypeEnum
	kProjectedCutProxyObject      =84005888   # from enum ObjectTypeEnum
	kProjectedCutsObject          =84005376   # from enum ObjectTypeEnum
	kPropertyObject               =50339072   # from enum ObjectTypeEnum
	kPropertySetObject            =50338560   # from enum ObjectTypeEnum
	kPropertySetsObject           =50338304   # from enum ObjectTypeEnum
	kPunchNoteObject              =117488128  # from enum ObjectTypeEnum
	kPunchNotesObject             =117491200  # from enum ObjectTypeEnum
	kPunchToolFeatureObject       =151002368  # from enum ObjectTypeEnum
	kPunchToolFeatureProxyObject  =151005440  # from enum ObjectTypeEnum
	kPunchToolFeaturesObject      =151002112  # from enum ObjectTypeEnum
	kQueryManagerObject           =50410752   # from enum ObjectTypeEnum
	kRadialMarkingMenuObject      =50441984   # from enum ObjectTypeEnum
	kRadialMarkingMenusObject     =50446592   # from enum ObjectTypeEnum
	kRadiusDimConstraint3DObject  =84008704   # from enum ObjectTypeEnum
	kRadiusDimConstraint3DProxyObject=84008816   # from enum ObjectTypeEnum
	kRadiusDimConstraintObject    =83906816   # from enum ObjectTypeEnum
	kRadiusDimConstraintProxyObject=83906928   # from enum ObjectTypeEnum
	kRadiusGeneralDimensionObject =117475072  # from enum ObjectTypeEnum
	kRadiusModelDimensionDefinitionObject=84025856   # from enum ObjectTypeEnum
	kRadiusModelDimensionObject   =84023040   # from enum ObjectTypeEnum
	kRadiusModelDimensionsObject  =84022272   # from enum ObjectTypeEnum
	kRectangularOccurrencePatternObject=100669440  # from enum ObjectTypeEnum
	kRectangularOccurrencePatternProxyObject=100669568  # from enum ObjectTypeEnum
	kRectangularPatternFeatureObject=83913728   # from enum ObjectTypeEnum
	kRectangularPatternFeatureProxyObject=83959808   # from enum ObjectTypeEnum
	kRectangularPatternFeaturesObject=83913984   # from enum ObjectTypeEnum
	kReferenceAssetValueObject    =50452224   # from enum ObjectTypeEnum
	kReferenceComponentObject     =83929856   # from enum ObjectTypeEnum
	kReferenceComponentsObject    =83932672   # from enum ObjectTypeEnum
	kReferenceFeatureObject       =83921152   # from enum ObjectTypeEnum
	kReferenceFeatureProxyObject  =83962368   # from enum ObjectTypeEnum
	kReferenceFeaturesEnumeratorObject=83934720   # from enum ObjectTypeEnum
	kReferenceFeaturesObject      =83923456   # from enum ObjectTypeEnum
	kReferenceKeyEventsObject     =50443008   # from enum ObjectTypeEnum
	kReferenceKeyManagerObject    =67128576   # from enum ObjectTypeEnum
	kReferenceParameterObject     =50348800   # from enum ObjectTypeEnum
	kReferenceParametersObject    =50347520   # from enum ObjectTypeEnum
	kReferencedFileDescriptorObject=50337536   # from enum ObjectTypeEnum
	kReferencedFileDescriptorsObject=50337792   # from enum ObjectTypeEnum
	kReferencedOLEFileDescriptorObject=50342400   # from enum ObjectTypeEnum
	kReferencedOLEFileDescriptorsObject=50342656   # from enum ObjectTypeEnum
	kRefoldFeatureObject          =151017216  # from enum ObjectTypeEnum
	kRefoldFeatureProxyObject     =151017728  # from enum ObjectTypeEnum
	kRefoldFeaturesObject         =151017472  # from enum ObjectTypeEnum
	kRegionPropertiesObject       =83992064   # from enum ObjectTypeEnum
	kRenderStyleObject            =50359296   # from enum ObjectTypeEnum
	kRenderStylesObject           =50359040   # from enum ObjectTypeEnum
	kReplaceFaceFeatureObject     =83954688   # from enum ObjectTypeEnum
	kReplaceFaceFeatureProxyObject=83960576   # from enum ObjectTypeEnum
	kReplaceFaceFeaturesObject    =83954944   # from enum ObjectTypeEnum
	kRepresentationEventsObject   =50411264   # from enum ObjectTypeEnum
	kRepresentationsManagerObject =100678400  # from enum ObjectTypeEnum
	kRestFeatureObject            =84003840   # from enum ObjectTypeEnum
	kRestFeatureProxyObject       =84003952   # from enum ObjectTypeEnum
	kRestFeaturesObject           =84004096   # from enum ObjectTypeEnum
	kRevisionTableCellObject      =117469440  # from enum ObjectTypeEnum
	kRevisionTableColumnObject    =117467136  # from enum ObjectTypeEnum
	kRevisionTableColumnsObject   =117466880  # from enum ObjectTypeEnum
	kRevisionTableObject          =117466624  # from enum ObjectTypeEnum
	kRevisionTableRowObject       =117469184  # from enum ObjectTypeEnum
	kRevisionTableRowsObject      =117467392  # from enum ObjectTypeEnum
	kRevisionTableStyleObject     =117494272  # from enum ObjectTypeEnum
	kRevisionTableStylesEnumeratorObject=117494016  # from enum ObjectTypeEnum
	kRevisionTablesObject         =117466368  # from enum ObjectTypeEnum
	kRevolutionAndHeightCoilExtentObject=83931648   # from enum ObjectTypeEnum
	kRevolveFeatureObject         =83914240   # from enum ObjectTypeEnum
	kRevolveFeatureProxyObject    =83960064   # from enum ObjectTypeEnum
	kRevolveFeaturesObject        =83914496   # from enum ObjectTypeEnum
	kRevolvedFaceWorkAxisDefObject=83892224   # from enum ObjectTypeEnum
	kRibDefinitionObject          =84013312   # from enum ObjectTypeEnum
	kRibFeatureObject             =83914752   # from enum ObjectTypeEnum
	kRibFeatureProxyObject        =83960320   # from enum ObjectTypeEnum
	kRibFeaturesObject            =83915008   # from enum ObjectTypeEnum
	kRibbonObject                 =50424320   # from enum ObjectTypeEnum
	kRibbonPanelObject            =50425344   # from enum ObjectTypeEnum
	kRibbonPanelsObject           =50425088   # from enum ObjectTypeEnum
	kRibbonTabObject              =50424832   # from enum ObjectTypeEnum
	kRibbonTabsObject             =50424576   # from enum ObjectTypeEnum
	kRibbonsObject                =50424064   # from enum ObjectTypeEnum
	kRigidBodyGroupObject         =100690432  # from enum ObjectTypeEnum
	kRigidBodyGroupsObject        =100686336  # from enum ObjectTypeEnum
	kRigidBodyJointObject         =100698624  # from enum ObjectTypeEnum
	kRigidBodyJointsObject        =100694528  # from enum ObjectTypeEnum
	kRigidBodyResultsObject       =100682240  # from enum ObjectTypeEnum
	kRipDefinitionObject          =151022592  # from enum ObjectTypeEnum
	kRipFeatureObject             =151020032  # from enum ObjectTypeEnum
	kRipFeatureProxyObject        =151020288  # from enum ObjectTypeEnum
	kRipFeaturesObject            =151020544  # from enum ObjectTypeEnum
	kRolledHemDefinitionObject    =151015168  # from enum ObjectTypeEnum
	kRotateAboutLineMoveOperationObject=84015616   # from enum ObjectTypeEnum
	kRotateRotateConstraintObject =100666624  # from enum ObjectTypeEnum
	kRotateRotateConstraintProxyObject=100676608  # from enum ObjectTypeEnum
	kRotateRotateiMateDefinitionObject=83948032   # from enum ObjectTypeEnum
	kRotateRotateiMateDefinitionProxyObject=83948160   # from enum ObjectTypeEnum
	kRotateTranslateConstraintObject=100666880  # from enum ObjectTypeEnum
	kRotateTranslateConstraintProxyObject=100676864  # from enum ObjectTypeEnum
	kRotateTranslateiMateDefinitionObject=83948288   # from enum ObjectTypeEnum
	kRotateTranslateiMateDefinitionProxyObject=83948416   # from enum ObjectTypeEnum
	kRowObject                    =117462272  # from enum ObjectTypeEnum
	kRowsObject                   =117462016  # from enum ObjectTypeEnum
	kRuleFilletFeatureObject      =84004352   # from enum ObjectTypeEnum
	kRuleFilletFeatureProxyObject =84004464   # from enum ObjectTypeEnum
	kRuleFilletFeaturesObject     =84004608   # from enum ObjectTypeEnum
	kRuledSurfaceDefinitionObject =84050176   # from enum ObjectTypeEnum
	kRuledSurfaceFeatureObject    =84050432   # from enum ObjectTypeEnum
	kRuledSurfaceFeatureProxyObject=84050944   # from enum ObjectTypeEnum
	kRuledSurfaceFeaturesObject   =84050688   # from enum ObjectTypeEnum
	kSaveOptionsObject            =50408960   # from enum ObjectTypeEnum
	kSculptFeatureObject          =83969792   # from enum ObjectTypeEnum
	kSculptFeatureProxyObject     =83970304   # from enum ObjectTypeEnum
	kSculptFeaturesObject         =83970048   # from enum ObjectTypeEnum
	kSculptSurfaceObject          =83976960   # from enum ObjectTypeEnum
	kSectionDrawingViewObject     =117463296  # from enum ObjectTypeEnum
	kSelectEventsObject           =50353408   # from enum ObjectTypeEnum
	kSelectSetObject              =50366464   # from enum ObjectTypeEnum
	kSelectionPreferencesObject   =50454016   # from enum ObjectTypeEnum
	kShadedDisplayOptionsObject   =50413056   # from enum ObjectTypeEnum
	kSheetFormatObject            =117482496  # from enum ObjectTypeEnum
	kSheetFormatsObject           =117482240  # from enum ObjectTypeEnum
	kSheetMetalComponentDefinitionObject=150995200  # from enum ObjectTypeEnum
	kSheetMetalFeaturesObject     =150995456  # from enum ObjectTypeEnum
	kSheetMetalStyleObject        =150995968  # from enum ObjectTypeEnum
	kSheetMetalStylesObject       =150995712  # from enum ObjectTypeEnum
	kSheetObject                  =117441280  # from enum ObjectTypeEnum
	kSheetSettingsObject          =50408448   # from enum ObjectTypeEnum
	kSheetsObject                 =117442560  # from enum ObjectTypeEnum
	kShellDefinitionObject        =83963136   # from enum ObjectTypeEnum
	kShellFeatureObject           =83915264   # from enum ObjectTypeEnum
	kShellFeatureProxyObject      =83960832   # from enum ObjectTypeEnum
	kShellFeaturesObject          =83915520   # from enum ObjectTypeEnum
	kShellThicknessFaceSetObject  =83963392   # from enum ObjectTypeEnum
	kSilhouetteCurveObject        =84012800   # from enum ObjectTypeEnum
	kSilhouetteCurveProxyObject   =84012929   # from enum ObjectTypeEnum
	kSilhouetteCurvesObject       =84013056   # from enum ObjectTypeEnum
	kSimulationComponentObject    =100700416  # from enum ObjectTypeEnum
	kSimulationManagerObject      =100701440  # from enum ObjectTypeEnum
	kSingleHemDefinitionObject    =151014656  # from enum ObjectTypeEnum
	kSinglePointRipTypeDefObject  =151022848  # from enum ObjectTypeEnum
	kSketch3DObject               =83936256   # from enum ObjectTypeEnum
	kSketch3DOptionsObject        =50405888   # from enum ObjectTypeEnum
	kSketch3DProxyObject          =83936368   # from enum ObjectTypeEnum
	kSketch3DSettingsObject       =50383616   # from enum ObjectTypeEnum
	kSketchArc3DObject            =83938304   # from enum ObjectTypeEnum
	kSketchArc3DProxyObject       =83938416   # from enum ObjectTypeEnum
	kSketchArcObject              =83898880   # from enum ObjectTypeEnum
	kSketchArcProxyObject         =83898992   # from enum ObjectTypeEnum
	kSketchArcs3DObject           =83938560   # from enum ObjectTypeEnum
	kSketchArcsObject             =83897344   # from enum ObjectTypeEnum
	kSketchBlockDefinitionObject  =84006400   # from enum ObjectTypeEnum
	kSketchBlockDefinitionProxyObject=84006512   # from enum ObjectTypeEnum
	kSketchBlockDefinitionsEnumeratorObject=84007424   # from enum ObjectTypeEnum
	kSketchBlockDefinitionsObject =84006144   # from enum ObjectTypeEnum
	kSketchBlockObject            =84006912   # from enum ObjectTypeEnum
	kSketchBlockProxyObject       =84007024   # from enum ObjectTypeEnum
	kSketchBlocksEnumeratorObject =84007168   # from enum ObjectTypeEnum
	kSketchBlocksObject           =84006656   # from enum ObjectTypeEnum
	kSketchCircle3DObject         =83939840   # from enum ObjectTypeEnum
	kSketchCircle3DProxyObject    =83939952   # from enum ObjectTypeEnum
	kSketchCircleObject           =83899648   # from enum ObjectTypeEnum
	kSketchCircleProxyObject      =83899760   # from enum ObjectTypeEnum
	kSketchCircles3DObject        =83940864   # from enum ObjectTypeEnum
	kSketchCirclesObject          =83898368   # from enum ObjectTypeEnum
	kSketchConstraintSettingsObject=50453760   # from enum ObjectTypeEnum
	kSketchConstraints3dEnumeratorObject=83941120   # from enum ObjectTypeEnum
	kSketchConstraintsEnumeratorObject=83897088   # from enum ObjectTypeEnum
	kSketchControlPointSpline3DObject=84018432   # from enum ObjectTypeEnum
	kSketchControlPointSpline3DProxyObject=84018544   # from enum ObjectTypeEnum
	kSketchControlPointSplineObject=84017920   # from enum ObjectTypeEnum
	kSketchControlPointSplineProxyObject=84018032   # from enum ObjectTypeEnum
	kSketchControlPointSplines3DObject=84018688   # from enum ObjectTypeEnum
	kSketchControlPointSplinesObject=84018176   # from enum ObjectTypeEnum
	kSketchEllipse3DObject        =83939328   # from enum ObjectTypeEnum
	kSketchEllipse3DProxyObject   =83939440   # from enum ObjectTypeEnum
	kSketchEllipseObject          =83899392   # from enum ObjectTypeEnum
	kSketchEllipseProxyObject     =83899504   # from enum ObjectTypeEnum
	kSketchEllipses3DObject       =83940352   # from enum ObjectTypeEnum
	kSketchEllipsesObject         =83898112   # from enum ObjectTypeEnum
	kSketchEllipticalArc3DObject  =83939584   # from enum ObjectTypeEnum
	kSketchEllipticalArc3DProxyObject=83939696   # from enum ObjectTypeEnum
	kSketchEllipticalArcObject    =83904768   # from enum ObjectTypeEnum
	kSketchEllipticalArcProxyObject=83904880   # from enum ObjectTypeEnum
	kSketchEllipticalArcs3DObject =83940608   # from enum ObjectTypeEnum
	kSketchEllipticalArcsObject   =83904512   # from enum ObjectTypeEnum
	kSketchEntities3DEnumeratorObject=83937024   # from enum ObjectTypeEnum
	kSketchEntitiesEnumeratorObject=83908096   # from enum ObjectTypeEnum
	kSketchEquationCurve3DObject  =84019456   # from enum ObjectTypeEnum
	kSketchEquationCurve3DProxyObject=84019568   # from enum ObjectTypeEnum
	kSketchEquationCurveObject    =84018944   # from enum ObjectTypeEnum
	kSketchEquationCurveProxyObject=84019056   # from enum ObjectTypeEnum
	kSketchEquationCurves3DObject =84019712   # from enum ObjectTypeEnum
	kSketchEquationCurvesObject   =84019200   # from enum ObjectTypeEnum
	kSketchEventsObject           =50411008   # from enum ObjectTypeEnum
	kSketchFillRegion             =83969280   # from enum ObjectTypeEnum
	kSketchFillRegions            =83969024   # from enum ObjectTypeEnum
	kSketchFixedSpline3DObject    =83964416   # from enum ObjectTypeEnum
	kSketchFixedSpline3DProxyObject=83964528   # from enum ObjectTypeEnum
	kSketchFixedSplineObject      =83963904   # from enum ObjectTypeEnum
	kSketchFixedSplineProxyObject =83964016   # from enum ObjectTypeEnum
	kSketchFixedSplines3DObject   =83964160   # from enum ObjectTypeEnum
	kSketchFixedSplinesObject     =83963648   # from enum ObjectTypeEnum
	kSketchHolePlacementDefinitionObject=83966720   # from enum ObjectTypeEnum
	kSketchImageObject            =83972352   # from enum ObjectTypeEnum
	kSketchImageProxyObject       =83972368   # from enum ObjectTypeEnum
	kSketchImagesObject           =83972096   # from enum ObjectTypeEnum
	kSketchLine3DObject           =83937280   # from enum ObjectTypeEnum
	kSketchLine3DProxyObject      =83937392   # from enum ObjectTypeEnum
	kSketchLineObject             =83896064   # from enum ObjectTypeEnum
	kSketchLineProxyObject        =83896176   # from enum ObjectTypeEnum
	kSketchLines3DObject          =83937536   # from enum ObjectTypeEnum
	kSketchLinesObject            =83896320   # from enum ObjectTypeEnum
	kSketchOffsetSplineObject     =83962624   # from enum ObjectTypeEnum
	kSketchOffsetSplineProxyObject=83962736   # from enum ObjectTypeEnum
	kSketchOffsetSplinesObject    =83962880   # from enum ObjectTypeEnum
	kSketchOptionsObject          =50400000   # from enum ObjectTypeEnum
	kSketchPoint3DObject          =83937792   # from enum ObjectTypeEnum
	kSketchPoint3DProxyObject     =83937904   # from enum ObjectTypeEnum
	kSketchPointObject            =83896576   # from enum ObjectTypeEnum
	kSketchPointProxyObject       =83896688   # from enum ObjectTypeEnum
	kSketchPoints3DObject         =83938048   # from enum ObjectTypeEnum
	kSketchPointsObject           =83896832   # from enum ObjectTypeEnum
	kSketchSettingsObject         =50383360   # from enum ObjectTypeEnum
	kSketchSpline3DObject         =83939072   # from enum ObjectTypeEnum
	kSketchSpline3DProxyObject    =83939184   # from enum ObjectTypeEnum
	kSketchSplineHandle3DObject   =83980032   # from enum ObjectTypeEnum
	kSketchSplineHandle3DProxyObject=83980144   # from enum ObjectTypeEnum
	kSketchSplineHandleObject     =83984128   # from enum ObjectTypeEnum
	kSketchSplineHandleProxyObject=83984240   # from enum ObjectTypeEnum
	kSketchSplineObject           =83899136   # from enum ObjectTypeEnum
	kSketchSplineProxyObject      =83899248   # from enum ObjectTypeEnum
	kSketchSplines3DObject        =83940096   # from enum ObjectTypeEnum
	kSketchSplinesObject          =83897856   # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionLibrariesObject=117496320  # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionLibraryObject=117496576  # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionObject=117448448  # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionsObject=117448192  # from enum ObjectTypeEnum
	kSketchedSymbolObject         =117448704  # from enum ObjectTypeEnum
	kSketchedSymbolsObject        =117449472  # from enum ObjectTypeEnum
	kSketches3DEnumeratorObject   =83997696   # from enum ObjectTypeEnum
	kSketches3DObject             =83936512   # from enum ObjectTypeEnum
	kSketchesEnumeratorObject     =83932416   # from enum ObjectTypeEnum
	kSmoothConstraint3DObject     =83977728   # from enum ObjectTypeEnum
	kSmoothConstraint3DProxyObject=83977840   # from enum ObjectTypeEnum
	kSmoothConstraintObject       =83973376   # from enum ObjectTypeEnum
	kSmoothConstraintProxyObject  =83973488   # from enum ObjectTypeEnum
	kSnapFitFeatureObject         =84004864   # from enum ObjectTypeEnum
	kSnapFitFeatureProxyObject    =84004976   # from enum ObjectTypeEnum
	kSnapFitFeaturesObject        =84005120   # from enum ObjectTypeEnum
	kSoftwareVersionObject        =50345728   # from enum ObjectTypeEnum
	kSphereCenterPointWorkPointDefObject=84027392   # from enum ObjectTypeEnum
	kSpiralCoilExtentObject       =83932160   # from enum ObjectTypeEnum
	kSplineFitPointConstraintObject=83900928   # from enum ObjectTypeEnum
	kSplineFitPointConstraintProxyObject=83901040   # from enum ObjectTypeEnum
	kSplineFitPointsConstraint3DObject=83955712   # from enum ObjectTypeEnum
	kSplineFitPointsConstraint3DProxyObject=83955824   # from enum ObjectTypeEnum
	kSplitFeatureObject           =83915776   # from enum ObjectTypeEnum
	kSplitFeatureProxyObject      =83961088   # from enum ObjectTypeEnum
	kSplitFeaturesObject          =83916032   # from enum ObjectTypeEnum
	kStandardThreadInfoObject     =83920128   # from enum ObjectTypeEnum
	kStringAssetValueObject       =50451712   # from enum ObjectTypeEnum
	kStyleEventsObject            =50414336   # from enum ObjectTypeEnum
	kStyleObject                  =117478400  # from enum ObjectTypeEnum
	kStylesManagerObject          =50426112   # from enum ObjectTypeEnum
	kStylesObject                 =117478656  # from enum ObjectTypeEnum
	kSurfaceBodiesObject          =67121456   # from enum ObjectTypeEnum
	kSurfaceBodyDefinitionObject  =50435072   # from enum ObjectTypeEnum
	kSurfaceBodyObject            =67118896   # from enum ObjectTypeEnum
	kSurfaceBodyProxyObject       =67119008   # from enum ObjectTypeEnum
	kSurfaceGraphicsEdgeListObject=50418944   # from enum ObjectTypeEnum
	kSurfaceGraphicsEdgeObject    =50419200   # from enum ObjectTypeEnum
	kSurfaceGraphicsFaceListObject=50418432   # from enum ObjectTypeEnum
	kSurfaceGraphicsFaceObject    =50418688   # from enum ObjectTypeEnum
	kSurfaceGraphicsObject        =50417920   # from enum ObjectTypeEnum
	kSurfaceGraphicsVertexListObject=50447104   # from enum ObjectTypeEnum
	kSurfaceGraphicsVertexObject  =50447360   # from enum ObjectTypeEnum
	kSurfaceTextureANSIDefinitionObject=117497088  # from enum ObjectTypeEnum
	kSurfaceTextureBSIDefinitionObject=117497344  # from enum ObjectTypeEnum
	kSurfaceTextureDINDefinitionObject=117497600  # from enum ObjectTypeEnum
	kSurfaceTextureGBDefinitionObject=117497856  # from enum ObjectTypeEnum
	kSurfaceTextureGOSTDefinitionObject=117498112  # from enum ObjectTypeEnum
	kSurfaceTextureISODefinitionObject=117498368  # from enum ObjectTypeEnum
	kSurfaceTextureJISDefinitionObject=117498624  # from enum ObjectTypeEnum
	kSurfaceTextureStyleObject    =117481984  # from enum ObjectTypeEnum
	kSurfaceTextureStylesEnumeratorObject=117481728  # from enum ObjectTypeEnum
	kSurfaceTextureSymbolDefinitionObject=117496832  # from enum ObjectTypeEnum
	kSurfaceTextureSymbolObject   =117484032  # from enum ObjectTypeEnum
	kSurfaceTextureSymbolsObject  =117483776  # from enum ObjectTypeEnum
	kSweepDefinitionObject        =83973632   # from enum ObjectTypeEnum
	kSweepFeatureObject           =83916288   # from enum ObjectTypeEnum
	kSweepFeatureProxyObject      =83961344   # from enum ObjectTypeEnum
	kSweepFeaturesObject          =83916544   # from enum ObjectTypeEnum
	kSweepGraphicsObject          =50414080   # from enum ObjectTypeEnum
	kSymmetryConstraintObject     =83903488   # from enum ObjectTypeEnum
	kSymmetryConstraintProxyObject=83903600   # from enum ObjectTypeEnum
	kTableFormatObject            =117465088  # from enum ObjectTypeEnum
	kTableParameterObject         =50349312   # from enum ObjectTypeEnum
	kTableParametersObject        =50348032   # from enum ObjectTypeEnum
	kTableStyleObject             =117494784  # from enum ObjectTypeEnum
	kTableStylesEnumeratorObject  =117494528  # from enum ObjectTypeEnum
	kTangentConstraint3DObject    =83955968   # from enum ObjectTypeEnum
	kTangentConstraint3DProxyObject=83956080   # from enum ObjectTypeEnum
	kTangentConstraintObject      =100665600  # from enum ObjectTypeEnum
	kTangentConstraintProxyObject =100677120  # from enum ObjectTypeEnum
	kTangentDistanceDimConstraintObject=83907072   # from enum ObjectTypeEnum
	kTangentDistanceDimConstraintProxyObject=83907184   # from enum ObjectTypeEnum
	kTangentSketchConstraintObject=83903744   # from enum ObjectTypeEnum
	kTangentSketchConstraintProxyObject=83903856   # from enum ObjectTypeEnum
	kTangentiMateDefinitionObject =83948544   # from enum ObjectTypeEnum
	kTangentiMateDefinitionProxyObject=83948672   # from enum ObjectTypeEnum
	kTaperedThreadInfoObject      =83920640   # from enum ObjectTypeEnum
	kTeardropHemDefinitionObject  =151014912  # from enum ObjectTypeEnum
	kTextBoxConstraintObject      =83972864   # from enum ObjectTypeEnum
	kTextBoxConstraintProxyObject =83972976   # from enum ObjectTypeEnum
	kTextBoxObject                =117445888  # from enum ObjectTypeEnum
	kTextBoxesObject              =117445632  # from enum ObjectTypeEnum
	kTextGraphicsObject           =50358784   # from enum ObjectTypeEnum
	kTextStyleObject              =117447936  # from enum ObjectTypeEnum
	kTextStylesEnumeratorObject   =117465600  # from enum ObjectTypeEnum
	kTextStylesObject             =117447680  # from enum ObjectTypeEnum
	kTextureAssetValueObject      =50451456   # from enum ObjectTypeEnum
	kTextureCoordinateSetObject   =50405376   # from enum ObjectTypeEnum
	kTextureMapObject             =50404864   # from enum ObjectTypeEnum
	kTextureMapsObject            =50404608   # from enum ObjectTypeEnum
	kThickenFeatureObject         =83955200   # from enum ObjectTypeEnum
	kThickenFeatureProxyObject    =83961600   # from enum ObjectTypeEnum
	kThickenFeaturesObject        =83955456   # from enum ObjectTypeEnum
	kThreadFeatureObject          =83916800   # from enum ObjectTypeEnum
	kThreadFeatureProxyObject     =83961856   # from enum ObjectTypeEnum
	kThreadFeaturesObject         =83917056   # from enum ObjectTypeEnum
	kThreadInfoObject             =83919872   # from enum ObjectTypeEnum
	kThreadNoteObject             =117487872  # from enum ObjectTypeEnum
	kThreadTableQueryObject       =50411520   # from enum ObjectTypeEnum
	kThreePlanesWorkPointDefObject=83893760   # from enum ObjectTypeEnum
	kThreePointAngleDimConstraintObject=83906304   # from enum ObjectTypeEnum
	kThreePointAngleDimConstraintProxyObject=83906416   # from enum ObjectTypeEnum
	kThreePointsWorkPlaneDefObject=83888128   # from enum ObjectTypeEnum
	kThroughAllExtentObject       =83919616   # from enum ObjectTypeEnum
	kTitleBlockDefinitionObject   =117447168  # from enum ObjectTypeEnum
	kTitleBlockDefinitionsObject  =117446912  # from enum ObjectTypeEnum
	kTitleBlockObject             =117447424  # from enum ObjectTypeEnum
	kToExtentObject               =83918848   # from enum ObjectTypeEnum
	kToHeightExtentObject         =83996160   # from enum ObjectTypeEnum
	kToNextExtentObject           =83919104   # from enum ObjectTypeEnum
	kToleranceObject              =50377984   # from enum ObjectTypeEnum
	kTorusCenterPointWorkPointDefObject=83990784   # from enum ObjectTypeEnum
	kTorusMidPlaneWorkPlaneDefObject=83990528   # from enum ObjectTypeEnum
	kTrailObject                  =134219264  # from enum ObjectTypeEnum
	kTrailSegmentObject           =134219520  # from enum ObjectTypeEnum
	kTrailsEnumeratorObject       =134219008  # from enum ObjectTypeEnum
	kTransactionEventsObject      =50342144   # from enum ObjectTypeEnum
	kTransactionManagerObject     =50341376   # from enum ObjectTypeEnum
	kTransactionObject            =50341632   # from enum ObjectTypeEnum
	kTransactionsEnumeratorObject =50341888   # from enum ObjectTypeEnum
	kTransientGeometryObject      =67126912   # from enum ObjectTypeEnum
	kTransitionalConstraintObject =100666112  # from enum ObjectTypeEnum
	kTransitionalConstraintProxyObject=100677376  # from enum ObjectTypeEnum
	kTranslateTranslateConstraintObject=100667136  # from enum ObjectTypeEnum
	kTranslateTranslateConstraintProxyObject=100677888  # from enum ObjectTypeEnum
	kTranslatorAddInObject        =50343936   # from enum ObjectTypeEnum
	kTriadEventsObject            =50392064   # from enum ObjectTypeEnum
	kTriangleFanGraphicsObject    =50358272   # from enum ObjectTypeEnum
	kTriangleGraphicsObject       =50357760   # from enum ObjectTypeEnum
	kTriangleStripGraphicsObject  =50358016   # from enum ObjectTypeEnum
	kTrimFeatureObject            =83974400   # from enum ObjectTypeEnum
	kTrimFeatureProxyObject       =83976448   # from enum ObjectTypeEnum
	kTrimFeaturesObject           =83976192   # from enum ObjectTypeEnum
	kTutorialsManagerObject       =50454528   # from enum ObjectTypeEnum
	kTwoDistancesChamferDefObject =83926016   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraint3DObject=83971072   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraint3DProxyObject=83971184   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraintObject=83906048   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraintProxyObject=83906160   # from enum ObjectTypeEnum
	kTwoLinesWorkPlaneDefObject   =83888384   # from enum ObjectTypeEnum
	kTwoLinesWorkPointDefObject   =83894016   # from enum ObjectTypeEnum
	kTwoPlanesWorkAxisDefObject   =83891712   # from enum ObjectTypeEnum
	kTwoPlanesWorkPlaneDefObject  =83951872   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraint3DObject=83971328   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraint3DProxyObject=83971440   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraintObject=83905792   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraintProxyObject=83905904   # from enum ObjectTypeEnum
	kTwoPointsWorkAxisDefObject   =83891968   # from enum ObjectTypeEnum
	kUnfoldFeatureObject          =151016448  # from enum ObjectTypeEnum
	kUnfoldFeatureProxyObject     =151016960  # from enum ObjectTypeEnum
	kUnfoldFeaturesObject         =151016704  # from enum ObjectTypeEnum
	kUnfoldMethodObject           =150996480  # from enum ObjectTypeEnum
	kUnfoldMethodsObject          =150996224  # from enum ObjectTypeEnum
	kUnitAttributesObject         =117499904  # from enum ObjectTypeEnum
	kUnitsOfMeasureObject         =50346240   # from enum ObjectTypeEnum
	kUnknownObject                =2130706483 # from enum ObjectTypeEnum
	kUserCoordinateSystemDefinitionObject=84010752   # from enum ObjectTypeEnum
	kUserCoordinateSystemObject   =84008192   # from enum ObjectTypeEnum
	kUserCoordinateSystemProxyObject=84008352   # from enum ObjectTypeEnum
	kUserCoordinateSystemSettingsObject=50431232   # from enum ObjectTypeEnum
	kUserCoordinateSystemsObject  =84008448   # from enum ObjectTypeEnum
	kUserInputEventsObject        =50340352   # from enum ObjectTypeEnum
	kUserInterfaceEventsObject    =50402816   # from enum ObjectTypeEnum
	kUserInterfaceManagerObject   =50388224   # from enum ObjectTypeEnum
	kUserParameterObject          =50349056   # from enum ObjectTypeEnum
	kUserParametersObject         =50347776   # from enum ObjectTypeEnum
	kVertexDefinitionObject       =50430464   # from enum ObjectTypeEnum
	kVertexDefinitionsObject      =50430208   # from enum ObjectTypeEnum
	kVertexObject                 =67120432   # from enum ObjectTypeEnum
	kVertexProxyObject            =67120544   # from enum ObjectTypeEnum
	kVerticalAlignConstraintObject=83904256   # from enum ObjectTypeEnum
	kVerticalAlignConstraintProxyObject=83904368   # from enum ObjectTypeEnum
	kVerticalConstraintObject     =83904000   # from enum ObjectTypeEnum
	kVerticalConstraintProxyObject=83904112   # from enum ObjectTypeEnum
	kVerticesObject               =67122992   # from enum ObjectTypeEnum
	kViewListObject               =50389760   # from enum ObjectTypeEnum
	kViewObject                   =50332672   # from enum ObjectTypeEnum
	kViewsEnumeratorObject        =50350080   # from enum ObjectTypeEnum
	kViewsObject                  =50332928   # from enum ObjectTypeEnum
	kVirtualComponentDefinitionObject=100675072  # from enum ObjectTypeEnum
	kVisibleOccurrenceFinderObject=100704768  # from enum ObjectTypeEnum
	kWebBrowserDockableWindowObject=50454272   # from enum ObjectTypeEnum
	kWebViewObject                =50455040   # from enum ObjectTypeEnum
	kWebViewsObject               =50454784   # from enum ObjectTypeEnum
	kWeldBeadObject               =100672768  # from enum ObjectTypeEnum
	kWeldBeadsObject              =100672000  # from enum ObjectTypeEnum
	kWeldObject                   =100672512  # from enum ObjectTypeEnum
	kWeldmentComponentDefinitionObject=100673280  # from enum ObjectTypeEnum
	kWeldsComponentDefinitionObject=100670208  # from enum ObjectTypeEnum
	kWeldsObject                  =100671744  # from enum ObjectTypeEnum
	kWidthOffsetWidthExtentObject =83996928   # from enum ObjectTypeEnum
	kWireDefinitionObject         =50445824   # from enum ObjectTypeEnum
	kWireDefinitionsObject        =50445568   # from enum ObjectTypeEnum
	kWireEdgeDefinitionObject     =50446336   # from enum ObjectTypeEnum
	kWireEdgeDefinitionsObject    =50446080   # from enum ObjectTypeEnum
	kWireObject                   =67131392   # from enum ObjectTypeEnum
	kWireframeDisplayOptionsObject=50412800   # from enum ObjectTypeEnum
	kWiresObject                  =67132160   # from enum ObjectTypeEnum
	kWorkAxesObject               =83890944   # from enum ObjectTypeEnum
	kWorkAxisObject               =83891200   # from enum ObjectTypeEnum
	kWorkAxisProxyObject          =83891360   # from enum ObjectTypeEnum
	kWorkPlaneObject              =83887616   # from enum ObjectTypeEnum
	kWorkPlaneProxyObject         =83887776   # from enum ObjectTypeEnum
	kWorkPlanesObject             =83887872   # from enum ObjectTypeEnum
	kWorkPointObject              =83893504   # from enum ObjectTypeEnum
	kWorkPointProxyObject         =83893664   # from enum ObjectTypeEnum
	kWorkPointsObject             =83893248   # from enum ObjectTypeEnum
	kWorkSurfaceObject            =83945216   # from enum ObjectTypeEnum
	kWorkSurfaceProxyObject       =83945328   # from enum ObjectTypeEnum
	kWorkSurfacesObject           =83945472   # from enum ObjectTypeEnum
	kiAssemblyFactoryObject       =100680960  # from enum ObjectTypeEnum
	kiAssemblyMemberObject        =100680192  # from enum ObjectTypeEnum
	kiAssemblyTableCellObject     =100681216  # from enum ObjectTypeEnum
	kiAssemblyTableColumnObject   =100681728  # from enum ObjectTypeEnum
	kiAssemblyTableColumnsObject  =100681472  # from enum ObjectTypeEnum
	kiAssemblyTableRowObject      =100680704  # from enum ObjectTypeEnum
	kiAssemblyTableRowsObject     =100680448  # from enum ObjectTypeEnum
	kiFeatureComponentObject      =83932928   # from enum ObjectTypeEnum
	kiFeatureComponentsObject     =83933184   # from enum ObjectTypeEnum
	kiFeatureDefinitionObject     =83942912   # from enum ObjectTypeEnum
	kiFeatureEntityInputObject    =83944192   # from enum ObjectTypeEnum
	kiFeatureInputObject          =83943680   # from enum ObjectTypeEnum
	kiFeatureInputsObject         =83943424   # from enum ObjectTypeEnum
	kiFeatureObject               =83998208   # from enum ObjectTypeEnum
	kiFeatureOptionsObject        =50406144   # from enum ObjectTypeEnum
	kiFeatureParameterInputObject =83943936   # from enum ObjectTypeEnum
	kiFeatureProxyObject          =83998320   # from enum ObjectTypeEnum
	kiFeatureSketchPlaneInputObject=83944704   # from enum ObjectTypeEnum
	kiFeatureTableCellObject      =83998464   # from enum ObjectTypeEnum
	kiFeatureTableColumnObject    =83998720   # from enum ObjectTypeEnum
	kiFeatureTableColumnsObject   =83998976   # from enum ObjectTypeEnum
	kiFeatureTableObject          =83999744   # from enum ObjectTypeEnum
	kiFeatureTableRowObject       =83999232   # from enum ObjectTypeEnum
	kiFeatureTableRowsObject      =83999488   # from enum ObjectTypeEnum
	kiFeatureTemplateDescriptorObject=83933952   # from enum ObjectTypeEnum
	kiFeatureTemplateDescriptorsObject=83934208   # from enum ObjectTypeEnum
	kiFeatureVectorInputObject    =83944960   # from enum ObjectTypeEnum
	kiFeatureWorkPlaneInputObject =83944448   # from enum ObjectTypeEnum
	kiFeaturesObject              =83997952   # from enum ObjectTypeEnum
	kiMateDefinitionObject        =83946752   # from enum ObjectTypeEnum
	kiMateDefinitionsEnumeratorObject=83952384   # from enum ObjectTypeEnum
	kiMateDefinitionsObject       =83946496   # from enum ObjectTypeEnum
	kiMateResultObject            =83949312   # from enum ObjectTypeEnum
	kiMateResultProxyObject       =83949321   # from enum ObjectTypeEnum
	kiMateResultsEnumeratorObject =83949568   # from enum ObjectTypeEnum
	kiMateResultsObject           =83949056   # from enum ObjectTypeEnum
	kiPartFactoryObject           =83933440   # from enum ObjectTypeEnum
	kiPartMemberObject            =83933696   # from enum ObjectTypeEnum
	kiPartTableCellObject         =83936000   # from enum ObjectTypeEnum
	kiPartTableColumnObject       =83935232   # from enum ObjectTypeEnum
	kiPartTableColumnsObject      =83934976   # from enum ObjectTypeEnum
	kiPartTableRowObject          =83935744   # from enum ObjectTypeEnum
	kiPartTableRowsObject         =83935488   # from enum ObjectTypeEnum
	kCanIgnoreDegreeOfFreedom     =78082      # from enum OccurrenceDOFStateEnum
	kCanRetainDegreeOfFreedom     =78081      # from enum OccurrenceDOFStateEnum
	kNoDegreeOfFreedomState       =78083      # from enum OccurrenceDOFStateEnum
	kBestImageFidelity            =37380      # from enum OfflineImageFidelityEnum
	kBetterImageFidelity          =37379      # from enum OfflineImageFidelityEnum
	kLowerImageFidelity           =37377      # from enum OfflineImageFidelityEnum
	kStandardImageFidelity        =37378      # from enum OfflineImageFidelityEnum
	kCircularCornerClosure        =96257      # from enum OffsetCornerClosureTypeEnum
	kExtendCornerClosure          =96259      # from enum OffsetCornerClosureTypeEnum
	kLinearCornerClosure          =96258      # from enum OffsetCornerClosureTypeEnum
	kConstrainedOrbit             =86018      # from enum OrbitTypeEnum
	kFreeOrbit                    =86017      # from enum OrbitTypeEnum
	kOrdinateContinuousAlignment  =102145     # from enum OrdinateDimensionAlignmentEnum
	kOrdinateLeaderAligned        =102146     # from enum OrdinateDimensionAlignmentEnum
	kOridateNoAlignment           =102147     # from enum OrdinateDimensionAlignmentEnum
	kApplyDrivenDimension         =50689      # from enum OverConstrainedDimensionBehaviorEnum
	kWarnOfOverConstrainedCondition=50690      # from enum OverConstrainedDimensionBehaviorEnum
	kFullOverflowMenu             =97793      # from enum OverflowMenuBehaviorEnum
	kRadialOnlyOverflowMenu       =97794      # from enum OverflowMenuBehaviorEnum
	kShortOverflowMenu            =97795      # from enum OverflowMenuBehaviorEnum
	kDefaultPageOrientation       =10241      # from enum PageOrientationTypeEnum
	kLandscapePageOrientation     =10242      # from enum PageOrientationTypeEnum
	kPortraitPageOrientation      =10243      # from enum PageOrientationTypeEnum
	kPaperSize10x14               =14337      # from enum PaperSizeEnum
	kPaperSize11x17               =14338      # from enum PaperSizeEnum
	kPaperSizeA0                  =14357      # from enum PaperSizeEnum
	kPaperSizeA0Oversize          =14358      # from enum PaperSizeEnum
	kPaperSizeA1                  =14359      # from enum PaperSizeEnum
	kPaperSizeA1Oversize          =14360      # from enum PaperSizeEnum
	kPaperSizeA2                  =14339      # from enum PaperSizeEnum
	kPaperSizeA2Oversize          =14361      # from enum PaperSizeEnum
	kPaperSizeA3                  =14340      # from enum PaperSizeEnum
	kPaperSizeA4                  =14341      # from enum PaperSizeEnum
	kPaperSizeA4Small             =14342      # from enum PaperSizeEnum
	kPaperSizeA5                  =14343      # from enum PaperSizeEnum
	kPaperSizeA6                  =14365      # from enum PaperSizeEnum
	kPaperSizeB0                  =14366      # from enum PaperSizeEnum
	kPaperSizeB1                  =14362      # from enum PaperSizeEnum
	kPaperSizeB2                  =14363      # from enum PaperSizeEnum
	kPaperSizeB3                  =14364      # from enum PaperSizeEnum
	kPaperSizeB4                  =14344      # from enum PaperSizeEnum
	kPaperSizeB5                  =14345      # from enum PaperSizeEnum
	kPaperSizeB6                  =14367      # from enum PaperSizeEnum
	kPaperSizeCSheet              =14346      # from enum PaperSizeEnum
	kPaperSizeCustom              =14355      # from enum PaperSizeEnum
	kPaperSizeDSheet              =14347      # from enum PaperSizeEnum
	kPaperSizeDefault             =14356      # from enum PaperSizeEnum
	kPaperSizeESheet              =14348      # from enum PaperSizeEnum
	kPaperSizeExecutive           =14349      # from enum PaperSizeEnum
	kPaperSizeFolio               =14350      # from enum PaperSizeEnum
	kPaperSizeLedger              =14351      # from enum PaperSizeEnum
	kPaperSizeLegal               =14352      # from enum PaperSizeEnum
	kPaperSizeLetter              =14353      # from enum PaperSizeEnum
	kPaperSizeQuarto              =14354      # from enum PaperSizeEnum
	kArchitecturalDisplayFormat   =92419      # from enum ParameterDisplayFormatEnum
	kDecimalDisplayFormat         =92417      # from enum ParameterDisplayFormatEnum
	kFractionalDisplayFormat      =92418      # from enum ParameterDisplayFormatEnum
	kDerivedParameter             =11525      # from enum ParameterTypeEnum
	kModelParameter               =11521      # from enum ParameterTypeEnum
	kReferenceParameter           =11522      # from enum ParameterTypeEnum
	kTableParameter               =11523      # from enum ParameterTypeEnum
	kUserParameter                =11524      # from enum ParameterTypeEnum
	kNegativeExtentDirection      =20994      # from enum PartFeatureExtentDirectionEnum
	kPositiveExtentDirection      =20993      # from enum PartFeatureExtentDirectionEnum
	kSymmetricExtentDirection     =20995      # from enum PartFeatureExtentDirectionEnum
	kAngleExtent                  =20738      # from enum PartFeatureExtentEnum
	kCenteredWidthExtent          =20755      # from enum PartFeatureExtentEnum
	kCutAcrossBendsExtent         =20756      # from enum PartFeatureExtentEnum
	kDistanceExtent               =20737      # from enum PartFeatureExtentEnum
	kEdgeWidthExtent              =20751      # from enum PartFeatureExtentEnum
	kFlangeDistanceExtent         =20748      # from enum PartFeatureExtentEnum
	kFlangeLegacyDistanceExtent   =20750      # from enum PartFeatureExtentEnum
	kFlangeToExtent               =20749      # from enum PartFeatureExtentEnum
	kFromToExtent                 =20742      # from enum PartFeatureExtentEnum
	kFromToWidthExtent            =20754      # from enum PartFeatureExtentEnum
	kFullSweepExtent              =20739      # from enum PartFeatureExtentEnum
	kOffsetWidthExtent            =20753      # from enum PartFeatureExtentEnum
	kPitchAndHeightCoilExtent     =20746      # from enum PartFeatureExtentEnum
	kPitchAndRevolutionCoilExtent =20744      # from enum PartFeatureExtentEnum
	kRevolutionAndHeightCoilExtent=20745      # from enum PartFeatureExtentEnum
	kSpiralCoilExtent             =20747      # from enum PartFeatureExtentEnum
	kThroughAllExtent             =20743      # from enum PartFeatureExtentEnum
	kToExtent                     =20741      # from enum PartFeatureExtentEnum
	kToNextExtent                 =20740      # from enum PartFeatureExtentEnum
	kWidthOffsetWidthExtent       =20752      # from enum PartFeatureExtentEnum
	kCutOperation                 =20482      # from enum PartFeatureOperationEnum
	kIntersectOperation           =20483      # from enum PartFeatureOperationEnum
	kJoinOperation                =20481      # from enum PartFeatureOperationEnum
	kNewBodyOperation             =20485      # from enum PartFeatureOperationEnum
	kSurfaceOperation             =20484      # from enum PartFeatureOperationEnum
	kMicrosoftAccess              =48641      # from enum PartsListFileFormatEnum
	kMicrosoftExcel               =48642      # from enum PartsListFileFormatEnum
	kTextFileCommaDelimited       =48647      # from enum PartsListFileFormatEnum
	kTextFileTabDelimited         =48646      # from enum PartsListFileFormatEnum
	kUnicodeTextFileCommaDelimited=48649      # from enum PartsListFileFormatEnum
	kUnicodeTextFileTabDelimited  =48648      # from enum PartsListFileFormatEnum
	kdBASEIII                     =48643      # from enum PartsListFileFormatEnum
	kdBASEIV                      =48644      # from enum PartsListFileFormatEnum
	kFirstLevelComponents         =46593      # from enum PartsListLevelEnum
	kPartsOnly                    =46594      # from enum PartsListLevelEnum
	kStructured                   =46593      # from enum PartsListLevelEnum
	kStructuredAllLevels          =46595      # from enum PartsListLevelEnum
	kAdjustToModelCompute         =47362      # from enum PatternComputeTypeEnum
	kIdenticalCompute             =47361      # from enum PatternComputeTypeEnum
	kOptimizedCompute             =47363      # from enum PatternComputeTypeEnum
	kAdjustToDirection1           =33794      # from enum PatternOrientationEnum
	kAdjustToDirection2           =33795      # from enum PatternOrientationEnum
	kIdentical                    =33793      # from enum PatternOrientationEnum
	kDefault                      =33537      # from enum PatternSpacingTypeEnum
	kFitToPathLength              =33539      # from enum PatternSpacingTypeEnum
	kFitted                       =33538      # from enum PatternSpacingTypeEnum
	kPhysicalModelArea            =72450      # from enum PhysicalPropertyEnum
	kPhysicalModelDensity         =72452      # from enum PhysicalPropertyEnum
	kPhysicalModelMass            =72449      # from enum PhysicalPropertyEnum
	kPhysicalModelVolume          =72451      # from enum PhysicalPropertyEnum
	kPtAtIntersection             =22273      # from enum PointInferenceEnum
	kPtAtMidPoint                 =22276      # from enum PointInferenceEnum
	kPtOnCurve                    =22274      # from enum PointInferenceEnum
	kPtOnPt                       =22275      # from enum PointInferenceEnum
	kAxisEndPointIntent           =57867      # from enum PointIntentEnum
	kAxisMidPointIntent           =57866      # from enum PointIntentEnum
	kAxisStartPointIntent         =57865      # from enum PointIntentEnum
	kCenterPointIntent            =57860      # from enum PointIntentEnum
	kCircularBottomPointIntent    =57864      # from enum PointIntentEnum
	kCircularLeftPointIntent      =57861      # from enum PointIntentEnum
	kCircularRightPointIntent     =57862      # from enum PointIntentEnum
	kCircularTopPointIntent       =57863      # from enum PointIntentEnum
	kEndPointIntent               =57858      # from enum PointIntentEnum
	kMidPointIntent               =57859      # from enum PointIntentEnum
	kPlanarFaceCenterPointIntent  =57868      # from enum PointIntentEnum
	kStartPointIntent             =57857      # from enum PointIntentEnum
	kCirclePointStyle             =20226      # from enum PointRenderStyleEnum
	kCrossPointStyle              =20230      # from enum PointRenderStyleEnum
	kCustomImagePointStyle        =20235      # from enum PointRenderStyleEnum
	kDimCircularPointStyle        =20227      # from enum PointRenderStyleEnum
	kEndPointStyle                =20234      # from enum PointRenderStyleEnum
	kFilledCirclePointStyle       =20228      # from enum PointRenderStyleEnum
	kFilledCircleSelectPointStyle =20229      # from enum PointRenderStyleEnum
	kFilledCrossPointStyle        =20231      # from enum PointRenderStyleEnum
	kNoSnapPointStyle             =20233      # from enum PointRenderStyleEnum
	kOnCurvePointStyle            =20232      # from enum PointRenderStyleEnum
	kXPointStyle                  =20225      # from enum PointRenderStyleEnum
	kAboveAndBelow                =42498      # from enum PrefixAndSuffixOrderEnum
	kBeforeAndAfter               =42497      # from enum PrefixAndSuffixOrderEnum
	kPrintColorPalette            =13313      # from enum PrintColorModeEnum
	kPrintDefaultColorMode        =13315      # from enum PrintColorModeEnum
	kPrintGrayScale               =13314      # from enum PrintColorModeEnum
	kDefaultOrientation           =13571      # from enum PrintOrientationEnum
	kLandscapeOrientation         =13570      # from enum PrintOrientationEnum
	kPortraitOrientation          =13569      # from enum PrintOrientationEnum
	kPrintAllSheets               =14082      # from enum PrintRangeEnum
	kPrintCurrentSheet            =14081      # from enum PrintRangeEnum
	kPrintSheetRange              =14083      # from enum PrintRangeEnum
	kPrintBestFitScale            =13826      # from enum PrintScaleModeEnum
	kPrintCurrentWindow           =13828      # from enum PrintScaleModeEnum
	kPrintCustomScale             =13827      # from enum PrintScaleModeEnum
	kPrintFullScale               =13825      # from enum PrintScaleModeEnum
	kCommandNameEvent             =6661       # from enum PrivateEventTypeEnum
	kDimensionEvent               =6659       # from enum PrivateEventTypeEnum
	kFileNameEvent                =6657       # from enum PrivateEventTypeEnum
	kNameEvent                    =6658       # from enum PrivateEventTypeEnum
	kStringEvent                  =6660       # from enum PrivateEventTypeEnum
	kProductEditionInventor       =76551      # from enum ProductEditionEnum
	kProductEditionInventorFactoryAdvanced=76553      # from enum ProductEditionEnum
	kProductEditionInventorFactoryPremium=76552      # from enum ProductEditionEnum
	kProductEditionInventorFactoryUltimate=76553      # from enum ProductEditionEnum
	kProductEditionInventorLT     =76545      # from enum ProductEditionEnum
	kProductEditionInventorOEM    =76554      # from enum ProductEditionEnum
	kProductEditionInventorProfessional=76547      # from enum ProductEditionEnum
	kProductEditionInventorRoutedSystems=76548      # from enum ProductEditionEnum
	kProductEditionInventorSimulation=76549      # from enum ProductEditionEnum
	kProductEditionInventorSuite  =76546      # from enum ProductEditionEnum
	kProductEditionInventorTooling=76550      # from enum ProductEditionEnum
	kOrthographicProjection       =86273      # from enum ProjectionTypeEnum
	kPerspectiveProjection        =86274      # from enum ProjectionTypeEnum
	kDontAllowButton1NeverAgain   =8          # from enum PromptMessageRestrictionsEnum
	kDontAllowButton1NoMoreThisSession=16         # from enum PromptMessageRestrictionsEnum
	kDontAllowButton2NeverAgain   =64         # from enum PromptMessageRestrictionsEnum
	kDontAllowButton2NoMoreThisSession=128        # from enum PromptMessageRestrictionsEnum
	kDontAllowButton3NeverAgain   =512        # from enum PromptMessageRestrictionsEnum
	kDontAllowButton3NoMoreThisSession=1024       # from enum PromptMessageRestrictionsEnum
	kDontAllowNeverAgain          =1          # from enum PromptMessageRestrictionsEnum
	kDontAllowNoMoreThisSession   =2          # from enum PromptMessageRestrictionsEnum
	kNoRestrictions               =0          # from enum PromptMessageRestrictionsEnum
	kAuthoringToolContentLibrary  =11         # from enum PropertiesForContentLibraryEnum
	kComponentTypeContentLibrary  =3          # from enum PropertiesForContentLibraryEnum
	kDomainCategoriesContentLibrary=13         # from enum PropertiesForContentLibraryEnum
	kFamilyContentLibrary         =6          # from enum PropertiesForContentLibraryEnum
	kFamilyIdContentLibrary       =17         # from enum PropertiesForContentLibraryEnum
	kFamilyReviesionTimeContentLibrary=18         # from enum PropertiesForContentLibraryEnum
	kFamilyRevisionContentLibrary =9          # from enum PropertiesForContentLibraryEnum
	kFamilyfolderContentLibrary   =19         # from enum PropertiesForContentLibraryEnum
	kLibraryContentLibrary        =4          # from enum PropertiesForContentLibraryEnum
	kLibraryIdContentLibrary      =10         # from enum PropertiesForContentLibraryEnum
	kLibraryLocationContentLibrary=2          # from enum PropertiesForContentLibraryEnum
	kMemberContentLibrary         =7          # from enum PropertiesForContentLibraryEnum
	kMemberFileNameContentLibrary =21         # from enum PropertiesForContentLibraryEnum
	kMemberIdContentLibrary       =20         # from enum PropertiesForContentLibraryEnum
	kMemberRevisionContentLibrary =8          # from enum PropertiesForContentLibraryEnum
	kSizeDesignationContentLibrary=12         # from enum PropertiesForContentLibraryEnum
	kUserCategoriesContentLibrary =15         # from enum PropertiesForContentLibraryEnum
	k_MonikerContentLibrary       =16         # from enum PropertiesForContentLibraryEnum
	k_PropertySetSchemaRevisionContentLibrary=14         # from enum PropertiesForContentLibraryEnum
	k_SubLibraryContentLibrary    =5          # from enum PropertiesForContentLibraryEnum
	kCheckInByDesignTrackingControl=7          # from enum PropertiesForDesignTrackingControlEnum
	kCheckInDateDesignTrackingControl=8          # from enum PropertiesForDesignTrackingControlEnum
	kCheckOutVersionDesignTrackingControls=12         # from enum PropertiesForDesignTrackingControlEnum
	kCheckOutWorkGroupDesignTrackingControl=9          # from enum PropertiesForDesignTrackingControlEnum
	kCheckOutWorkSpaceDesignTrackingControl=11         # from enum PropertiesForDesignTrackingControlEnum
	kCheckedOutByDesignTrackingControl=5          # from enum PropertiesForDesignTrackingControlEnum
	kCheckedOutDateDesignTrackingControl=6          # from enum PropertiesForDesignTrackingControlEnum
	kCurrentVersionDesignTrackingControl=14         # from enum PropertiesForDesignTrackingControlEnum
	kDrawingDeferUpdateDesignTrackingControl=19         # from enum PropertiesForDesignTrackingControlEnum
	kLastSavedByDesignTrackingControl=16         # from enum PropertiesForDesignTrackingControlEnum
	kLastSavedDateDesignTrackingControl=17         # from enum PropertiesForDesignTrackingControlEnum
	kNextVersionDesignTrackingControl=13         # from enum PropertiesForDesignTrackingControlEnum
	kPreviousVersionDesignTrackingControl=15         # from enum PropertiesForDesignTrackingControlEnum
	kAppearanceDesignTrackingProperties=72         # from enum PropertiesForDesignTrackingPropertiesEnum
	kAuthorityDesignTrackingProperties=43         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCatalogWebLinkDesignTrackingProperties=23         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCategoriesDesignTrackingProperties=56         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCheckedByDesignTrackingProperties=10         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCostCenterDesignTrackingProperties=9          # from enum PropertiesForDesignTrackingPropertiesEnum
	kCostDesignTrackingProperties =36         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCreationDateDesignTrackingProperties=4          # from enum PropertiesForDesignTrackingPropertiesEnum
	kDateCheckedDesignTrackingProperties=11         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDateEngrApprovedDesignTrackingProperties=13         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDateMfgApprovedDesignTrackingProperties=35         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDensityDesignTrackingProperties=61         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDescriptionDesignTrackingProperties=29         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDesignStatusDesignTrackingProperties=40         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDesignerDesignTrackingProperties=41         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDocSubTypeDesignTrackingProperties=31         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDocSubTypeNameDesignTrackingProperties=32         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDrawingDeferUpdateDesignTrackingProperties=51         # from enum PropertiesForDesignTrackingPropertiesEnum
	kEngineerDesignTrackingProperties=42         # from enum PropertiesForDesignTrackingPropertiesEnum
	kEngrApprovedByDesignTrackingProperties=12         # from enum PropertiesForDesignTrackingPropertiesEnum
	kExternalPropRevIdDesignTrackingProperties=46         # from enum PropertiesForDesignTrackingPropertiesEnum
	kFlatPatternExtentsAreaDesignTrackingProperties=65         # from enum PropertiesForDesignTrackingPropertiesEnum
	kFlatPatternExtentsLengthDesignTrackingProperties=64         # from enum PropertiesForDesignTrackingPropertiesEnum
	kFlatPatternExtentsWidthDesignTrackingProperties=63         # from enum PropertiesForDesignTrackingPropertiesEnum
	kLanguageDesignTrackingProperties=50         # from enum PropertiesForDesignTrackingPropertiesEnum
	kLastUpdatedWithDesignTrackingProperties=67         # from enum PropertiesForDesignTrackingPropertiesEnum
	kManufacturerDesignTrackingProperties=48         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMassDesignTrackingProperties =58         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMaterialDesignTrackingProperties=20         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMaterialIdentifierDesignTrackingProperties=71         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMfgApprovedByDesignTrackingProperties=34         # from enum PropertiesForDesignTrackingPropertiesEnum
	kParameterizedTemplateDesignTrackingProperties=44         # from enum PropertiesForDesignTrackingPropertiesEnum
	kPartIconDesignTrackingProperties=28         # from enum PropertiesForDesignTrackingPropertiesEnum
	kPartNumberDesignTrackingProperties=5          # from enum PropertiesForDesignTrackingPropertiesEnum
	kPartPropRevIdDesignTrackingProperties=21         # from enum PropertiesForDesignTrackingPropertiesEnum
	kProjectDesignTrackingProperties=7          # from enum PropertiesForDesignTrackingPropertiesEnum
	kProxyRefreshDateDesignTrackingProperties=33         # from enum PropertiesForDesignTrackingPropertiesEnum
	kSheetMetalRuleDesignTrackingProperties=66         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStandardDesignTrackingProperties=37         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStandardRevisionDesignTrackingProperties=47         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStandardsOrganizationDesignTrackingProperties=49         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStockNumberDesignTrackingProperties=55         # from enum PropertiesForDesignTrackingPropertiesEnum
	kSurfaceAreaDesignTrackingProperties=59         # from enum PropertiesForDesignTrackingPropertiesEnum
	kTemplateRowDesignTrackingProperties=45         # from enum PropertiesForDesignTrackingPropertiesEnum
	kUserStatusDesignTrackingProperties=17         # from enum PropertiesForDesignTrackingPropertiesEnum
	kValidMassPropsDesignTrackingProperties=62         # from enum PropertiesForDesignTrackingPropertiesEnum
	kVendorDesignTrackingProperties=30         # from enum PropertiesForDesignTrackingPropertiesEnum
	kVolumeDesignTrackingProperties=60         # from enum PropertiesForDesignTrackingPropertiesEnum
	kWeldMaterialDesignTrackingProperties=57         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCategoryDocSummaryInformation=2          # from enum PropertiesForDocSummaryInformationEnum
	kCompanyDocSummaryInformation =15         # from enum PropertiesForDocSummaryInformationEnum
	kManagerDocSummaryInformation =14         # from enum PropertiesForDocSummaryInformationEnum
	kAuthorSummaryInformation     =4          # from enum PropertiesForSummaryInformationEnum
	kCommentsSummaryInformation   =6          # from enum PropertiesForSummaryInformationEnum
	kCreationTimeSummaryInformation=12         # from enum PropertiesForSummaryInformationEnum
	kKeywordsSummaryInformation   =5          # from enum PropertiesForSummaryInformationEnum
	kLastSavedBySummaryInformation=8          # from enum PropertiesForSummaryInformationEnum
	kRevisionSummaryInformation   =9          # from enum PropertiesForSummaryInformationEnum
	kSubjectSummaryInformation    =3          # from enum PropertiesForSummaryInformationEnum
	kThumbnailSummaryInformation  =17         # from enum PropertiesForSummaryInformationEnum
	kTitleSummaryInformation      =2          # from enum PropertiesForSummaryInformationEnum
	kDummyUserDefinedProperties   =0          # from enum PropertiesForUserDefinedPropertiesEnum
	kAngleDisplayPrecision_PrivateModelInformation=13         # from enum PropertiesFor_PrivateModelInformationEnum
	kAngleUnits_PrivateModelInformation=9          # from enum PropertiesFor_PrivateModelInformationEnum
	kAssemblyAvailablePvs_PrivateModelInformation=15         # from enum PropertiesFor_PrivateModelInformationEnum
	kCompacted_PrivateModelInformation=14         # from enum PropertiesFor_PrivateModelInformationEnum
	kLengthDisplayPrecision_PrivateModelInformation=12         # from enum PropertiesFor_PrivateModelInformationEnum
	kLengthUnits_PrivateModelInformation=8          # from enum PropertiesFor_PrivateModelInformationEnum
	kMassUnits_PrivateModelInformation=11         # from enum PropertiesFor_PrivateModelInformationEnum
	kPartActiveColorStyle_PrivateModelInformation=16         # from enum PropertiesFor_PrivateModelInformationEnum
	kTimeUnits_PrivateModelInformation=10         # from enum PropertiesFor_PrivateModelInformationEnum
	kBaseQuantityPartsListProperty=45576      # from enum PropertyTypeEnum
	kBaseUnitPartsListProperty    =45577      # from enum PropertyTypeEnum
	kCustomProperty               =45570      # from enum PropertyTypeEnum
	kFileProperty                 =45569      # from enum PropertyTypeEnum
	kFilenamePartsListProperty    =45571      # from enum PropertyTypeEnum
	kItemPartsListProperty        =45572      # from enum PropertyTypeEnum
	kItemQuantityPartsListProperty=45578      # from enum PropertyTypeEnum
	kMassPartsListProperty        =45573      # from enum PropertyTypeEnum
	kMaterialPartsListProperty    =45574      # from enum PropertyTypeEnum
	kQuantityPartsListProperty    =45575      # from enum PropertyTypeEnum
	kUnitQuantityPartsListProperty=45579      # from enum PropertyTypeEnum
	kVolumePartsListProperty      =45580      # from enum PropertyTypeEnum
	kNumberOfLikePunchesInFeature =83713      # from enum PunchNoteQuantityEnum
	kNumberOfLikePunchesInModel   =83714      # from enum PunchNoteQuantityEnum
	k2DSketchAndCenterMarkPunchRepresentation=64517      # from enum PunchRepresentationTypeEnum
	k2DSketchPunchRepresentation  =64515      # from enum PunchRepresentationTypeEnum
	kCentermarkPunchRepresentation=64516      # from enum PunchRepresentationTypeEnum
	kDefaultPunchRepresentation   =64513      # from enum PunchRepresentationTypeEnum
	kFormedFeaturePunchRepresentation=64514      # from enum PunchRepresentationTypeEnum
	kBestRayTracingQuality        =95747      # from enum RayTracingQualityEnum
	kDraftRayTracingQuality       =95749      # from enum RayTracingQualityEnum
	kGoodRayTracingQuality        =95746      # from enum RayTracingQualityEnum
	kHighRayTracingQuality        =95750      # from enum RayTracingQualityEnum
	kInteractiveRayTracingQuality =95745      # from enum RayTracingQualityEnum
	kLowRayTracingQuality         =95748      # from enum RayTracingQualityEnum
	kMonitorAndEnableUpdate       =90626      # from enum ReferenceMonitoringEnum
	kNoMonitor                    =90625      # from enum ReferenceMonitoringEnum
	kMissingReference             =49668      # from enum ReferenceStatusEnum
	kOutOfDateReference           =49667      # from enum ReferenceStatusEnum
	kReplacedReference            =49669      # from enum ReferenceStatusEnum
	kUnknownReference             =49665      # from enum ReferenceStatusEnum
	kUpToDateReference            =49666      # from enum ReferenceStatusEnum
	kRelationshipAngleValue       =103169     # from enum RelationshipValueTypeEnum
	kRelationshipAngularPositionValue=103173     # from enum RelationshipValueTypeEnum
	kRelationshipGapValue         =103170     # from enum RelationshipValueTypeEnum
	kRelationshipLinearPositionValue=103171     # from enum RelationshipValueTypeEnum
	kRelationshipOffsetValue      =103172     # from enum RelationshipValueTypeEnum
	kEmbeddedReport               =107778     # from enum ReportLocationEnum
	kExternalReport               =107779     # from enum ReportLocationEnum
	kNoReport                     =107777     # from enum ReportLocationEnum
	kRevisionTableCustomProperty  =89346      # from enum RevisionTablePropertyEnum
	kRevisionTableDateProperty    =89347      # from enum RevisionTablePropertyEnum
	kRevisionTableFileProperty    =89345      # from enum RevisionTablePropertyEnum
	kRevisionTableLtrProperty     =89351      # from enum RevisionTablePropertyEnum
	kRevisionTableSheetProperty   =89348      # from enum RevisionTablePropertyEnum
	kRevisionTableZoneProperty    =89349      # from enum RevisionTablePropertyEnum
	kRevisionTableZoneSheetProperty=89350      # from enum RevisionTablePropertyEnum
	kCircularRevisionTag          =89089      # from enum RevisionTagShapeEnum
	kHexagonRevisionTag           =89090      # from enum RevisionTagShapeEnum
	kSquareRevisionTag            =89091      # from enum RevisionTagShapeEnum
	kTriangularRevisionTag        =89092      # from enum RevisionTagShapeEnum
	kFiniteRibExtent              =93697      # from enum RibFeatureExtentEnum
	kToNextRibExtent              =93698      # from enum RibFeatureExtentEnum
	kRibThicknessAtRoot           =93954      # from enum RibThicknessPlaneEnum
	kRibThicknessAtSketchPlane    =93953      # from enum RibThicknessPlaneEnum
	kAllTextOff                   =82946      # from enum RibbonAppearanceEnum
	kCompact                      =82948      # from enum RibbonAppearanceEnum
	kLarge                        =82949      # from enum RibbonAppearanceEnum
	kNormal                       =82945      # from enum RibbonAppearanceEnum
	kSmall                        =82947      # from enum RibbonAppearanceEnum
	kDockToLeft                   =85763      # from enum RibbonDockingStateEnum
	kDockToRight                  =85764      # from enum RibbonDockingStateEnum
	kDockToTop                    =85762      # from enum RibbonDockingStateEnum
	kFloating                     =85761      # from enum RibbonDockingStateEnum
	kFullRibbon                   =83201      # from enum RibbonStateEnum
	kMinimizeToPanelButtons       =83204      # from enum RibbonStateEnum
	kMinimizeToPanelTitles        =83203      # from enum RibbonStateEnum
	kMinimizeToTabs               =83202      # from enum RibbonStateEnum
	kAngleVectorVectorJoint       =68097      # from enum RigidBodyJointTypeEnum
	kConCentricCircleCircleJoint  =68109      # from enum RigidBodyJointTypeEnum
	kDistanceLineLineJoint        =68113      # from enum RigidBodyJointTypeEnum
	kDistanceLinePlaneJoint       =68114      # from enum RigidBodyJointTypeEnum
	kDistancePlanePlaneJoint      =68115      # from enum RigidBodyJointTypeEnum
	kDistancePointLineJoint       =68111      # from enum RigidBodyJointTypeEnum
	kDistancePointPlaneJoint      =68112      # from enum RigidBodyJointTypeEnum
	kDistancePointPointJoint      =68110      # from enum RigidBodyJointTypeEnum
	kEqualDistancePlanePlaneJoint =68117      # from enum RigidBodyJointTypeEnum
	kEqualDistancePointPlaneJoint =68116      # from enum RigidBodyJointTypeEnum
	kGearJoint                    =68138      # from enum RigidBodyJointTypeEnum
	kMateConeConeJoint            =68104      # from enum RigidBodyJointTypeEnum
	kMateCurveCurveJoint          =68108      # from enum RigidBodyJointTypeEnum
	kMateCylinderCylinderJoint    =68101      # from enum RigidBodyJointTypeEnum
	kMateLineLineJoint            =68100      # from enum RigidBodyJointTypeEnum
	kMatePointCircleJoint         =68106      # from enum RigidBodyJointTypeEnum
	kMatePointCurveJoint          =68105      # from enum RigidBodyJointTypeEnum
	kMatePointLineJoint           =68099      # from enum RigidBodyJointTypeEnum
	kMatePointPointJoint          =68098      # from enum RigidBodyJointTypeEnum
	kMatePointSurfaceJoint        =68107      # from enum RigidBodyJointTypeEnum
	kMateSphereConeJoint          =68103      # from enum RigidBodyJointTypeEnum
	kMateSphereSphereJoint        =68102      # from enum RigidBodyJointTypeEnum
	kPerpendicularCurveSurfaceJoint=68134      # from enum RigidBodyJointTypeEnum
	kRevoluteJoint                =68136      # from enum RigidBodyJointTypeEnum
	kSymmetricCircleCircleLineJoint=68148      # from enum RigidBodyJointTypeEnum
	kSymmetricEllipseEllipseLineJoint=68149      # from enum RigidBodyJointTypeEnum
	kSymmetricLineLineLineJoint   =68147      # from enum RigidBodyJointTypeEnum
	kSymmetricLineLinePlaneJoint  =68145      # from enum RigidBodyJointTypeEnum
	kSymmetricPlanePlanePlaneJoint=68144      # from enum RigidBodyJointTypeEnum
	kSymmetricPointPointLineJoint =68146      # from enum RigidBodyJointTypeEnum
	kSymmetricPointPointPlaneJoint=68142      # from enum RigidBodyJointTypeEnum
	kSymmetricVectorVectorPlaneJoint=68143      # from enum RigidBodyJointTypeEnum
	kTangentCircleCircleJoint     =68129      # from enum RigidBodyJointTypeEnum
	kTangentCircleCylinderJoint   =68127      # from enum RigidBodyJointTypeEnum
	kTangentConeConeJoint         =68125      # from enum RigidBodyJointTypeEnum
	kTangentCurveSurfaceJoint     =68132      # from enum RigidBodyJointTypeEnum
	kTangentCylinderConeJoint     =68123      # from enum RigidBodyJointTypeEnum
	kTangentCylinderCylinderJoint =68119      # from enum RigidBodyJointTypeEnum
	kTangentCylinderSphereJoint   =68120      # from enum RigidBodyJointTypeEnum
	kTangentLineCircleJoint       =68131      # from enum RigidBodyJointTypeEnum
	kTangentLineCylinderJoint     =68128      # from enum RigidBodyJointTypeEnum
	kTangentLineSphereJoint       =68130      # from enum RigidBodyJointTypeEnum
	kTangentPlaneCircleJoint      =68126      # from enum RigidBodyJointTypeEnum
	kTangentPlaneConeJoint        =68122      # from enum RigidBodyJointTypeEnum
	kTangentPlaneCylinderJoint    =68118      # from enum RigidBodyJointTypeEnum
	kTangentSphereConeJoint       =68124      # from enum RigidBodyJointTypeEnum
	kTangentSphereSphereJoint     =68121      # from enum RigidBodyJointTypeEnum
	kTangentSurfaceSurfaceJoint   =68133      # from enum RigidBodyJointTypeEnum
	kTransitionalJoint            =68137      # from enum RigidBodyJointTypeEnum
	kTranslationalJoint           =68135      # from enum RigidBodyJointTypeEnum
	kUniversalJoint               =68141      # from enum RigidBodyJointTypeEnum
	kUnknownJoint                 =68150      # from enum RigidBodyJointTypeEnum
	kWeldJoint                    =68140      # from enum RigidBodyJointTypeEnum
	kWireframeWireframeJoint      =68139      # from enum RigidBodyJointTypeEnum
	kFaceExtentsRipType           =90883      # from enum RipTypeEnum
	kPointToPointRipType          =90882      # from enum RipTypeEnum
	kSinglePointRipType           =90881      # from enum RipTypeEnum
	kCombineNotesRowMerge         =77315      # from enum RowMergeTypeEnum
	kNoRowMerge                   =77313      # from enum RowMergeTypeEnum
	kRollupRowMerge               =77314      # from enum RowMergeTypeEnum
	kNormalRuledSurfaceType       =110337     # from enum RuledSurfaceTypeEnum
	kSweepRuledSurfaceType        =110339     # from enum RuledSurfaceTypeEnum
	kTangentRuledSurfaceType      =110338     # from enum RuledSurfaceTypeEnum
	SELECTTYPE_INSIDE             =1          # from enum SelectType
	SELECTTYPE_OVERLAP            =2          # from enum SelectType
	kBrowserSelection             =15362      # from enum SelectionDeviceEnum
	kGraphicsWindowSelection      =15361      # from enum SelectionDeviceEnum
	kNameSelection                =15363      # from enum SelectionDeviceEnum
	kUnknownSelection             =15364      # from enum SelectionDeviceEnum
	kAllCircularEntities          =18435      # from enum SelectionFilterEnum
	kAllCustomGraphicsFilter      =18436      # from enum SelectionFilterEnum
	kAllEntitiesFilter            =18439      # from enum SelectionFilterEnum
	kAllLinearEntities            =18433      # from enum SelectionFilterEnum
	kAllPlanarEntities            =18432      # from enum SelectionFilterEnum
	kAllPointEntities             =18434      # from enum SelectionFilterEnum
	kAssemblyFeatureFilter        =16646      # from enum SelectionFilterEnum
	kAssemblyLeafOccurrenceFilter =16643      # from enum SelectionFilterEnum
	kAssemblyOccurrenceFilter     =16640      # from enum SelectionFilterEnum
	kAssemblyOccurrencePatternElementFilter=16645      # from enum SelectionFilterEnum
	kAssemblyOccurrencePatternFilter=16644      # from enum SelectionFilterEnum
	kCustomBrowserNodeFilter      =18437      # from enum SelectionFilterEnum
	kDrawingAutoCADBlockDefinitionFilter=16923      # from enum SelectionFilterEnum
	kDrawingAutoCADBlockFilter    =16922      # from enum SelectionFilterEnum
	kDrawingBalloonFilter         =16906      # from enum SelectionFilterEnum
	kDrawingBorderDefinitionFilter=16909      # from enum SelectionFilterEnum
	kDrawingBorderFilter          =16913      # from enum SelectionFilterEnum
	kDrawingCenterlineFilter      =16915      # from enum SelectionFilterEnum
	kDrawingCentermarkFilter      =16916      # from enum SelectionFilterEnum
	kDrawingCurveSegmentFilter    =16914      # from enum SelectionFilterEnum
	kDrawingCustomTableFilter     =16905      # from enum SelectionFilterEnum
	kDrawingDefaultFilter         =16896      # from enum SelectionFilterEnum
	kDrawingDimensionFilter       =16900      # from enum SelectionFilterEnum
	kDrawingFeatureControlFrameFilter=16918      # from enum SelectionFilterEnum
	kDrawingHoleTableFilter       =16902      # from enum SelectionFilterEnum
	kDrawingHoleTagFilter         =16903      # from enum SelectionFilterEnum
	kDrawingNoteFilter            =16899      # from enum SelectionFilterEnum
	kDrawingOriginIndicatorFilter =16920      # from enum SelectionFilterEnum
	kDrawingPartsListFilter       =16901      # from enum SelectionFilterEnum
	kDrawingRevisionTableFilter   =16904      # from enum SelectionFilterEnum
	kDrawingSheetFilter           =16897      # from enum SelectionFilterEnum
	kDrawingSheetFormatFilter     =16917      # from enum SelectionFilterEnum
	kDrawingSketchedSymbolDefinitionFilter=16908      # from enum SelectionFilterEnum
	kDrawingSketchedSymbolFilter  =16907      # from enum SelectionFilterEnum
	kDrawingSurfaceTextureSymbolFilter=16919      # from enum SelectionFilterEnum
	kDrawingTitleBlockDefinitionFilter=16910      # from enum SelectionFilterEnum
	kDrawingTitleBlockFilter      =16912      # from enum SelectionFilterEnum
	kDrawingViewFilter            =16898      # from enum SelectionFilterEnum
	kDrawingViewLabelFilter       =16921      # from enum SelectionFilterEnum
	kFeatureDimensionFilter       =18438      # from enum SelectionFilterEnum
	kPartBodyFilter               =15890      # from enum SelectionFilterEnum
	kPartDefaultFilter            =15886      # from enum SelectionFilterEnum
	kPartEdgeCircularFilter       =15874      # from enum SelectionFilterEnum
	kPartEdgeFilter               =15873      # from enum SelectionFilterEnum
	kPartEdgeLinearFilter         =15875      # from enum SelectionFilterEnum
	kPartEdgeMidpointFilter       =15876      # from enum SelectionFilterEnum
	kPartFaceConicalFilter        =15880      # from enum SelectionFilterEnum
	kPartFaceCylindricalFilter    =15879      # from enum SelectionFilterEnum
	kPartFaceFilter               =15877      # from enum SelectionFilterEnum
	kPartFacePlanarFilter         =15878      # from enum SelectionFilterEnum
	kPartFaceSphericalFilter      =15882      # from enum SelectionFilterEnum
	kPartFaceToroidalFilter       =15881      # from enum SelectionFilterEnum
	kPartFeatureFilter            =15884      # from enum SelectionFilterEnum
	kPartSurfaceFeatureFilter     =15885      # from enum SelectionFilterEnum
	kPartVertexFilter             =15883      # from enum SelectionFilterEnum
	kPointCloudFilter             =15891      # from enum SelectionFilterEnum
	kPointCloudPlaneFilter        =15893      # from enum SelectionFilterEnum
	kPointCloudPointFilter        =15892      # from enum SelectionFilterEnum
	kSketch3DCurveCircularFilter  =17666      # from enum SelectionFilterEnum
	kSketch3DCurveEllipseFilter   =17667      # from enum SelectionFilterEnum
	kSketch3DCurveFilter          =17664      # from enum SelectionFilterEnum
	kSketch3DCurveLinearFilter    =17665      # from enum SelectionFilterEnum
	kSketch3DCurveSplineFilter    =17668      # from enum SelectionFilterEnum
	kSketch3DDefaultFilter        =17670      # from enum SelectionFilterEnum
	kSketch3DDimConstraintFilter  =17672      # from enum SelectionFilterEnum
	kSketch3DObjectFilter         =17671      # from enum SelectionFilterEnum
	kSketch3DPointFilter          =17669      # from enum SelectionFilterEnum
	kSketch3DProfileFilter        =17673      # from enum SelectionFilterEnum
	kSketchBlockDefinitionFilter  =16141      # from enum SelectionFilterEnum
	kSketchBlockFilter            =16142      # from enum SelectionFilterEnum
	kSketchCurveCircularFilter    =16131      # from enum SelectionFilterEnum
	kSketchCurveEllipseFilter     =16132      # from enum SelectionFilterEnum
	kSketchCurveFilter            =16129      # from enum SelectionFilterEnum
	kSketchCurveLinearFilter      =16130      # from enum SelectionFilterEnum
	kSketchCurveSplineFilter      =16133      # from enum SelectionFilterEnum
	kSketchDefaultFilter          =16135      # from enum SelectionFilterEnum
	kSketchDimConstraintFilter    =16128      # from enum SelectionFilterEnum
	kSketchImageFilter            =16137      # from enum SelectionFilterEnum
	kSketchObjectFilter           =16136      # from enum SelectionFilterEnum
	kSketchPointFilter            =16134      # from enum SelectionFilterEnum
	kSketchProfileFilter          =16139      # from enum SelectionFilterEnum
	kSketchProjectedCutFilter     =16140      # from enum SelectionFilterEnum
	kSketchTextBoxFilter          =16138      # from enum SelectionFilterEnum
	kUserCoordinateSystemFilter   =16387      # from enum SelectionFilterEnum
	kWorkAxisFilter               =16384      # from enum SelectionFilterEnum
	kWorkPlaneFilter              =16385      # from enum SelectionFilterEnum
	kWorkPointFilter              =16386      # from enum SelectionFilterEnum
	kAnnotationSelectionPriority  =67594      # from enum SelectionPriorityEnum
	kBodySelectionPriority        =67593      # from enum SelectionPriorityEnum
	kComponentSelectionPriority   =67590      # from enum SelectionPriorityEnum
	kEdgeAndFaceSelectionPriority =67587      # from enum SelectionPriorityEnum
	kEdgeSelectionPriority        =67592      # from enum SelectionPriorityEnum
	kFeatureSelectionPriority     =67585      # from enum SelectionPriorityEnum
	kGroupSelectionPriority       =67588      # from enum SelectionPriorityEnum
	kPartSelectionPriority        =67591      # from enum SelectionPriorityEnum
	kSketchSelectionPriority      =67586      # from enum SelectionPriorityEnum
	kWireSelectionPriority        =67589      # from enum SelectionPriorityEnum
	k45DegreesLeftShadowDirection =92161      # from enum ShadowDirectionEnum
	k45DegreesRightShadowDirection=92162      # from enum ShadowDirectionEnum
	kAboveShadowDirection         =92163      # from enum ShadowDirectionEnum
	kLightFourShadowDirection     =92167      # from enum ShadowDirectionEnum
	kLightOneShadowDirection      =92164      # from enum ShadowDirectionEnum
	kLightThreeShadowDirection    =92166      # from enum ShadowDirectionEnum
	kLightTwoShadowDirection      =92165      # from enum ShadowDirectionEnum
	kSheetMetalFlatPatternArea    =78851      # from enum SheetMetalPropertyEnum
	kSheetMetalFlatPatternLength  =78849      # from enum SheetMetalPropertyEnum
	kSheetMetalFlatPatternWidth   =78850      # from enum SheetMetalPropertyEnum
	kBothSidesShellDirection      =41219      # from enum ShellDirectionEnum
	kInsideShellDirection         =41217      # from enum ShellDirectionEnum
	kOutsideShellDirection        =41218      # from enum ShellDirectionEnum
	kShiftStateAlt                =4          # from enum ShiftStateEnum
	kShiftStateCtrl               =2          # from enum ShiftStateEnum
	kShiftStateCtrlAlt            =6          # from enum ShiftStateEnum
	kShiftStateNone               =0          # from enum ShiftStateEnum
	kShiftStateShift              =1          # from enum ShiftStateEnum
	kShiftStateShiftAlt           =5          # from enum ShiftStateEnum
	kShiftStateShiftCtrl          =3          # from enum ShiftStateEnum
	kShiftStateShiftCtrlAlt       =7          # from enum ShiftStateEnum
	kAcceleratorShortcut          =68355      # from enum ShortcutTypeEnum
	kAliasShortcut                =68354      # from enum ShortcutTypeEnum
	kNoShortcut                   =68353      # from enum ShortcutTypeEnum
	kCoincidentInference          =1          # from enum SketchConstraintInferenceTypeEnum
	kHorizontalInference          =2          # from enum SketchConstraintInferenceTypeEnum
	kIntersectionInference        =4          # from enum SketchConstraintInferenceTypeEnum
	kMidPointInference            =8          # from enum SketchConstraintInferenceTypeEnum
	kOnCurveInference             =16         # from enum SketchConstraintInferenceTypeEnum
	kParallelInference            =32         # from enum SketchConstraintInferenceTypeEnum
	kPerpendicularInference       =64         # from enum SketchConstraintInferenceTypeEnum
	kTangentInference             =128        # from enum SketchConstraintInferenceTypeEnum
	kVerticalInference            =256        # from enum SketchConstraintInferenceTypeEnum
	kNoNewSketchCreation          =55041      # from enum SketchCreationOnNewPartEnum
	kXYPlaneSketchCreation        =55042      # from enum SketchCreationOnNewPartEnum
	kXZPlaneSketchCreation        =55044      # from enum SketchCreationOnNewPartEnum
	kYZPlaneSketchCreation        =55043      # from enum SketchCreationOnNewPartEnum
	kCoincident                   =1          # from enum SketchGeometricConstraintTypeEnum
	kColinear                     =4          # from enum SketchGeometricConstraintTypeEnum
	kConcentric                   =2          # from enum SketchGeometricConstraintTypeEnum
	kEqual                        =8          # from enum SketchGeometricConstraintTypeEnum
	kFix                          =16         # from enum SketchGeometricConstraintTypeEnum
	kHorizontal                   =32         # from enum SketchGeometricConstraintTypeEnum
	kParallel                     =64         # from enum SketchGeometricConstraintTypeEnum
	kPerpendicular                =128        # from enum SketchGeometricConstraintTypeEnum
	kSmooth                       =256        # from enum SketchGeometricConstraintTypeEnum
	kSymmetric                    =512        # from enum SketchGeometricConstraintTypeEnum
	kTangent                      =1024       # from enum SketchGeometricConstraintTypeEnum
	kVertical                     =2048       # from enum SketchGeometricConstraintTypeEnum
	kDistinctlyManySolutions      =2          # from enum SolutionNatureEnum
	kInfinitelyManySolutions      =3          # from enum SolutionNatureEnum
	kNoSolution                   =4          # from enum SolutionNatureEnum
	kUniqueSolution               =1          # from enum SolutionNatureEnum
	kUnknownSolutionNature        =0          # from enum SolutionNatureEnum
	kACADSplineFit                =26371      # from enum SplineFitMethodEnum
	kSmoothSplineFit              =26369      # from enum SplineFitMethodEnum
	kSweetSplineFit               =26370      # from enum SplineFitMethodEnum
	kPath                         =33025      # from enum SplitToolTypeEnum
	kSurfaceBody                  =33028      # from enum SplitToolTypeEnum
	kWorkPlane                    =33026      # from enum SplitToolTypeEnum
	kWorkSurface                  =33027      # from enum SplitToolTypeEnum
	kSplitBody                    =32771      # from enum SplitTypeEnum
	kSplitFaces                   =32770      # from enum SplitTypeEnum
	kSplitPart                    =32769      # from enum SplitTypeEnum
	kTrimSolid                    =32769      # from enum SplitTypeEnum
	kAlwaysSectionStandardParts   =66561      # from enum StandardPartsSectionBehaviorEnum
	kNeverSectionStandardParts    =66562      # from enum StandardPartsSectionBehaviorEnum
	kObeyBrowserSettingsSectionStandardParts=66563      # from enum StandardPartsSectionBehaviorEnum
	kFileNewDialogStartupAction   =70913      # from enum StartupActionTypeEnum
	kFileOpenDialogStartupAction  =70914      # from enum StartupActionTypeEnum
	kNewFileFromTemplateStartupAction=70915      # from enum StartupActionTypeEnum
	kNoStartupAction              =70916      # from enum StartupActionTypeEnum
	kInventorClassicStartupHelpTopic=71169      # from enum StartupHelpFocusTopicEnum
	kInventorForAutocadStartupHelpTopic=71170      # from enum StartupHelpFocusTopicEnum
	kStatusError                  =96004      # from enum StatusEnum
	kStatusNo                     =96002      # from enum StatusEnum
	kStatusUnknown                =96003      # from enum StatusEnum
	kStatusYes                    =96001      # from enum StatusEnum
	kFileOrStreamStorage          =6148       # from enum StorageTypeEnum
	kFileStorage                  =6146       # from enum StorageTypeEnum
	kStorageStorage               =6149       # from enum StorageTypeEnum
	kStreamStorage                =6147       # from enum StorageTypeEnum
	kUnknownStorage               =6145       # from enum StorageTypeEnum
	kBothStyleLocation            =51201      # from enum StyleLocationEnum
	kLibraryStyleLocation         =51203      # from enum StyleLocationEnum
	kLocalStyleLocation           =51202      # from enum StyleLocationEnum
	kBodyRenderStyle              =37125      # from enum StyleSourceTypeEnum
	kFeatureRenderStyle           =37122      # from enum StyleSourceTypeEnum
	kOverrideRenderStyle          =37123      # from enum StyleSourceTypeEnum
	kPartRenderStyle              =37121      # from enum StyleSourceTypeEnum
	kWeldBeadRenderStyle          =37124      # from enum StyleSourceTypeEnum
	kBalloonStyleType             =71426      # from enum StyleTypeEnum
	kCentermarkStyleType          =71427      # from enum StyleTypeEnum
	kDatumTargetStyleType         =71428      # from enum StyleTypeEnum
	kDimensionStyleType           =71429      # from enum StyleTypeEnum
	kFeatureControlFrameStyleType =71430      # from enum StyleTypeEnum
	kHatchStyleType               =71431      # from enum StyleTypeEnum
	kHoleTableStyleType           =71432      # from enum StyleTypeEnum
	kIDStyleType                  =71433      # from enum StyleTypeEnum
	kLayerStyleType               =71434      # from enum StyleTypeEnum
	kLeaderStyleType              =71435      # from enum StyleTypeEnum
	kObjectDefaultsStyleType      =71436      # from enum StyleTypeEnum
	kPartsListStyleType           =71437      # from enum StyleTypeEnum
	kRevisionTableStyleType       =71438      # from enum StyleTypeEnum
	kSheetMetalStyleType          =71445      # from enum StyleTypeEnum
	kStandardStyleType            =71425      # from enum StyleTypeEnum
	kSurfaceTextureStyleType      =71439      # from enum StyleTypeEnum
	kTableStyleType               =71440      # from enum StyleTypeEnum
	kTextStyleType                =71441      # from enum StyleTypeEnum
	kUnfoldMethodType             =71446      # from enum StyleTypeEnum
	kViewAnnotationStyleType      =71444      # from enum StyleTypeEnum
	kWeldBeadStyleType            =71443      # from enum StyleTypeEnum
	kWeldSymbolStyleType          =71442      # from enum StyleTypeEnum
	kNoStylesLibraryAccess        =54019      # from enum StylesLibraryAccessEnum
	kReadOnlyStylesLibraryAccess  =54017      # from enum StylesLibraryAccessEnum
	kReadWriteStylesLibraryAccess =54018      # from enum StylesLibraryAccessEnum
	SurfaceGeometryForm_ClosedUVLoops=1          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_NURBS     =4          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_Not_ClosedUVLoops=2          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_Not_NURBS =8          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_ProceduralToNURBS=16         # from enum SurfaceGeometryFormEnum
	kBasicSurfaceType             =76801      # from enum SurfaceTextureTypeEnum
	kMaterialRemovalProhibitedSurfaceType=76803      # from enum SurfaceTextureTypeEnum
	kMaterialRemovalRequiredSurfaceType=76802      # from enum SurfaceTextureTypeEnum
	kBSplineSurface               =5897       # from enum SurfaceTypeEnum
	kConeSurface                  =5893       # from enum SurfaceTypeEnum
	kCylinderSurface              =5891       # from enum SurfaceTypeEnum
	kEllipticalConeSurface        =5894       # from enum SurfaceTypeEnum
	kEllipticalCylinderSurface    =5892       # from enum SurfaceTypeEnum
	kPlaneSurface                 =5890       # from enum SurfaceTypeEnum
	kSphereSurface                =5896       # from enum SurfaceTypeEnum
	kTorusSurface                 =5895       # from enum SurfaceTypeEnum
	kUnknownSurface               =5889       # from enum SurfaceTypeEnum
	kPathAndGuideRailSweepDef     =59138      # from enum SweepDefinitionTypeEnum
	kPathAndGuideSurfaceSweepDef  =59139      # from enum SweepDefinitionTypeEnum
	kPathAndSectionTwistsSweepDef =59140      # from enum SweepDefinitionTypeEnum
	kPathSweepDef                 =59137      # from enum SweepDefinitionTypeEnum
	kNormalToPath                 =59649      # from enum SweepProfileOrientationEnum
	kParallelToOriginalProfile    =59650      # from enum SweepProfileOrientationEnum
	kNoProfileScaling             =59395      # from enum SweepProfileScalingEnum
	kXProfileScaling              =59394      # from enum SweepProfileScalingEnum
	kXYProfileScaling             =59393      # from enum SweepProfileScalingEnum
	kPathAndGuidRailSweepType     =104450     # from enum SweepTypeEnum
	kPathAndGuidSurfaceSweepType  =104451     # from enum SweepTypeEnum
	kPathAndSectionTwistSweepType =104452     # from enum SweepTypeEnum
	kPathSweepType                =104449     # from enum SweepTypeEnum
	kDefaultSystemOfMeasure       =8961       # from enum SystemOfMeasureEnum
	kEnglishSystemOfMeasure       =8963       # from enum SystemOfMeasureEnum
	kMetricSystemOfMeasure        =8962       # from enum SystemOfMeasureEnum
	kBottomUpDirection            =46082      # from enum TableDirectionEnum
	kTopDownDirection             =46081      # from enum TableDirectionEnum
	kBendTableSource              =77058      # from enum TableSourceTypeEnum
	kCSVTableSource               =77061      # from enum TableSourceTypeEnum
	kConfigurationTableSource     =77059      # from enum TableSourceTypeEnum
	kExcelTableSource             =77060      # from enum TableSourceTypeEnum
	kNoTableSource                =77057      # from enum TableSourceTypeEnum
	kExactLineSpacing             =29185      # from enum TextLineSpacingTypeEnum
	kMultipleLineSpacing          =29186      # from enum TextLineSpacingTypeEnum
	k1DTexture                    =95489      # from enum TextureDimensionEnum
	k2DTexture                    =95490      # from enum TextureDimensionEnum
	kAutomaticMappingType         =100866     # from enum TextureMappingTypeEnum
	kBoxMappingType               =100867     # from enum TextureMappingTypeEnum
	kCylindricalMappingType       =100868     # from enum TextureMappingTypeEnum
	kNoMappingType                =100865     # from enum TextureMappingTypeEnum
	kPlanarMappingType            =100869     # from enum TextureMappingTypeEnum
	kSphericalMappingType         =100870     # from enum TextureMappingTypeEnum
	kStandardThread               =22017      # from enum ThreadTypeEnum
	kTaperedThread                =22018      # from enum ThreadTypeEnum
	kActiveComponentIsoViewOnSave =79874      # from enum ThumbnailSaveOptionEnum
	kActiveWindow                 =79876      # from enum ThumbnailSaveOptionEnum
	kActiveWindowOnSave           =79875      # from enum ThumbnailSaveOptionEnum
	kImportFromFile               =79877      # from enum ThumbnailSaveOptionEnum
	kNoThumbnail                  =79873      # from enum ThumbnailSaveOptionEnum
	kLowerLeftTitleBlockAlignment =66818      # from enum TitleBlockAlignmentEnum
	kLowerRightTitleBlockAlignment=66820      # from enum TitleBlockAlignmentEnum
	kUpperLeftTitleBlockAlignment =66817      # from enum TitleBlockAlignmentEnum
	kUpperRightTitleBlockAlignment=66819      # from enum TitleBlockAlignmentEnum
	kBottomLeftPosition           =29443      # from enum TitleBlockLocationEnum
	kBottomRightPosition          =29444      # from enum TitleBlockLocationEnum
	kTopLeftPosition              =29441      # from enum TitleBlockLocationEnum
	kTopRightPosition             =29442      # from enum TitleBlockLocationEnum
	kBasicTolerance               =31245      # from enum ToleranceTypeEnum
	kDefaultTolerance             =31233      # from enum ToleranceTypeEnum
	kDeviationTolerance           =31236      # from enum ToleranceTypeEnum
	kLimitLinearTolerance         =31238      # from enum ToleranceTypeEnum
	kLimitsFitsLinearTolerance    =31242      # from enum ToleranceTypeEnum
	kLimitsFitsShowSizeTolerance  =31243      # from enum ToleranceTypeEnum
	kLimitsFitsShowTolerance      =31244      # from enum ToleranceTypeEnum
	kLimitsFitsStackedTolerance   =31241      # from enum ToleranceTypeEnum
	kLimitsStackedTolerance       =31237      # from enum ToleranceTypeEnum
	kMaxTolerance                 =31239      # from enum ToleranceTypeEnum
	kMinTolerance                 =31240      # from enum ToleranceTypeEnum
	kOverrideTolerance            =31234      # from enum ToleranceTypeEnum
	kReferenceTolerance           =31246      # from enum ToleranceTypeEnum
	kSymmetricTolerance           =31235      # from enum ToleranceTypeEnum
	kCurrentTransaction           =3588       # from enum TransactionPointEnum
	kNextTransaction              =3586       # from enum TransactionPointEnum
	kPreviousTransaction          =3587       # from enum TransactionPointEnum
	kUnknownTransaction           =3585       # from enum TransactionPointEnum
	kUptoSpecifiedTransaction     =3589       # from enum TransactionPointEnum
	kDoneState                    =36866      # from enum TransactionStateEnum
	kUncommittedState             =36865      # from enum TransactionStateEnum
	kUndoneState                  =36867      # from enum TransactionStateEnum
	kBlendingTransparency         =58625      # from enum TransparencyTypeEnum
	kScreenDoorTransparency       =58626      # from enum TransparencyTypeEnum
	kRepositionMoveType           =49409      # from enum TriadMoveTypeEnum
	kAllSegments                  =0          # from enum TriadSegmentEnum
	kOriginSegment                =1          # from enum TriadSegmentEnum
	kXAxisRotationSegment         =16         # from enum TriadSegmentEnum
	kXAxisTranslationSegment      =2          # from enum TriadSegmentEnum
	kXYPlaneTranslationSegment    =128        # from enum TriadSegmentEnum
	kXZPlaneTranslationSegment    =256        # from enum TriadSegmentEnum
	kYAxisRotationSegment         =32         # from enum TriadSegmentEnum
	kYAxisTranslationSegment      =4          # from enum TriadSegmentEnum
	kYZPlaneTranslationSegment    =512        # from enum TriadSegmentEnum
	kZAxisRotationSegment         =64         # from enum TriadSegmentEnum
	kZAxisTranslationSegment      =8          # from enum TriadSegmentEnum
	kThreePointsDefinitionType    =90370      # from enum UCSDefinitionTypeEnum
	kTransformationDefinitionType =90369      # from enum UCSDefinitionTypeEnum
	kBendAllowanceEquationType    =81409      # from enum UnfoldMethodEquationTypeEnum
	kBendCompensationEquationType =81410      # from enum UnfoldMethodEquationTypeEnum
	kBendDeductionEquationType    =81411      # from enum UnfoldMethodEquationTypeEnum
	kBendkFactorEquationType      =81412      # from enum UnfoldMethodEquationTypeEnum
	kBendTableUnfoldMethod        =28674      # from enum UnfoldMethodTypeEnum
	kCustomEquationUnfoldMethod   =28675      # from enum UnfoldMethodTypeEnum
	kLinearUnfoldMethod           =28673      # from enum UnfoldMethodTypeEnum
	kLockDOF                      =4          # from enum UniqueOccurrencesBehaviorEnum
	kRetainDOF                    =2          # from enum UniqueOccurrencesBehaviorEnum
	kSinglePartRigidBody          =1          # from enum UniqueOccurrencesBehaviorEnum
	kAcreAreaUnits                =11301      # from enum UnitsTypeEnum
	kAmpElectricalCurrentUnits    =11327      # from enum UnitsTypeEnum
	kBTUWorkUnits                 =11320      # from enum UnitsTypeEnum
	kBooleanUnits                 =11347      # from enum UnitsTypeEnum
	kCalorieWorkUnits             =11319      # from enum UnitsTypeEnum
	kCandelaLuminousIntensityUnits=11342      # from enum UnitsTypeEnum
	kCelsiusTemperatureUnits      =11296      # from enum UnitsTypeEnum
	kCentimeterLengthUnits        =11268      # from enum UnitsTypeEnum
	kCircularMilAreaUnits         =11326      # from enum UnitsTypeEnum
	kCompositeUnits               =11322      # from enum UnitsTypeEnum
	kCoulombElectricalChargeUnits =11330      # from enum UnitsTypeEnum
	kCupVolumeUnits               =11306      # from enum UnitsTypeEnum
	kDatabaseAngleUnits           =11277      # from enum UnitsTypeEnum
	kDatabaseLengthUnits          =11267      # from enum UnitsTypeEnum
	kDatabaseMassUnits            =11282      # from enum UnitsTypeEnum
	kDatabaseTemperatureUnits     =11294      # from enum UnitsTypeEnum
	kDatabaseTimeUnits            =11289      # from enum UnitsTypeEnum
	kDefaultDisplayAngleUnits     =11276      # from enum UnitsTypeEnum
	kDefaultDisplayLengthUnits    =11266      # from enum UnitsTypeEnum
	kDefaultDisplayMassUnits      =11281      # from enum UnitsTypeEnum
	kDefaultDisplayTemperatureUnits=11293      # from enum UnitsTypeEnum
	kDefaultDisplayTimeUnits      =11288      # from enum UnitsTypeEnum
	kDegreeAngleUnits             =11279      # from enum UnitsTypeEnum
	kDyneForceUnits               =11312      # from enum UnitsTypeEnum
	kErgWorkUnits                 =11318      # from enum UnitsTypeEnum
	kFahrenheitTemperatureUnits   =11297      # from enum UnitsTypeEnum
	kFaradElectricalCapacitanceUnits=11331      # from enum UnitsTypeEnum
	kFeetPerSecondSpeedUnits      =11299      # from enum UnitsTypeEnum
	kFootLengthUnits              =11273      # from enum UnitsTypeEnum
	kGallonVolumeUnits            =11303      # from enum UnitsTypeEnum
	kGammaMagneticInductionUnits  =11337      # from enum UnitsTypeEnum
	kGaussMagneticInductionUnits  =11338      # from enum UnitsTypeEnum
	kGradAngleUnits               =11280      # from enum UnitsTypeEnum
	kGramMassUnits                =11284      # from enum UnitsTypeEnum
	kHenryElectricalInductanceUnits=11339      # from enum UnitsTypeEnum
	kHertzFrequencyUnits          =11341      # from enum UnitsTypeEnum
	kHorsePowerPowerUnits         =11316      # from enum UnitsTypeEnum
	kHourTimeUnits                =11292      # from enum UnitsTypeEnum
	kInchLengthUnits              =11272      # from enum UnitsTypeEnum
	kJouleWorkUnits               =11317      # from enum UnitsTypeEnum
	kKSIPressureUnits             =11310      # from enum UnitsTypeEnum
	kKelvinTemperatureUnits       =11295      # from enum UnitsTypeEnum
	kKilogramMassUnits            =11283      # from enum UnitsTypeEnum
	kLbForceUnits                 =11313      # from enum UnitsTypeEnum
	kLbMassMassUnits              =11286      # from enum UnitsTypeEnum
	kLiterVolumeUnits             =11302      # from enum UnitsTypeEnum
	kLumenLuminousFluxUnits       =11343      # from enum UnitsTypeEnum
	kLuxIlluminationUnits         =11344      # from enum UnitsTypeEnum
	kMaxwellMagneticFluxUnits     =11335      # from enum UnitsTypeEnum
	kMeterLengthUnits             =11270      # from enum UnitsTypeEnum
	kMetersPerSecondSpeedUnits    =11298      # from enum UnitsTypeEnum
	kMicronLengthUnits            =11271      # from enum UnitsTypeEnum
	kMilLengthUnits               =11324      # from enum UnitsTypeEnum
	kMileLengthUnits              =11275      # from enum UnitsTypeEnum
	kMilesPerHourSpeedUnits       =11300      # from enum UnitsTypeEnum
	kMillimeterLengthUnits        =11269      # from enum UnitsTypeEnum
	kMinuteTimeUnits              =11291      # from enum UnitsTypeEnum
	kMoleSubstanceUnits           =11345      # from enum UnitsTypeEnum
	kNauticalMileLengthUnits      =11323      # from enum UnitsTypeEnum
	kNewtonForceUnits             =11311      # from enum UnitsTypeEnum
	kOerstedMagneticInductionUnits=11340      # from enum UnitsTypeEnum
	kOhmElectricalResistanceUnits =11329      # from enum UnitsTypeEnum
	kOunceForceUnits              =11314      # from enum UnitsTypeEnum
	kOunceMassUnits               =11287      # from enum UnitsTypeEnum
	kOunceVolumeUnits             =11307      # from enum UnitsTypeEnum
	kPSIPressureUnits             =11309      # from enum UnitsTypeEnum
	kPascalPressureUnits          =11308      # from enum UnitsTypeEnum
	kPintVolumeUnits              =11305      # from enum UnitsTypeEnum
	kQuartVolumeUnits             =11304      # from enum UnitsTypeEnum
	kRPMAngularVelocityUnits      =11321      # from enum UnitsTypeEnum
	kRadianAngleUnits             =11278      # from enum UnitsTypeEnum
	kSecondTimeUnits              =11290      # from enum UnitsTypeEnum
	kSiemensElectricalConductanceUnits=11332      # from enum UnitsTypeEnum
	kSlugMassUnits                =11285      # from enum UnitsTypeEnum
	kSteradianAngleUnits          =11325      # from enum UnitsTypeEnum
	kTeslaMagneticInductionUnits  =11336      # from enum UnitsTypeEnum
	kTextUnits                    =11346      # from enum UnitsTypeEnum
	kUnitlessUnits                =11265      # from enum UnitsTypeEnum
	kVoltElectricalVoltageUnits   =11328      # from enum UnitsTypeEnum
	kWattPowerUnits               =11315      # from enum UnitsTypeEnum
	kWeberMagneticFluxUnits       =11334      # from enum UnitsTypeEnum
	kYardLengthUnits              =11274      # from enum UnitsTypeEnum
	kmhoElectricalConductanceUnits=11333      # from enum UnitsTypeEnum
	kDontUpdateProperties         =71681      # from enum UpdatePropertiesOnSaveForFileTypeEnum
	kUpdatePropertiesForPartsAndAssemblies=71683      # from enum UpdatePropertiesOnSaveForFileTypeEnum
	kUpdatePropertiesForPartsOnly =71682      # from enum UpdatePropertiesOnSaveForFileTypeEnum
	kApplicationVBAProject        =30465      # from enum VBAProjectTypeEnum
	kDocumentVBAProject           =30466      # from enum VBAProjectTypeEnum
	kUserVBAProject               =30467      # from enum VBAProjectTypeEnum
	kBooleanType                  =14597      # from enum ValueTypeEnum
	kByteArrayType                =14596      # from enum ValueTypeEnum
	kDoubleType                   =14594      # from enum ValueTypeEnum
	kIntegerType                  =14593      # from enum ValueTypeEnum
	kStringType                   =14595      # from enum ValueTypeEnum
	kAngleUnits                   =94977      # from enum ValueUnitsTypeEnum
	kAngularVelocityUnits         =94978      # from enum ValueUnitsTypeEnum
	kAreaUnits                    =94979      # from enum ValueUnitsTypeEnum
	kCurrentUnits                 =94980      # from enum ValueUnitsTypeEnum
	kForceUnits                   =94981      # from enum ValueUnitsTypeEnum
	kLengthUnits                  =94982      # from enum ValueUnitsTypeEnum
	kMassUnits                    =94983      # from enum ValueUnitsTypeEnum
	kPowerUnits                   =94984      # from enum ValueUnitsTypeEnum
	kPressureUnits                =94985      # from enum ValueUnitsTypeEnum
	kSpeedUnits                   =94986      # from enum ValueUnitsTypeEnum
	kTemperatureUnits             =94987      # from enum ValueUnitsTypeEnum
	kTimeUnits                    =94988      # from enum ValueUnitsTypeEnum
	kUnitless                     =94989      # from enum ValueUnitsTypeEnum
	kVoltageUnits                 =94990      # from enum ValueUnitsTypeEnum
	kVolumeUnits                  =94991      # from enum ValueUnitsTypeEnum
	kWorkUnits                    =94992      # from enum ValueUnitsTypeEnum
	kAlignTextBaseline            =25604      # from enum VerticalTextAlignmentEnum
	kAlignTextLower               =25603      # from enum VerticalTextAlignmentEnum
	kAlignTextMiddle              =25601      # from enum VerticalTextAlignmentEnum
	kAlignTextUpper               =25602      # from enum VerticalTextAlignmentEnum
	kModelOriginInsertion         =86786      # from enum ViewBlockInsertionPointEnum
	kViewCenterInsertion          =86785      # from enum ViewBlockInsertionPointEnum
	kCenteredViewJustification    =67073      # from enum ViewJustificationEnum
	kFixedViewJustification       =67074      # from enum ViewJustificationEnum
	kBottomLeftViewCorner         =41475      # from enum ViewLayoutEnum
	kBottomRightViewCorner        =41476      # from enum ViewLayoutEnum
	kTopLeftViewCorner            =41473      # from enum ViewLayoutEnum
	kTopRightViewCorner           =41474      # from enum ViewLayoutEnum
	kPanViewOperation             =30210      # from enum ViewOperationTypeEnum
	kRotateViewOperation          =30209      # from enum ViewOperationTypeEnum
	kZoomViewOperation            =30211      # from enum ViewOperationTypeEnum
	kArbitraryViewOrientation     =10763      # from enum ViewOrientationTypeEnum
	kBackViewOrientation          =10756      # from enum ViewOrientationTypeEnum
	kBottomViewOrientation        =10757      # from enum ViewOrientationTypeEnum
	kCurrentViewOrientation       =10765      # from enum ViewOrientationTypeEnum
	kDefaultViewOrientation       =10753      # from enum ViewOrientationTypeEnum
	kFlatBacksidePivot180ViewOrientation=10773      # from enum ViewOrientationTypeEnum
	kFlatBacksidePivotLeftViewOrientation=10772      # from enum ViewOrientationTypeEnum
	kFlatBacksidePivotRightViewOrientation=10771      # from enum ViewOrientationTypeEnum
	kFlatBacksideViewOrientation  =10770      # from enum ViewOrientationTypeEnum
	kFlatPivot180ViewOrientation  =10769      # from enum ViewOrientationTypeEnum
	kFlatPivotLeftViewOrientation =10768      # from enum ViewOrientationTypeEnum
	kFlatPivotRightViewOrientation=10767      # from enum ViewOrientationTypeEnum
	kFrontViewOrientation         =10764      # from enum ViewOrientationTypeEnum
	kIsoBottomLeftViewOrientation =10762      # from enum ViewOrientationTypeEnum
	kIsoBottomRightViewOrientation=10761      # from enum ViewOrientationTypeEnum
	kIsoTopLeftViewOrientation    =10760      # from enum ViewOrientationTypeEnum
	kIsoTopRightViewOrientation   =10759      # from enum ViewOrientationTypeEnum
	kLeftViewOrientation          =10758      # from enum ViewOrientationTypeEnum
	kRightViewOrientation         =10755      # from enum ViewOrientationTypeEnum
	kSavedCameraViewOrientation   =10766      # from enum ViewOrientationTypeEnum
	kTopViewOrientation           =10754      # from enum ViewOrientationTypeEnum
	kAllComponentsViewPreview     =70657      # from enum ViewPreviewTypeEnum
	kBoundingBoxViewPreview       =70659      # from enum ViewPreviewTypeEnum
	kPartialViewPreview           =70658      # from enum ViewPreviewTypeEnum
	kBrowserViewType              =9219       # from enum ViewTypeEnum
	kGraphicsViewType             =9218       # from enum ViewTypeEnum
	kNoteBookViewType             =9220       # from enum ViewTypeEnum
	kUnknownViewType              =9217       # from enum ViewTypeEnum
	kAssemblyFeatureGroup         =35073      # from enum WeldmentFeatureGroupEnum
	kMachiningFeatureGroup        =35076      # from enum WeldmentFeatureGroupEnum
	kPreperationsFeatureGroup     =35074      # from enum WeldmentFeatureGroupEnum
	kWeldsFeatureGroup            =35075      # from enum WeldmentFeatureGroupEnum
	kAssemblyWeldmentState        =80897      # from enum WeldmentStateEnum
	kMachiningWeldmentState       =80898      # from enum WeldmentStateEnum
	kPreparationsWeldmentState    =80900      # from enum WeldmentStateEnum
	kWeldsWeldmentState           =80899      # from enum WeldmentStateEnum
	kMaximize                     =32514      # from enum WindowsSizeEnum
	kMinimize                     =32515      # from enum WindowsSizeEnum
	kNormalWindow                 =32513      # from enum WindowsSizeEnum
	kAnalyticEdgeWorkAxis         =12555      # from enum WorkAxisDefinitionEnum
	kAssemblyWorkAxis             =12552      # from enum WorkAxisDefinitionEnum
	kFixedWorkAxis                =12551      # from enum WorkAxisDefinitionEnum
	kLineAndPlaneWorkAxis         =12550      # from enum WorkAxisDefinitionEnum
	kLineAndPointWorkAxis         =12554      # from enum WorkAxisDefinitionEnum
	kLineWorkAxis                 =12545      # from enum WorkAxisDefinitionEnum
	kNormalToSurfaceWorkAxis      =12553      # from enum WorkAxisDefinitionEnum
	kPointAndPlaneWorkAxis        =12549      # from enum WorkAxisDefinitionEnum
	kRevolvedFaceWorkAxis         =12548      # from enum WorkAxisDefinitionEnum
	kTwoPlanesWorkAxis            =12546      # from enum WorkAxisDefinitionEnum
	kTwoPointsWorkAxis            =12547      # from enum WorkAxisDefinitionEnum
	kAssemblyWorkPlane            =12044      # from enum WorkPlaneDefinitionEnum
	kFixedWorkPlane               =12041      # from enum WorkPlaneDefinitionEnum
	kLineAndPointWorkPlane        =12035      # from enum WorkPlaneDefinitionEnum
	kLineAndTangentWorkPlane      =12039      # from enum WorkPlaneDefinitionEnum
	kLinePlaneAndAngleWorkPlane   =12037      # from enum WorkPlaneDefinitionEnum
	kNormalToCurveWorkPlane       =12042      # from enum WorkPlaneDefinitionEnum
	kPlaneAndOffsetWorkPlane      =12038      # from enum WorkPlaneDefinitionEnum
	kPlaneAndPointWorkPlane       =12036      # from enum WorkPlaneDefinitionEnum
	kPlaneAndTangentWorkPlane     =12040      # from enum WorkPlaneDefinitionEnum
	kPointAndTangentWorkPlane     =12045      # from enum WorkPlaneDefinitionEnum
	kThreePointsWorkPlane         =12033      # from enum WorkPlaneDefinitionEnum
	kTorusMidPlaneWorkPlane       =12046      # from enum WorkPlaneDefinitionEnum
	kTwoLinesWorkPlane            =12034      # from enum WorkPlaneDefinitionEnum
	kTwoPlanesWorkPlane           =12043      # from enum WorkPlaneDefinitionEnum
	kAssemblyWorkPoint            =12808      # from enum WorkPointDefinitionEnum
	kCentroidWorkPoint            =12811      # from enum WorkPointDefinitionEnum
	kCurveAndEntityWorkPoint      =12807      # from enum WorkPointDefinitionEnum
	kFixedWorkPoint               =12806      # from enum WorkPointDefinitionEnum
	kLineAndFaceWorkPoint         =12803      # from enum WorkPointDefinitionEnum
	kMidPointWorkPoint            =12805      # from enum WorkPointDefinitionEnum
	kNonLinearEdgeWorkPoint       =12809      # from enum WorkPointDefinitionEnum
	kPointWorkPoint               =12804      # from enum WorkPointDefinitionEnum
	kSphereCenterPointWorkPoint   =12812      # from enum WorkPointDefinitionEnum
	kThreePlanesWorkPoint         =12801      # from enum WorkPointDefinitionEnum
	kTorusCenterPointWorkPoint    =12810      # from enum WorkPointDefinitionEnum
	kTwoLinesWorkPoint            =12802      # from enum WorkPointDefinitionEnum
	kZoomTargetAll                =55811      # from enum ZoomTargetComponentWithiMateEnum
	kZoomTargetNone               =55809      # from enum ZoomTargetComponentWithiMateEnum
	kZoomTargetPlacedComponent    =55810      # from enum ZoomTargetComponentWithiMateEnum
	kCurrentInventorVersionHiveCU =2565       # from enum _RegistryHiveTypeEnum
	kHKEY_CLASSES_ROOT            =2562       # from enum _RegistryHiveTypeEnum
	kHKEY_CURRENT_USER            =2564       # from enum _RegistryHiveTypeEnum
	kHKEY_LOCAL_MACHINE           =2563       # from enum _RegistryHiveTypeEnum
	kInventorHiveCU               =2561       # from enum _RegistryHiveTypeEnum
	kInventorHiveLM               =2560       # from enum _RegistryHiveTypeEnum
	kHalfOpenedSegState           =2          # from enum _SegmentLoadState
	kLoadedSegState               =8          # from enum _SegmentLoadState
	kNotOpenSegState              =0          # from enum _SegmentLoadState
	kOpenedSegState               =4          # from enum _SegmentLoadState
	kPreOpenedSegState            =1          # from enum _SegmentLoadState
	kAdaptiveColumn               =88074      # from enum iComponentColumnTypeEnum
	kBOMQuantityColumn            =88067      # from enum iComponentColumnTypeEnum
	kBOMStructureColumn           =88066      # from enum iComponentColumnTypeEnum
	kExclusionColumn              =88070      # from enum iComponentColumnTypeEnum
	kFilePropertyColumn           =88068      # from enum iComponentColumnTypeEnum
	kFlatPatternBendOrderColumn   =88079      # from enum iComponentColumnTypeEnum
	kFlatPatternOrientationColumn =88078      # from enum iComponentColumnTypeEnum
	kGroundedColumn               =88073      # from enum iComponentColumnTypeEnum
	kMemberNameColumn             =88065      # from enum iComponentColumnTypeEnum
	kParameterValueColumn         =88069      # from enum iComponentColumnTypeEnum
	kSheetMetalRuleColumn         =88080      # from enum iComponentColumnTypeEnum
	kSheetMetalUnfoldColumn       =88081      # from enum iComponentColumnTypeEnum
	kThreadClassColumn            =88084      # from enum iComponentColumnTypeEnum
	kThreadDesignationColumn      =88083      # from enum iComponentColumnTypeEnum
	kThreadDirectionColumn        =88085      # from enum iComponentColumnTypeEnum
	kThreadPipeDiameterColumn     =88086      # from enum iComponentColumnTypeEnum
	kThreadTypeColumn             =88082      # from enum iComponentColumnTypeEnum
	kUnknownColumn                =88087      # from enum iComponentColumnTypeEnum
	kiComponentTableReplaceColumn =88071      # from enum iComponentColumnTypeEnum
	kiFeatureTableReplaceColumn   =88072      # from enum iComponentColumnTypeEnum
	kiMateMatchingListColumn      =88076      # from enum iComponentColumnTypeEnum
	kiMateMatchingNameColumn      =88075      # from enum iComponentColumnTypeEnum
	kiMateSequenceNumberColumn    =88077      # from enum iComponentColumnTypeEnum
	kiFeatureEntityInputTypeCircularEdge=32         # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeCircularSketchCurve=512        # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeConicalSurface=65536      # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeCylindricalSurface=32768      # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeEllipticalSketchCurve=1024       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeGenericEdge=8          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeGenericSketchCurve=128        # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeGenericSurface=16384      # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeLinearEdge=16         # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeLinearSketchCurve=256        # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypePlanarFace=4096       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeSketchPoint=2          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeSphericalSurface=131072     # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeSplineSketchCurve=2048       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeToroidalSurface=262144     # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeUnknown=0          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeVertex=1          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeWorkAxis=64         # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeWorkPlane=8192       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeWorkPoint=4          # from enum iFeatureEntityInputTypeEnum
	kParamLimitList               =33283      # from enum iFeatureParamLimitTypeEnum
	kParamLimitNone               =33281      # from enum iFeatureParamLimitTypeEnum
	kParamLimitRange              =33282      # from enum iFeatureParamLimitTypeEnum

RecordMap = {
	u'tagSTATSTG': '{00000000-0000-0000-0000-000000000000}',
}

CLSIDToClassMap = {}
CLSIDToPackageMap = {
	'{88B090C2-BD7E-47CC-89D3-AA683A3E0297}' : u'DriveConstraintSettings',
	'{5B7A8CDA-6F27-4396-9E39-C21A67CA03D3}' : u'TwoDistancesChamferDef',
	'{75A1BC5F-78FC-4E62-99C7-623813E36C43}' : u'FlatPatternFeatures',
	'{151E96E1-59DA-4732-B025-4AA7A1C9AF27}' : u'Columns',
	'{3098A39F-CCD6-4163-8ADC-2E9504F3E00C}' : u'ExtrudeDefinition',
	'{148682B7-6B44-4FF0-8C10-AB21D276602E}' : u'BOMRow',
	'{CA8E18AF-5EA2-4A45-BA43-FF3914C5C200}' : u'FileManagerEventsSink',
	'{4A1FD94B-337F-43F7-AA7C-BA33B076B1EB}' : u'DrawingViewEvents',
	'{6F9AAB22-31DC-4F5A-98ED-8A8693D5BD1C}' : u'CircularOccurrencePattern',
	'{5FCCBA74-9BA4-49C7-95D3-FC9E7D76EFB3}' : u'ModelSurfaceTextureSymbols',
	'{903F1E1B-1A0E-4344-820B-CDD9619C0FDC}' : u'ImportedComponentDefinition',
	'{29049E48-996E-4799-8DA6-778A0B82AB54}' : u'iAssemblyMember',
	'{EEB73D62-BB10-4FDA-84B2-B27521C833A1}' : u'OrdinateDimensions',
	'{61B9A367-8CCB-4868-A573-CCE62C5C35B6}' : u'DerivedAliasComponent',
	'{BBF9FDF1-52DC-11D0-8C04-0800090BE8EC}' : u'_DrawingDocument',
	'{FD9487E1-57A9-419B-A365-14323D1B1CD9}' : u'ObjectCollectionByVariant',
	'{063D7617-E630-4D35-B809-64D6695F57C0}' : u'SketchOffsetSpline',
	'{8B72B033-1F46-4D07-8B26-6E9A718A1533}' : u'CornerChamferFeature',
	'{D2E7C9A2-CB9A-4619-B0AA-B7BA2870CDEE}' : u'DerivedAssemblyComponentProxy',
	'{114E3531-FE3B-4042-A454-372A6B98F26F}' : u'PointGraphics',
	'{8415AC9D-CA60-4AD8-8F79-CE03F00F573D}' : u'ChamferDefinition',
	'{611EDF7B-009C-4871-B3F9-69E1B4A61C1E}' : u'InventorVBAComponent',
	'{748041B9-77F8-481D-BADA-8F03152C3AF1}' : u'SmoothConstraint3DProxy',
	'{B76D6529-D84D-4A66-8215-58B6A32D56A9}' : u'iAssemblyFactory',
	'{EB213A42-0727-48F0-9BCF-C55F6CB4CD78}' : u'FileOptions',
	'{D07B4A7B-08EE-4CEA-BC85-525E882714BC}' : u'ThickenFeatureProxy',
	'{682CEB3B-365E-4863-B103-BCC368FBA896}' : u'FeatureControlFrames',
	'{97D6B280-1D62-48E6-B4B9-007F25F7A3A5}' : u'BoundaryPatchFeatures',
	'{BEB3104E-2019-49E0-BC17-F5759998D9FE}' : u'ControlDefinitionEvents',
	'{B4298554-2144-4054-A4EA-81888D6F6997}' : u'FeaturePatternElementProxy',
	'{2D0B10A8-711C-4352-AEE1-C8465CBDC36B}' : u'CombineFeature',
	'{E139EE45-18F4-404E-972E-08C6008BD225}' : u'FaceOffsetFeatureProxy',
	'{06AC6A50-B820-406B-995A-DDA0CCE3E2F5}' : u'LinearHolePlacementDefinition',
	'{425458DA-4495-11D3-B791-0060B0F159EF}' : u'AddInAutomation',
	'{B0E8CB6F-9451-4AFC-B8D3-A157ACDCBB0F}' : u'LinearGeneralDimension',
	'{6C312B38-95D8-47B3-A6A8-78942F77A1C7}' : u'LineGraphics',
	'{1D23FF98-1FB3-434F-847F-452217821819}' : u'Sketch3DSettings',
	'{BC450138-0F96-4342-BC2C-239747CD4797}' : u'SketchBlockDefinitions',
	'{BC1B0D6F-086B-43CC-91CC-6BEF7D7E35C1}' : u'MoveOperation',
	'{26EC46CE-6FFC-4605-8BB0-5C6198790433}' : u'MouseEvents',
	'{2B24FE45-C9E2-4590-BA7E-F7DB0E5A683F}' : u'MemberManager',
	'{6025C779-5DFB-4B1D-B2C9-E7CDD5D18B5F}' : u'RotateRotateiMateDefinition',
	'{4A558EB0-274A-4EF6-90A0-222A720A778E}' : u'FeatureControlFrameRows',
	'{A7993C2A-CFCA-4455-BC79-B15952DBF102}' : u'SketchFillRegions',
	'{7DF3C716-A1C7-4D3F-83C0-5D06A3D7F05C}' : u'MiniToolbarDropdownObject',
	'{2DB692B1-9CA2-40CA-AD6B-D1250C063724}' : u'iPartMember',
	'{F8B3014D-CA2D-40F4-B2A3-FA00E23105A1}' : u'EdgeDefinition',
	'{2D5EB497-6E4D-4B66-B185-EB6C7C188F2F}' : u'PointCloudCrop',
	'{1734EB03-2921-11D5-A4C1-00C04F6B9531}' : u'AttributeSetsEnumerator',
	'{1734EB04-2921-11D5-A4C1-00C04F6B9531}' : u'AttributesEnumerator',
	'{F7844415-30E0-4507-8BC0-F8AF990B3B38}' : u'MiniToolbarComboBoxObject',
	'{53196161-A966-4EE7-9080-3F75C7D5876D}' : u'ImportedGenericComponentDefinition',
	'{08A3AC40-A684-4F8B-8033-7D0FE23AFBE3}' : u'SketchBlock',
	'{4195A929-D003-467F-ADC6-11FB53A103EA}' : u'UserInterfaceEvents',
	'{1405C19D-F8AC-41AD-AAB2-D0923BD45C15}' : u'ReferenceKeyManager',
	'{098FDC37-8060-4944-AD0E-B55FEC55CA8C}' : u'DiameterModelDimension',
	'{A9C5B884-2122-4DBB-A94E-EB75ED78A160}' : u'SketchBlocks',
	'{2BFE4397-C369-4CEF-90C9-D5C8AE90BC9F}' : u'TransientBRep',
	'{F3C8A2A2-E9DF-454D-8769-8544374BB882}' : u'Welds',
	'{2CB6EA8B-44E3-4C93-BB2A-531D62EBD934}' : u'ContentTreeViewNodesEnumerator',
	'{839AA92C-F073-4BB6-9657-51061150E17C}' : u'CameraEventsSink',
	'{ACC86380-BE3B-48F1-A3D0-91E6ED2E2A82}' : u'OrdinateDimensionSets',
	'{66D547CF-949A-4B31-BC1B-AF002DC97D2B}' : u'DocumentSubTypeHandler',
	'{37076B79-AB7A-4E6B-8E9D-8D68D28C272E}' : u'CornerOptions',
	'{C032137F-6434-40C1-8DEC-763A191D1EE0}' : u'GripSnapOptions',
	'{892AF496-C31A-431A-9B15-39FA10940A86}' : u'AutoCADBlockDefinitionsEnumerator',
	'{3D70E84F-AC86-4734-8A36-1672FE750893}' : u'_SweepDefinition',
	'{EB143431-FB4F-4B4B-BDDA-C21026571456}' : u'ModelDatumIdentifier',
	'{77244784-A1C1-429E-A61F-E6E480B8DFEF}' : u'iFeatureSketchPlaneInput',
	'{92E91440-9FEA-11D6-8E0B-0010B541CAA8}' : u'_AssemblySolverNodeObject',
	'{E405BACE-0EE8-4427-B6BE-82CC11F9CC35}' : u'MapPointCurves',
	'{BEE271DA-318F-471D-AF24-296B6F59B392}' : u'FileMetadata',
	'{92E91460-9FEA-11D6-8E0B-0010B541CAA8}' : u'_AssemblySolverNode',
	'{3FD23B6F-222D-485D-A9E8-164C497B17F8}' : u'FaceOffsetFeatures',
	'{D39AB98F-45E0-4CAE-A0F2-4490804F2AD3}' : u'Sketch3DOptions',
	'{1A60195B-72BF-4714-9392-1212EC6260CB}' : u'FeaturePatternElement',
	'{73F35CC7-ED6E-11D2-B785-0060B0F159EF}' : u'PropertySet',
	'{73F35CC8-ED6E-11D2-B785-0060B0F159EF}' : u'PropertySets',
	'{73F35CC9-ED6E-11D2-B785-0060B0F159EF}' : u'Property',
	'{3C75ADFE-18C0-42BF-A83D-D0E539BD1F7D}' : u'MeasureEventsSink',
	'{90821476-EE63-4328-BC9F-164D0BBF6F9C}' : u'iAssemblyTableColumn',
	'{33E293A8-9DD6-4B9A-8274-E436A3BB3876}' : u'HelicalConstraint3D',
	'{F6A7B996-5EB9-4DC4-99D9-3919C36FB802}' : u'MiniToolbarButtonObject',
	'{0134748C-7F24-467B-9DF2-6647677B125F}' : u'DimensionStylesEnumerator',
	'{C534F040-9826-411E-8C6F-4A73C3A998FC}' : u'DoubleHemDefinition',
	'{1BFD9261-5C05-4BF4-9A9F-F5323F3C8E69}' : u'AngularModelDimension',
	'{830E9463-F267-4A8E-8CE5-8D417295459D}' : u'FlatPatternOrientation',
	'{2E19A8EE-1E70-4AE4-8C1E-06DAE3BBABB2}' : u'SelectEventsSink',
	'{124B76C3-CB79-4414-9CB9-DDA2F8C5C90A}' : u'ModelingEventsSink',
	'{D2CF1030-CA32-48F6-8865-298BE7E11CCC}' : u'IntersectionCurveProxy',
	'{7A7BD889-E944-41FC-A34F-474465F0894E}' : u'SketchEllipses3D',
	'{4D29B490-49B2-11D0-93C3-7E0706000000}' : u'_PartDocument',
	'{3D7599FE-1A8A-47D8-A353-5C48B819A55D}' : u'MiniToolbarCheckBoxObject',
	'{817C825E-2D55-4E09-A69E-789E9753959D}' : u'ColorSchemes',
	'{109C1DF4-2290-44AC-9E90-A108D090B4E9}' : u'TrimFeatures',
	'{321D3FD9-A57F-4CDE-AD39-FD1EEE22543C}' : u'DerivedParameterTables',
	'{325CFE17-8D9E-4977-A3B3-97AC9D827CD9}' : u'FilletSetback',
	'{D136B45B-7B03-4027-9759-AECD06393300}' : u'WorkSurface',
	'{8AF87EC1-B613-43DB-9FF6-E0D489B68DAE}' : u'Row',
	'{92E914D0-9FEA-11D6-8E0B-0010B541CAA8}' : u'_AssemblySolver',
	'{12A24FCF-4CBD-403D-9E32-ECE5DC3297E9}' : u'BOMViews',
	'{7E2A1EB5-F770-45BD-8DC5-8FEE60664D9F}' : u'SculptFeature',
	'{0466D05C-72BF-45E4-A1C6-3FA76AF8812C}' : u'TriadEventsObject',
	'{453A1005-42C9-469C-847E-CEA7D550751B}' : u'RipDefinition',
	'{98E6F703-DF38-4C29-85A2-A8266869668E}' : u'LibrarySketchedSymbolDefinitions',
	'{ACE59077-7778-11D4-8DD8-0010B541CAA8}' : u'DocumentsEnumerator',
	'{3F35DB6C-C158-4203-B420-AE4ABCC4B908}' : u'ImportedModelEntity',
	'{A267D26D-EA7D-444F-8D54-7316BF10DD96}' : u'Wire',
	'{C173A08D-012F-11D5-8DEA-0010B541CAA8}' : u'LineSegment2d',
	'{9ADC4649-06DC-449E-ABE8-5DCA6F4C7788}' : u'StringAssetValue',
	'{A77799B5-136D-4FEB-9902-CAEC8E122A24}' : u'RipFeatureProxy',
	'{B5E1C129-EE0E-4C45-9AC3-FE79794F1EB0}' : u'TriangleGraphics',
	'{A80294E5-6638-47F4-948A-A31A9F9CBC36}' : u'HoleTableColumns',
	'{4CDC6B45-25DB-442E-BF8B-12C87365788E}' : u'DeleteFaceFeature',
	'{EA1D0D38-93AD-48BB-84AC-7707FAC29BAF}' : u'FaceDraftFeature',
	'{62F1DC23-FB86-4D0C-81B3-05BF2CD775F4}' : u'AssemblyWorkPlaneDef',
	'{21F3FEA8-2DF7-47B5-9C4C-33BB28E97D1C}' : u'SelectEventsObject',
	'{7430CE13-37A3-4A67-A645-2AAD0BB71038}' : u'ModelLeaderNode',
	'{C75F478E-81C5-4E92-BC2A-630E598E34E5}' : u'ExtrudeFeatureProxy',
	'{BED3CF92-D335-4DC0-BA98-76F2E8A6A963}' : u'OGSSceneNode',
	'{550A5700-23FB-4E1F-98D6-5BD7D9701ACD}' : u'UnfoldFeatureProxy',
	'{DBC99CB5-8EB0-4D45-BAC7-DE9D532FDD04}' : u'MiniToolbarObject',
	'{D9AB7AE5-6A67-4165-9E0B-0F008C9135B0}' : u'HemFeature',
	'{CD675FA9-2F1B-4574-B287-C0C601CCC1B1}' : u'ModelFeatureControlFrameDefinition',
	'{E8DC5B4C-F562-4911-AFBC-41961F55C140}' : u'OGSSceneNodesEnumerator',
	'{9A14B139-7101-40B1-BD92-B3F9870DC7F0}' : u'DesignProject',
	'{0218B59B-0CE5-4CA1-9A3B-F7D266C4E75F}' : u'DecalFeatures',
	'{8D41F569-6407-4C82-A25E-762F6F8AA4B9}' : u'SpiralCoilExtent',
	'{D3CB21DB-DF14-45FC-ADD6-8E8EED0AECC3}' : u'LoftFeatureProxy',
	'{D2653F5F-C73A-4FAE-9172-EA1B60098B07}' : u'ImportedGenericComponent',
	'{920C0497-59BF-4F6C-A45C-8C8AA72750CF}' : u'SketchFillRegion',
	'{48D3D9AD-F3F0-41E8-B4D8-6DA2533CCFC9}' : u'IntegerAssetValue',
	'{3C934EFD-E26A-4940-BA5A-66908C16AA92}' : u'DimensionConstraints3D',
	'{1B63BB78-7EC2-4D21-A312-A867DCF54110}' : u'RestFeatureProxy',
	'{02BCE85C-478B-4A66-8668-6579602A0EB6}' : u'SketchSettings',
	'{5FDB5E25-C96F-11D5-8DF9-0010B541CAA8}' : u'Sketch',
	'{F21B5BBF-DBA8-480A-95A6-83D27D52343B}' : u'iFeatureWorkPlaneInput',
	'{06C9E562-0C16-4D86-8EB7-2513D279C81C}' : u'MiniToolbarButton',
	'{E205D028-CE6C-4BE5-AE33-AB6F9770D869}' : u'TorusCenterPointWorkPointDef',
	'{9F512CF6-D755-4539-A0A5-E346F4B89AE1}' : u'Lights',
	'{68BC4B61-96FC-4D5D-B4B5-10AEAC7EC05A}' : u'TriadEvents',
	'{AE99EE3F-A9E9-498C-AE33-C919105745F4}' : u'Bend',
	'{F2BD70CA-061C-45C4-B057-88526074C390}' : u'CameraEventsObject',
	'{5194100D-435F-4C85-A922-6BD3E4CC9C36}' : u'ModelLeaderNote',
	'{1426BDF8-DD91-4FF0-AD8D-BB0EC8797B24}' : u'KnitFeatures',
	'{A36A7AD1-DDBD-4858-B025-D3F6C2042BC8}' : u'DrawingBOMColumn',
	'{77D4A0A3-255E-42A8-B0F5-41FE5007BCCE}' : u'Leader',
	'{089C1D07-A3A6-4649-B1C4-CE9DAB1D8BBE}' : u'ModelAnnotation',
	'{F828B7C4-4B02-4B69-8D22-8BC7BA9D6243}' : u'SurfaceTextureSymbols',
	'{7CD6C780-663E-4187-8D35-D132C99F6918}' : u'FeatureControlFrameRow',
	'{0B13DE4E-2371-408F-AF1A-F884A9061ED9}' : u'ContentCenterConfiguration',
	'{9533BA5C-A32F-45DA-AE06-32EBE35E8CFF}' : u'BendConstraintProxy',
	'{863F993F-413C-4965-B391-CE4CF47616DB}' : u'DockableWindowsEventsSink',
	'{A19C2D06-4C43-41EC-93EB-AD104ABEE1B9}' : u'PathEntityProxy',
	'{DBD3CBEE-DBBC-4A71-B122-33A8D1786D20}' : u'DocumentDescriptorsEnumerator',
	'{AFA9F4D2-A1D8-42C3-8BFA-994FFAB1BEA4}' : u'GraphicsColorMapper',
	'{F829B171-412E-4642-8034-AEC013FCFDC5}' : u'PartsListStylesEnumerator',
	'{32F5072E-8F1B-4889-898F-A512619D7D74}' : u'MiniToolbarTextEditorSink',
	'{E3571293-DB40-11D2-B783-0060B0F159EF}' : u'ApplicationAddInServer',
	'{E3571299-DB40-11D2-B783-0060B0F159EF}' : u'ApplicationAddInSite',
	'{1112CDE3-CD39-4004-8E74-0C019C73F380}' : u'OccurrencePatterns',
	'{5B9228F3-FB28-487E-9EC2-D948901CA89F}' : u'SheetMetalStyles',
	'{4B427038-81A6-4E75-A633-CF7CCBDD8160}' : u'WireEdgeDefinitions',
	'{5BC0F92E-9C6A-4887-9B29-E1831F845DB2}' : u'ChainDimensionSet',
	'{C5AC2A12-6439-4CB5-BA1E-45765296285E}' : u'ComponentDefinitionsEnumerator',
	'{FBCADB33-9CBE-11D3-B799-0060B0F159EF}' : u'DataIO',
	'{289220CD-E245-473D-B626-114D97F9EDCB}' : u'CornerRoundEdgeSet',
	'{87F4CA2E-5700-4FC7-A283-8E2D90FE5F61}' : u'RevolveFeature',
	'{3B809336-2821-4E36-B2A1-31B987537E57}' : u'CutDefinition',
	'{CABA7470-1B47-492D-A62E-EE7213257C05}' : u'ClientBrowserNodeDefinitionObject',
	'{531B0D86-9BDA-4992-8D31-C42A8788000B}' : u'MateConstraintProxy',
	'{EF97259E-0689-42D1-AFAC-1FFD9F6A1980}' : u'DWGSplineProxy',
	'{0F6DEA5E-48E4-49BE-854E-164A89406DDC}' : u'HemFeatureProxy',
	'{ADE1D7A7-3CF2-49E7-8476-79677765D850}' : u'CustomParameterGroups',
	'{734FDACC-45FD-487A-AC60-02CE0522FF00}' : u'RibbonTab',
	'{CCEBC8A5-7171-47B6-B9DC-067DAC0C79E7}' : u'WebView',
	'{38C1B59A-0C1B-4076-A22C-291C34157BBD}' : u'SplitFeatureProxy',
	'{90ED1343-7C9E-4042-9664-93D821AF88CC}' : u'ModelHoleThreadNoteDefinition',
	'{A145B58E-E928-4180-951B-D7E652298E2A}' : u'BIMComponentProperty',
	'{C1516EB6-AEA2-412F-B1D0-9C609D152E21}' : u'HoleThreadNote',
	'{8C2CC3CF-A455-40D6-8505-56A702F6FB77}' : u'GraphicsDataSetsCollection',
	'{A44AF926-6383-42F0-8B2D-253F82F95ABE}' : u'FileManagerEvents',
	'{D4B12468-31B2-4885-BE17-B55DE2D561AF}' : u'SketchCircle3DProxy',
	'{5874F2D8-29C2-4D48-91C2-BB239564CF26}' : u'FaceDraftFeatureProxy',
	'{055EC022-CD9B-4983-97E2-2EC073939046}' : u'DSJoint',
	'{055EC023-CD9B-4983-97E2-2EC073939046}' : u'DSJointDefinition',
	'{055EC024-CD9B-4983-97E2-2EC073939046}' : u'DSDegreesOfFreedom',
	'{055EC025-CD9B-4983-97E2-2EC073939046}' : u'DSDegreeOfFreedom',
	'{055EC026-CD9B-4983-97E2-2EC073939046}' : u'DSResults',
	'{055EC027-CD9B-4983-97E2-2EC073939046}' : u'DSResult',
	'{ABD216FA-7559-4883-93D7-C0A9ECFF19C4}' : u'TransactionEventsObject',
	'{2B0F6166-711D-47E0-B9B1-54ED9E3F160B}' : u'ClientGraphics',
	'{85577108-087D-4E36-994A-48CA4F1D2AB9}' : u'UserCoordinateSystemProxy',
	'{652F6A52-8B8A-4CEF-B1DC-C78751914993}' : u'ModelParameters',
	'{9AA5A91E-286C-4F3E-A93D-863BAFD4B80C}' : u'SketchPoint3DProxy',
	'{498E2A5A-76DD-4059-BB54-300D026EC79D}' : u'ModelDatumIdentifiers',
	'{2A87493C-AFCD-42D8-A4AE-8385513E63E9}' : u'FlushiMateDefinitionProxy',
	'{127400A4-792F-4C40-892E-1AEEA1BBF1E2}' : u'EnumType',
	'{CDF65ADD-9C11-4AB9-8F2E-AB6F83FED7C2}' : u'OccurrencePatternElements',
	'{25FF655F-9C78-4C55-9166-51E299DB6565}' : u'IntersectionCurve',
	'{0BDE54D4-8527-46BE-B2DC-7E9A5AED8AB9}' : u'DerivedParameter',
	'{81F414A9-1062-46BB-A5EE-26575E90DCF0}' : u'ModelingSettings',
	'{DDB3F084-C3BC-4A46-8B6A-A169466514BF}' : u'HoleThreadNotes',
	'{0AD2B1BB-3410-4A43-9926-C3849F69FD2F}' : u'Trail',
	'{1EA98FE3-C2EA-4025-8B42-7F91BD2E8DFC}' : u'TwoLineAngleDimConstraint3D',
	'{96750E11-92EA-457A-BF5E-6FA15C44B8EE}' : u'ButtonDefinitionHandlerEventsSink',
	'{E8320E6D-E219-4F7C-954C-484A94137FD1}' : u'SinglePointRipTypeDef',
	'{D3067CC6-4526-4797-B62D-54AF0E415A47}' : u'DirectEditScaleOperation',
	'{2E264D50-AF7C-4FDE-96DA-12EBD46CAB9B}' : u'PointToPointRipTypeDef',
	'{3B39A185-9BED-4494-993C-26762D8A2D5F}' : u'DetailDrawingView',
	'{98675AD1-A109-43DE-A7D7-1612BC503E0E}' : u'iFeature',
	'{78F10980-2892-46CD-8F0E-B709A4835B9B}' : u'SculptFeatureProxy',
	'{3B71CB69-62FB-40D1-BEF9-3B0C255C8DD4}' : u'SketchEventsSink',
	'{C45BCCBE-2E53-4C8F-B76A-E6B7815E87E4}' : u'Materials',
	'{736ED1B9-7434-4044-B439-EEC1AA84CAAE}' : u'iFeatureProxy',
	'{BFB40FAA-DEC6-4C84-BBA2-8FD424F3C564}' : u'FamilyManager',
	'{F440685C-03F8-49FF-8B68-79E575AF5A5E}' : u'HeadsUpDisplayOptions',
	'{828DB6DB-AE56-4DB4-A765-216D9159A18C}' : u'RadialMarkingMenu',
	'{BAB06F80-7165-484C-88DF-7D8A0004A76D}' : u'InventorVBAArguments',
	'{89444C1E-456C-4684-B029-3A5E3A89988C}' : u'SelectEvents',
	'{BC329A16-2294-4C2D-AEAC-AE61F5433C7B}' : u'DirectEditScaleOperationProxy',
	'{CF66D521-D40D-477C-A686-D2D5A614D323}' : u'IntentConfiguration',
	'{8D389B94-12D9-4150-BC67-B64B560E743F}' : u'ContourFlangeDefinition',
	'{3B833858-7410-47C9-BCAD-F3BE5DEA191D}' : u'DirectEditMoveOperationProxy',
	'{5F9B0BEB-E30C-4750-A733-1FCFE4218750}' : u'DWGEntitiesEnumerator',
	'{1470BE5E-D0B2-4177-A484-3528D6B0FC37}' : u'ThreadInfo',
	'{31B11F76-0E31-45DF-8BE6-409EE5416DC5}' : u'Wires',
	'{C7CECA91-B8BD-4C0E-A998-FBFD9BE85416}' : u'MessageSection',
	'{37697A9E-01B1-4581-B52D-B8758FBA364E}' : u'Centermark',
	'{EAADC3AE-D599-495E-A56C-FA79AE3E8848}' : u'SculptFeatures',
	'{62F5FBCA-EC38-48F5-9CA7-1D38FED4D443}' : u'iFeatureComponents',
	'{FA39B171-CAA5-4FB2-94D0-4E0DF357D13E}' : u'Sketch3DProxy',
	'{67BD386A-CC79-48F0-BCFF-6C25FFBF59AA}' : u'FaceFeatureDefinition',
	'{837D8FB2-848D-4A3B-8F83-ECCFDCAC2766}' : u'MoveFaceFeature',
	'{C9216F3D-E886-4E75-89AB-D7665FA14AB1}' : u'DrawingViewLabel',
	'{C7A68C71-14FA-11D6-8E01-0010B541CAA8}' : u'CoincidentConstraintProxy',
	'{79093216-BF48-46A2-9BFA-2D15CCB8BADD}' : u'MiniToolbarControls',
	'{7DBA9100-AFA9-407A-A91C-A9CC7A079565}' : u'CornerFeature',
	'{290EC1FE-2BB5-46E8-AB41-919D7455740D}' : u'iAssemblyTableCell',
	'{E51041E7-5DB6-4951-9F76-3ACA9B2E2A66}' : u'FileAccessEventsSink',
	'{8E3A45D9-4432-4408-B261-12E725F97A5D}' : u'AssemblyWorkPointDef',
	'{4C9E5B40-4741-4AD9-AACC-47C2BAD5E903}' : u'iPartTableColumns',
	'{5D81FF33-0E80-4FC7-A02B-D955952B2EC9}' : u'AngularGeneralDimension',
	'{972006AB-5037-4850-AF98-8D3B5A55C1F4}' : u'MoveFeatures',
	'{20C36669-DC84-413C-84A7-4D0983BAD319}' : u'ContentTableColumn',
	'{C7A68CBB-14FA-11D6-8E01-0010B541CAA8}' : u'PlanarSketchProxy',
	'{4CD53A13-201C-402A-A729-EFEB24A1417C}' : u'BoundaryPatchLoops',
	'{C7A68CBF-14FA-11D6-8E01-0010B541CAA8}' : u'SketchPointProxy',
	'{96E36D73-DFEC-4CF8-9DB3-F97F01A41A23}' : u'OriginIndicator',
	'{C7A68CC1-14FA-11D6-8E01-0010B541CAA8}' : u'SketchArcProxy',
	'{C7A68CC3-14FA-11D6-8E01-0010B541CAA8}' : u'SketchSplineProxy',
	'{7B4F757F-55D3-4078-9AED-61AD15AC9AD5}' : u'ProjectPaths',
	'{C7A68CC5-14FA-11D6-8E01-0010B541CAA8}' : u'SketchEllipseProxy',
	'{C7A68CC7-14FA-11D6-8E01-0010B541CAA8}' : u'SketchEllipticalArcProxy',
	'{C7A68CC9-14FA-11D6-8E01-0010B541CAA8}' : u'SketchCircleProxy',
	'{C7A68CCB-14FA-11D6-8E01-0010B541CAA8}' : u'ProfileProxy',
	'{C7A68CCD-14FA-11D6-8E01-0010B541CAA8}' : u'ProfilePathProxy',
	'{C7A68CCF-14FA-11D6-8E01-0010B541CAA8}' : u'ProfileEntityProxy',
	'{0C946530-B275-481A-9573-6CA7D4F93611}' : u'ProjectOptionsButtonSink',
	'{8DE224FA-1DA2-4B05-BE2B-3E7FB6361FC2}' : u'AliasFreeformFeatureProxy',
	'{C7A68CD5-14FA-11D6-8E01-0010B541CAA8}' : u'SplineFitPointConstraintProxy',
	'{C7A68CD7-14FA-11D6-8E01-0010B541CAA8}' : u'OffsetConstraintProxy',
	'{C7A68CD9-14FA-11D6-8E01-0010B541CAA8}' : u'EqualLengthConstraintProxy',
	'{62246192-FF8D-4715-997D-09E760061B5C}' : u'ChangeProcessorObject',
	'{C7A68CDD-14FA-11D6-8E01-0010B541CAA8}' : u'GroundConstraintProxy',
	'{C7A68CDF-14FA-11D6-8E01-0010B541CAA8}' : u'HorizontalConstraintProxy',
	'{2FF370FA-BB1C-4C92-BB10-06D94CC8F8F3}' : u'UserParameters',
	'{C7A68CE1-14FA-11D6-8E01-0010B541CAA8}' : u'HorizontalAlignConstraintProxy',
	'{C6EEC114-BE48-4323-B58C-9DF90ED92996}' : u'ProjectAssetLibrary',
	'{C7A68CE3-14FA-11D6-8E01-0010B541CAA8}' : u'MidpointConstraintProxy',
	'{C7A68CE5-14FA-11D6-8E01-0010B541CAA8}' : u'ParallelConstraintProxy',
	'{C7A68CE7-14FA-11D6-8E01-0010B541CAA8}' : u'PerpendicularConstraintProxy',
	'{A89E388A-13C9-4FFA-B777-9C0E1C81F136}' : u'EndOfFeatures',
	'{C7A68CEB-14FA-11D6-8E01-0010B541CAA8}' : u'TangentSketchConstraintProxy',
	'{C7A68CED-14FA-11D6-8E01-0010B541CAA8}' : u'VerticalConstraintProxy',
	'{A957DFC5-7AC5-497F-A7AF-5438FAFAD6B4}' : u'TableStyle',
	'{C7A68CEF-14FA-11D6-8E01-0010B541CAA8}' : u'VerticalAlignConstraintProxy',
	'{C7A68CF1-14FA-11D6-8E01-0010B541CAA8}' : u'PatternConstraintProxy',
	'{C7A68CF3-14FA-11D6-8E01-0010B541CAA8}' : u'OffsetDimConstraintProxy',
	'{97B2D2E2-78EA-4838-B140-2BBAB4D8E7A9}' : u'HoleTableStyle',
	'{C7A68CF5-14FA-11D6-8E01-0010B541CAA8}' : u'TwoPointDistanceDimConstraintProxy',
	'{C7A68CF7-14FA-11D6-8E01-0010B541CAA8}' : u'TwoLineAngleDimConstraintProxy',
	'{EBB974BD-2A69-4125-899A-5752878B7E55}' : u'EnvironmentBaseHandlerObject',
	'{F7EDD327-75BC-4976-A0AE-7696B54D461D}' : u'FileOpenOptions',
	'{9CB10C50-7F27-4E55-BADE-15A308DB8820}' : u'FeatureControlFrameStyle',
	'{C7A68CFD-14FA-11D6-8E01-0010B541CAA8}' : u'RadiusDimConstraintProxy',
	'{C7A68CFF-14FA-11D6-8E01-0010B541CAA8}' : u'EllipseRadiusDimConstraintProxy',
	'{C7A68D01-14FA-11D6-8E01-0010B541CAA8}' : u'TangentDistanceDimConstraintProxy',
	'{165776AC-95DC-4BD0-8288-BE844390282F}' : u'EnvironmentBaseHandlerEventsSink',
	'{938C8A20-C60B-47C8-A9F4-CDAA7CE06095}' : u'SweepDefinition',
	'{58B0C13D-27CC-4F06-93FD-0524B69E6578}' : u'RectangularPatternFeature',
	'{6939FFDD-BA10-11D2-B779-0060B0F159EF}' : u'ObjectCollection',
	'{8F014D19-4B2F-4DD1-9010-FE75815C297C}' : u'SketchEllipse3D',
	'{186F6C0F-C3A2-4798-9685-C773181074C1}' : u'ReferenceAssetValue',
	'{6A89E379-03FC-440E-A655-6111E86247A1}' : u'iFeatureInput',
	'{1304BB1D-95AE-4738-80F8-CCCA1ABCFF6B}' : u'ReferenceParameters',
	'{A7E07EA5-369D-11D6-8E02-0010B541CAA8}' : u'FlatPattern',
	'{E4FA0888-2179-4CB4-9277-B103A9C40812}' : u'AssemblySymmetryConstraintProxy',
	'{237CB3F2-314E-4211-92DC-D69C15BF1B64}' : u'FilletConstantRadiusFaceSet',
	'{B534FD24-88CA-435C-95D5-F0DB0FB0238D}' : u'CosmeticBendFeatures',
	'{92A50081-D0B7-428F-BFF0-B0D277C3AEB0}' : u'TextBoxDefinitionHandler',
	'{66B08E3B-4411-44C0-9A17-2C818A5BB08F}' : u'TestConfiguration',
	'{AD4D6527-A103-4FF5-8433-FB90C52B9473}' : u'CentermarkStyle',
	'{3DC9DC2A-8A78-43BE-BDB5-E6F1162980BB}' : u'Centerlines',
	'{0E7B7C43-1EA3-4FA9-95ED-5A1370E81E3F}' : u'NonParametricBaseFeatureProxy',
	'{8378680D-EA06-405D-986A-8406E0E874B0}' : u'TestResults',
	'{744FFECE-189A-4ACC-8BCF-8F959D5E4EAE}' : u'Arc3d',
	'{50E1E017-584C-4C7D-8001-4CF9AEAB7E5E}' : u'DWGBlockDefinition',
	'{3DD6B742-71A1-438D-BB71-5CACFA2AACBE}' : u'ContentTreeViewNode',
	'{F3ACEE71-EC98-43F5-AC33-D0BDE47609EE}' : u'FaceDefinition',
	'{4594DFB7-06DB-4707-9F10-B42F740EE37D}' : u'FoldFeature',
	'{8C0B72C6-CFC6-4B2D-8A89-1DE890D9F65B}' : u'HoleTables',
	'{E09DAF1C-7738-4CDB-B26B-5DE6A2B37573}' : u'RigidBodyResults',
	'{FB1FDFB0-239C-4040-9B22-7ACACCFFE82E}' : u'BossSet',
	'{D8DEC5C0-4E92-4D60-B107-6D5FBBA9923A}' : u'WeldBead',
	'{D893A325-547B-4DE2-8F8B-BD9594025979}' : u'ReferenceKeyEvents',
	'{994CF5C9-F097-43AB-8741-76D5DD3DC2BA}' : u'CutFeatures',
	'{C0D71AC3-E085-4A0E-85FF-549C000BA1E7}' : u'FaceFeatures',
	'{F9B17D1C-6918-44FE-B072-7B4F00CD2BB3}' : u'FlangeFeatures',
	'{448C7AED-838C-44DB-87FC-2D18E74AA05A}' : u'FilletDefinition',
	'{1C4A4777-E52F-405F-BABA-7ED0931E81C0}' : u'RigidBodyJoints',
	'{F5BFBDBA-35EE-424D-A3AD-8D87B22484CF}' : u'HoleTapInfo',
	'{F393AB2C-8A8B-4B69-9F0D-91FFA842A53F}' : u'SketchBlockDefinition',
	'{5D21C290-CB28-4861-9367-C3F1B9F0BCCB}' : u'BrowserNode',
	'{5B29EB3A-F2F2-4998-B713-03042554E46C}' : u'TwoPointDistanceDimConstraint3DProxy',
	'{59E208A8-BB82-4322-92D6-DA364F8B9AB0}' : u'NonParametricBaseFeatures',
	'{55C72DAA-3307-43D6-89F0-CBF7DD348E4D}' : u'DrawingPrintManager',
	'{E16AEA74-FC21-4762-85D9-A4B20B06A095}' : u'CornerChamferDefinition',
	'{2F800161-0E4D-4953-A0B7-E55EE05E039B}' : u'MacroControlDefinition',
	'{5404EF69-8B8C-4CCF-BC9B-D9BC8B4F4A2E}' : u'LipFeature',
	'{460D3833-0485-4B61-8A1A-C9E8008FAFCC}' : u'DimensionConstraint3D',
	'{3D65F35E-2F1A-469E-9E5D-E02437A6E3BA}' : u'ReferenceFeatureProxy',
	'{4FDD2BD0-33C6-4EB0-90CE-4EEA2B181738}' : u'CollinearConstraint3DProxy',
	'{DCEF44A1-7A80-4A0A-937C-A349AF8A9233}' : u'SketchFixedSpline',
	'{0562B816-F05F-4293-AF39-D2F640E42740}' : u'SheetMetalComponentDefinition',
	'{04AAEAB9-6EAD-412C-B69A-D8EE4D924798}' : u'LeaderNote',
	'{C6E1E6AB-897D-4CDD-A486-4ABAA04FC9B9}' : u'AssetValue',
	'{7C6BCC40-95D1-4B47-AE7F-A5EBFEF95851}' : u'RadiusModelDimensions',
	'{A8E2C150-78E9-4E97-A4A0-BF43936B2A45}' : u'RectangularOccurrencePattern',
	'{01711A84-0018-4452-A736-D9292E754D38}' : u'ModelFeatureControlFrames',
	'{F5C82F4B-9B32-488E-920A-31F065B1AD77}' : u'AngleiMateDefinition',
	'{8A4D2830-7D4A-49E5-99BC-3E6C760463E7}' : u'DirectEditOperationProxy',
	'{D4F6BE55-A3E1-4420-BCBB-9E2E98A87226}' : u'OutOfProcessInventorServer',
	'{87DB004A-F974-4BFE-A8BD-65BA290F2D43}' : u'LoftedFlangeFeatureProxy',
	'{8DC730F1-A15F-4547-A279-69B7A9FAE657}' : u'EdgeCollection',
	'{4F599909-D43A-4090-BC23-3616A075A02D}' : u'ProjectOptionsButtonObject',
	'{70FCCBEE-EF8F-4917-98E0-B26399EAB6CE}' : u'MoveFeatureProxy',
	'{A6EC8B79-931A-409E-90CE-3EE28CB9F9F4}' : u'SaveOptions',
	'{28DD48C1-8D70-11D4-8DDE-0010B541CAA8}' : u'PointAndPlaneWorkAxisDef',
	'{239475B6-6DCA-4683-B410-A5788BF2077B}' : u'ImportedComponent',
	'{2C9F06C7-9124-43FE-B6D9-703620D53DA7}' : u'SketchBlocksEnumerator',
	'{CBE24DE3-529E-4039-BFDF-D014844691F0}' : u'RigidBodyGroups',
	'{1915251D-AC20-4EFC-A0EE-43FBEF266925}' : u'OGSRenderItemsEnumerator',
	'{34EE0736-EB0C-47F4-A4DA-D28AE8D91BFF}' : u'FaceDefinitions',
	'{CE3FEA37-5793-4814-B9E4-88C84DC0BEEE}' : u'Cell',
	'{D0F606AE-494C-4810-8280-071F5A56824F}' : u'ModelFeatureControlFrameRow',
	'{078D1300-9A94-4644-BB80-BFD3B4600F3A}' : u'DWGPolyline3DProxy',
	'{3181BFE4-BAD1-4C7A-9107-114093E4238A}' : u'DirectEditSizeOperationProxy',
	'{3E43E559-0053-402D-BE5F-4AC170C11A04}' : u'LoftRails',
	'{83C558ED-EC43-41A6-8FCB-36461DF6319B}' : u'SketchBlockDefinitionProxy',
	'{29F0D463-C114-11D2-B77F-0060B0F159EF}' : u'PartDocument',
	'{29F0D465-C114-11D2-B77F-0060B0F159EF}' : u'AssemblyDocument',
	'{29F0D467-C114-11D2-B77F-0060B0F159EF}' : u'DrawingDocument',
	'{29F0D46C-C114-11D2-B77F-0060B0F159EF}' : u'PresentationDocument',
	'{1010554D-5E7D-4D43-A381-89B57B51A708}' : u'LayersEnumerator',
	'{415A6C89-2B25-4884-B2E3-78BC8CAB9AC2}' : u'DrawingStandardStylesEnumerator',
	'{D05367DD-3A18-47DC-A618-7550582CEEDA}' : u'DrawingCurveSegments',
	'{28DD48CD-8D70-11D4-8DDE-0010B541CAA8}' : u'TwoLinesWorkPointDef',
	'{619680F8-EB9A-4F13-8D23-721FE776C955}' : u'BrowserPaneSink',
	'{2520A915-6F04-4248-B5A3-05B15E651FD9}' : u'iFeatureTemplateDescriptors',
	'{C64DD969-DCB0-4FA9-AD0A-E09744466D61}' : u'FileDescriptorsEnumerator',
	'{CE99120C-2AEC-4916-AB66-C14F780325A7}' : u'iAssemblyTableRows',
	'{2BAE3F08-F0AE-4B03-A432-E3A3C22408F6}' : u'ModelHoleThreadNote',
	'{5DE610F3-F512-4973-B78A-F50669560B4B}' : u'HelicalConstraint3DProxy',
	'{429D036C-4F9D-4F72-9F77-AB5789FCC6E9}' : u'OGSRenderItem',
	'{380ED49C-ADD8-47EC-B99E-10D00CE618D7}' : u'BalloonValueSet',
	'{A0F72CD2-B7A3-4EBA-9CDB-47F42BC74777}' : u'GeneralDimensions',
	'{5EA2744B-95DB-4104-B06A-E9BB6712D59E}' : u'iMateResultProxy',
	'{D54EA6F2-9FB4-43A3-A0C6-C93AF9991E28}' : u'BendPartFeatureProxy',
	'{6E68C1F1-A6AF-4235-8E86-AB031F7813E3}' : u'PresentationOptions',
	'{7EB60BBC-FF1C-428E-BB89-5F69BD727E83}' : u'DWGLineProxy',
	'{44A143D3-13C8-4B0A-AE53-CCC6169C44DB}' : u'FeatureDimensions',
	'{1DCB7001-C7CD-4637-AC67-296CEB47A86B}' : u'SurfaceTextureStylesEnumerator',
	'{FD30BB1E-44E3-4AB5-9035-9715ABEB9649}' : u'ContentQuery',
	'{901E43F5-403A-45C8-A93C-E9509386BB74}' : u'iPartTableCell',
	'{EA49DCCB-E7AE-4B7D-BEAC-80F835167854}' : u'ProfilePath3DProxy',
	'{F057A860-3896-4C4A-87CB-E634F9BA681B}' : u'ExtendFeatureProxy',
	'{3DA40E6A-7ED7-4B2C-A2E5-3FCE98B44077}' : u'OrdinateDimension',
	'{2FBF7141-4414-423B-9F95-3C6489DC47B9}' : u'DrawingBOMCell',
	'{46AEA719-4302-11D4-B7AB-0060B0F159EF}' : u'ComponentOccurrenceProxy',
	'{E538F3DF-5386-4537-ABDB-82C476C4274D}' : u'CommandBarButton',
	'{938A5052-5007-48B1-9629-D00898FD6855}' : u'FlatPatternPlate',
	'{AD47616F-A657-4363-AB07-360A1A38AD44}' : u'DWGPolyline2D',
	'{A50E48BD-8D0E-4C9A-B3C7-D6EC114ACB3D}' : u'SketchEllipse3DProxy',
	'{46AEA729-4302-11D4-B7AB-0060B0F159EF}' : u'SurfaceBodyProxy',
	'{F9CB0F15-28B0-4D98-A658-F906D8B0D965}' : u'SilhouetteCurve',
	'{46AEA72B-4302-11D4-B7AB-0060B0F159EF}' : u'FaceProxy',
	'{46AEA72C-4302-11D4-B7AB-0060B0F159EF}' : u'EdgeLoopProxy',
	'{46AEA72D-4302-11D4-B7AB-0060B0F159EF}' : u'EdgeUseProxy',
	'{46AEA72E-4302-11D4-B7AB-0060B0F159EF}' : u'FaceShellProxy',
	'{46AEA72F-4302-11D4-B7AB-0060B0F159EF}' : u'EdgeProxy',
	'{46AEA730-4302-11D4-B7AB-0060B0F159EF}' : u'VertexProxy',
	'{4FF4C556-DB2C-4FD7-A7E5-06C171C18D7B}' : u'BoundaryPatchDefinition',
	'{BE5F1900-C9E6-49B4-BA3A-1BC7FF49DCD0}' : u'AssetLibrary',
	'{7A5B2F53-5756-4261-B6F1-4B5C3CDE1226}' : u'SketchFixedSpline3D',
	'{73886374-D415-4797-8E3A-A2CA9115D924}' : u'HoleTableRows',
	'{CC1FB682-EF98-4FE5-9934-143CFB8C65B1}' : u'ChoiceAssetValue',
	'{EF706A55-28C3-41A6-8D99-EE900BDBCD9D}' : u'AssemblyJoints',
	'{1492BD29-4122-41C8-AA02-B871BC06CCA1}' : u'ContourRollFeature',
	'{AE277672-2FDC-11D3-B78F-0060B0F159EF}' : u'TransactionManager',
	'{AE277673-2FDC-11D3-B78F-0060B0F159EF}' : u'TransactionsEnumerator',
	'{AE277674-2FDC-11D3-B78F-0060B0F159EF}' : u'Transaction',
	'{AE277675-2FDC-11D3-B78F-0060B0F159EF}' : u'TransactionEvents',
	'{F59CE3B0-44CC-4FB5-9C81-7234A25DD381}' : u'ThickenFeatures',
	'{5A0B6FAA-1405-4AB1-AFE9-786462FADF33}' : u'ThreadTableQuery',
	'{AD86A222-E8A0-4754-A764-65A958389DF5}' : u'HoleFeatureProxy',
	'{CA779A92-76AD-4CD4-ACDB-7F06D73A089E}' : u'HoleTag',
	'{A19EC228-CE1D-4B2D-BE30-584AF42A18AA}' : u'DWGSpline',
	'{6ECCBC7F-A50D-11D4-8DE4-0010B541CAA8}' : u'TranslatorAddInServer',
	'{BC3487BB-F349-4A6C-9F72-D8C62CBADE6B}' : u'Attribute',
	'{E72E9ED9-8A10-4292-9792-96FA51ECD810}' : u'AutomatedCenterlineSettings',
	'{6ECCBC87-A50D-11D4-8DE4-0010B541CAA8}' : u'TranslatorAddIn',
	'{3D218008-FA54-48CB-89BC-8EFBF3D0B6CC}' : u'ClientViews',
	'{97ECB3AE-6C6E-4D8A-A91E-564314494EB8}' : u'TransientGeometry',
	'{4FAB4F91-4998-4B1C-9717-8CDF1BD7377E}' : u'MidpointConstraint3D',
	'{F899D5C4-5961-43ED-A66C-E44A186C1B67}' : u'RolledHemDefinition',
	'{78E9A7D5-C2AD-48C2-85D5-3A0A58D2FDA5}' : u'FromToWidthExtent',
	'{076FFE46-6694-42EE-9F7F-E61F71434845}' : u'AngleConstraintProxy',
	'{39930637-A840-4819-AB86-EFE9CCB21BD1}' : u'PointAndPlaneDistanceDimConstraint3D',
	'{90A1D182-6B1E-49C2-9DAF-3A74B31BE6D4}' : u'DerivedPartEntities',
	'{BF078925-9AC1-485E-9638-4DE87CABBCB7}' : u'FileDialogEventsSink',
	'{9C88D3A8-C3EB-11D3-B79E-0060B0F159EF}' : u'GeneralPreferences',
	'{1FE852AA-E1B7-4160-8F8D-302E0B46BC52}' : u'BIMDuctConnectorDefinition',
	'{9C88D3AA-C3EB-11D3-B79E-0060B0F159EF}' : u'HelpManager',
	'{611952AC-F765-4950-8863-36C465FA2370}' : u'RigidBodyGroup',
	'{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}' : u'Camera',
	'{FFC0E573-23C5-4DB1-A1DC-F6B12EA2907B}' : u'Weld',
	'{9F672C49-E28B-4239-8F7B-BF3FA7FD5071}' : u'IntersectionCurves',
	'{25944748-FC4C-4214-A0AC-627BDF178793}' : u'InventorVBAArgument',
	'{49CB4BB5-872A-11D3-8524-0060B0F0B5B7}' : u'Circle',
	'{49CB4BB6-872A-11D3-8524-0060B0F0B5B7}' : u'Circle2d',
	'{49CB4BB7-872A-11D3-8524-0060B0F0B5B7}' : u'EllipseFull',
	'{49CB4BB8-872A-11D3-8524-0060B0F0B5B7}' : u'EllipseFull2d',
	'{49CB4BB9-872A-11D3-8524-0060B0F0B5B7}' : u'BSplineCurve',
	'{49CB4BBA-872A-11D3-8524-0060B0F0B5B7}' : u'BSplineCurve2d',
	'{7F842490-A580-4A3A-AF94-DF8E5D292A42}' : u'EdgeDefinitions',
	'{45D64D2D-8D31-4ABD-BB94-E55F0879A90C}' : u'ReferenceComponents',
	'{E825D13E-DAE3-4CA1-A275-5C0A62A67E6B}' : u'DWGEllipticalArcsEnumerator',
	'{A962939B-0A11-490F-AC66-DC0FDAA3DD75}' : u'PointCloudScan',
	'{1C98EA42-27FC-4BFA-84E4-D29C7A11F889}' : u'DrawingCurve',
	'{2D38284B-DEAD-48C3-905D-02D1B7432699}' : u'ChamferFeatures',
	'{C70B926C-2519-4760-B513-DB4FD170208A}' : u'DWGLinesEnumerator',
	'{5C204B1E-BE7E-489A-A842-7A800A7CE348}' : u'GeneralNote',
	'{76283A80-50DD-11D3-A7E3-00C04F79D7BC}' : u'_PresentationDocument',
	'{6D78B55D-0148-442F-9EF5-E00611FCD8FF}' : u'RunoffSurfaceDefinition',
	'{3E39E3B3-FA8E-463D-A191-6D7A7CB8E7AE}' : u'BendPartFeatures',
	'{03B09E04-FA49-40EA-AE2D-FF7972025350}' : u'BIMComponentDescription',
	'{142C71BE-1254-4947-9192-382BCC511F46}' : u'ProfileEntity3D',
	'{FE15F632-2312-46D7-86C9-5EEAAC85F7B3}' : u'CenteredWidthExtent',
	'{206B59B2-22A6-11D4-B7A8-0060B0F159EF}' : u'DrawingViews',
	'{5908F091-036B-49E5-9685-3228EB2EE3E2}' : u'CornerRoundFeatures',
	'{28DD48BB-8D70-11D4-8DDE-0010B541CAA8}' : u'TwoPlanesWorkAxisDef',
	'{9D7514D7-EA00-4F2D-8F66-0E395B21C284}' : u'ColorAssetValue',
	'{2B2BEA0C-F141-4B3E-B061-1B2C8C6B5D9F}' : u'MidpointConstraint3DProxy',
	'{6AC23513-A004-4DC5-B77D-6D18BCB5E43E}' : u'GrillFeatures',
	'{4CF7D720-1E41-4049-8C1A-70C980D11667}' : u'ControlDefinitionEventsObject',
	'{1F917159-C90E-4746-A4E3-E543894ADFD3}' : u'PresentationExplodedView',
	'{3C16D9FD-5F89-4669-B637-B356887583D1}' : u'FilletIntermediateRadius',
	'{FBC6B272-3033-4F57-8279-7D70F3FFD508}' : u'TranslateTranslateConstraintProxy',
	'{63AD687A-3898-44E2-B857-C9DAD84FC9EC}' : u'FileUIEventsSink',
	'{F4D9FAC9-D5F7-4FB5-8324-16CA73F349FF}' : u'MiniToolbarControl',
	'{5E600148-DA27-47DD-8286-E38CC9466B2F}' : u'CustomConstraintProxy',
	'{82B32371-11B8-467E-B57E-0112DDD4BB65}' : u'FeaturePatternElements',
	'{A7D32953-D38C-4EB4-B9D0-79F7275B37C1}' : u'DistanceExtent',
	'{70109AA3-63C1-11D2-B78B-0060B0EC020B}' : u'View',
	'{FA34A401-F063-11D3-B7A2-0060B0F159EF}' : u'EllipticalCylinder',
	'{FA34A402-F063-11D3-B7A2-0060B0F159EF}' : u'EllipticalCone',
	'{1236D237-9BAC-4399-8CFB-66CB6B7FD5CA}' : u'SketchSplineHandle',
	'{4E27C06E-4D6A-4E53-9F84-32A0643623CF}' : u'Environment',
	'{239A8027-E757-4A2E-B8DC-9203A644401F}' : u'ContentFamiliesEnumerator',
	'{BC985A7D-4B44-4089-870D-0AEE95D5E86A}' : u'EnvironmentBaseCollection',
	'{E3757DA9-1C29-477B-838A-B84E896410B2}' : u'SketchControlPointSplineProxy',
	'{6B46D5EC-57DE-414D-8ACC-EF1E7C6C1AAF}' : u'DWGEntity',
	'{3F96EC38-31B5-46BD-B45D-CA049B450786}' : u'MidSurfaceFeatureProxy',
	'{4E1C27BA-D992-411F-9DE2-BD630285E4B3}' : u'DesignViewRepresentation',
	'{DA7E3A1C-5473-4CC3-8E19-25F8DE00C0A6}' : u'ShadedDisplayOptions',
	'{A1C8AD17-F4C3-4424-982C-9D628A5A4ECA}' : u'EnvironmentList',
	'{A0DB05CD-57E9-47C9-9D33-E648BB57226A}' : u'HoleFeatures',
	'{4F8D5D47-63F7-4690-A06D-54D7311A2566}' : u'ChangeDefinitionObject',
	'{4732A4F0-D435-4F10-8548-4DBE68276D58}' : u'StyleEvents',
	'{61FC7221-543B-4885-9546-B700267C98D1}' : u'SketchSpline3D',
	'{DDD17D41-9A17-4ADD-BDB2-E2701A524903}' : u'CornerChamferFeatureProxy',
	'{6B3ECB2F-78BA-492E-9235-E68EA88F66E9}' : u'PointCloudPlane',
	'{FA452CED-C585-4568-BACD-C3DBFAC85D97}' : u'InterferenceResult',
	'{E65DEA7B-63C6-4F6E-9FCE-8177FEE904F9}' : u'PointCloudPlaneProxy',
	'{6B9C5A03-557E-477A-A6E4-D2E00FB5B812}' : u'PathEntity',
	'{5189E676-CC1A-4901-98E7-EC85130FDB63}' : u'ProgressiveToolTip',
	'{BD923BF8-C5DD-4AE4-B577-0988B48FA89D}' : u'ProfileEntity3DProxy',
	'{0AE09AED-1DFB-41D3-B640-E0E9A24FA8C0}' : u'FoldDefinition',
	'{047360BD-1872-4C10-8538-01518FD7F750}' : u'AssetCategories',
	'{67B1BC45-4518-4DB9-A5D3-C0364374BB80}' : u'CommandBarControls',
	'{8112A2AA-0017-4029-81A5-9C18F5E37E92}' : u'ConstraintLimits',
	'{0456FF0D-196E-4C72-989D-D86E3DD32955}' : u'TangentConstraint3D',
	'{1D09051E-D674-4ABE-BEC9-5A58016455B1}' : u'NonParametricBaseFeature',
	'{8F656C43-9BFD-4BAE-AF23-A21067DDED8E}' : u'ModelAnnotationsEnumerator',
	'{66D80FFD-2C33-4F55-8A78-EBF0A094CEEE}' : u'DockableWindowsEvents',
	'{518CD473-78CC-4B12-A831-AE93812A2774}' : u'DWGBlockDefinitionProxy',
	'{62D66B29-1EA9-48CA-A6C6-6D6FF7785213}' : u'RadiusModelDimensionDefinition',
	'{EF118F14-C2D2-4DF4-910A-3438FBEC2817}' : u'ConcentricConstraint3D',
	'{95852FC2-F171-47D3-9435-A478AFF2353E}' : u'FromToExtent',
	'{B0128AFD-14AE-4FD6-AED0-314D1F79F3EB}' : u'ModelingEvents',
	'{75120650-FD69-4DFD-A738-9E5E34F5934B}' : u'Profile3DProxy',
	'{AEFA0FB8-139F-469C-8765-26AEA8C0A175}' : u'DimensionText',
	'{C00FE3F4-2D75-4409-93FB-9B72913C073C}' : u'SketchImage',
	'{201C8CF3-0801-49F5-B87E-F39CEA7508D7}' : u'SurfaceTextureBSIDefinition',
	'{358B0B8E-D2C7-4D76-AAC6-33009864424E}' : u'iFeatureDefinition',
	'{4E97BC3C-1235-44DE-8B31-571FA40955B5}' : u'MiniToolbarValueEditorObject',
	'{347FB32C-79ED-4A5B-89B1-7B14FF6A9CA8}' : u'ReferenceFeatures',
	'{56B990B9-D25A-436F-A652-1D21EC739C57}' : u'GeometryIntent',
	'{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}' : u'Parameter',
	'{71BA345E-F3F9-49C9-917C-D7DFC284A07F}' : u'OrdinateDimensionSet',
	'{A03B2CAF-A5F8-4522-BF79-CF4D497DCF4E}' : u'PlanarSketches',
	'{1E4085FD-7428-4EA1-B3EF-B2ADDD7F8F5C}' : u'RotateAboutLineMoveOperation',
	'{6DEF95B4-C5EF-4FBA-AEE9-B9486F648CAB}' : u'FaceFeatureProxy',
	'{F0AF7CF3-7F4E-4A34-B384-7C98CE2843B2}' : u'MoveFeature',
	'{70B77812-4E3A-4499-8F8D-6AB6C6BDC5A5}' : u'MouseEventsObject',
	'{2A6C1D0D-FAF8-4A31-A9FB-39761F36F814}' : u'CustomTables',
	'{30A44C19-C3F4-483B-8835-A0A13B849AC0}' : u'PanelBarEventsSink',
	'{9D063FDB-B597-49B0-8DBC-7EB3D5F715B8}' : u'BrowserFolder',
	'{2FD8A7F5-B548-4E12-9D65-FF47FD063F8C}' : u'ExtrudeFeature',
	'{FD30DCC9-A6E8-44B1-85B0-D7D8AE1580E5}' : u'DrawingDimensions',
	'{9A750C49-0384-4CD8-B1D9-DAADD3E28657}' : u'WeldmentComponentDefinition',
	'{C78E43C1-DB92-414A-9B45-352DFAC434E4}' : u'TangentiMateDefinition',
	'{0E000A5B-67FD-4B23-A312-E6E5F444C045}' : u'RestFeatures',
	'{2DADCD08-8ED5-4F71-88BF-481E8B0E9847}' : u'ExtendFeature',
	'{773C0E8F-2C4C-4871-93F7-AF9483171461}' : u'FeatureBasedOccurrencePattern',
	'{523EF757-245A-11D5-8DEC-0010B541CAA8}' : u'Profiles',
	'{C9D63CDD-B82A-4CD9-82EB-CE937569197E}' : u'ChainDimensionSets',
	'{A2E47B01-25D6-4047-BC17-FA7F71B18599}' : u'HoleTableColumn',
	'{04A196FD-3FBB-43EF-9A79-2735B3B99214}' : u'LineLengthDimConstraint3D',
	'{941D7D22-4C65-4E96-B446-086CD1B94572}' : u'PresentationExplodedViews',
	'{F1B96719-11ED-44A6-9AAB-34BC6D05F8EF}' : u'BrowserPanesEvents',
	'{359AC6D9-E239-4825-BA81-DD8E433FBD1E}' : u'iMateResultsEnumerator',
	'{3C007201-8D66-47BD-AD94-2012FF75C4C5}' : u'AliasFreeformFeatures',
	'{EF42229B-CAC3-488D-BCC4-C992FC7795AE}' : u'InventorServerObject',
	'{3588F0A6-950E-402A-BFB1-C0ECB1B2EE44}' : u'TestCase',
	'{32429DA6-B712-4638-8C53-B1EEE7C1D18B}' : u'CommandBarPopUp',
	'{C3E0CCFC-A6F5-4C54-83E4-3A2CBF11D5D7}' : u'LibraryManager',
	'{602389D5-6C6A-4368-A6F2-47D54FA1FBA4}' : u'DirectEditFeature',
	'{B546124B-09AA-11D5-8DEC-0010B541CAA8}' : u'SketchEntitiesEnumerator',
	'{B546124D-09AA-11D5-8DEC-0010B541CAA8}' : u'SketchEntity',
	'{02466B5A-9C4B-48C4-BFA0-5590DB014745}' : u'LoftRail',
	'{B5461255-09AA-11D5-8DEC-0010B541CAA8}' : u'ProfileEntity',
	'{B716CEF3-32C9-4A9A-911D-0D1CF52A74C9}' : u'PunchToolFeatureProxy',
	'{B5461257-09AA-11D5-8DEC-0010B541CAA8}' : u'GeometricConstraint',
	'{18A18CCA-283E-4E06-9358-1949A91CECF1}' : u'LineAndPointWorkAxisDef',
	'{B5461259-09AA-11D5-8DEC-0010B541CAA8}' : u'DimensionConstraint',
	'{9E0BA9CA-E916-11D2-B785-0060B0F159EF}' : u'ReferencedFileDescriptor',
	'{9E0BA9CB-E916-11D2-B785-0060B0F159EF}' : u'ReferencedFileDescriptors',
	'{C3F06C8B-B0EA-4EC3-9922-1657009774D3}' : u'DriveConstraintSettingsObject',
	'{539ACB89-A1F6-43E4-BC0A-BDCE1B127584}' : u'ChamferFeature',
	'{D5DA4F07-3728-4B95-9D14-5FF0ED96992E}' : u'MiniToolbar',
	'{BBC883B2-B5E1-44C9-A98F-E7221FC17F3D}' : u'BendFeature',
	'{4A66B607-4991-4FA2-A361-CD8424A99A70}' : u'iFeatureTableRows',
	'{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}' : u'FilesEnumerator',
	'{494427B8-E911-4706-9814-35980AC5621D}' : u'FlangeFeatureProxy',
	'{CB69F173-558E-11D3-B793-0060B0F159EF}' : u'Point2d',
	'{AB5EF2D1-EAEB-4A4A-A86B-24BF0F2111BD}' : u'ControlDefinitionEventsSink',
	'{30E22548-6DE0-43B7-A8EE-E379A9C86F7D}' : u'ContentFamily',
	'{3D157428-294A-4446-A33D-6BEA664F61D7}' : u'ProgressBarObject',
	'{CB69F175-558E-11D3-B793-0060B0F159EF}' : u'Vector2d',
	'{D29F9AF1-3383-40AC-94BA-69057A213AAD}' : u'WireEdgeDefinition',
	'{264513E0-16F5-4AE8-A80D-46EE06D2C99B}' : u'DirectEditRotateOperationProxy',
	'{843FEEB5-A0EF-4C5B-8939-4F9B574119D8}' : u'CoincidentConstraint3D',
	'{1880ABD8-B826-4258-A2F1-31B5E5740FA6}' : u'BreakOperations',
	'{91BDBCAB-AC12-4216-ACE4-4F561D7DD4BD}' : u'DeleteFaceFeatures',
	'{5F89369C-998C-4AD6-B59D-FBA9AFDCFB65}' : u'BIMComponentPropertySet',
	'{CB69F178-558E-11D3-B793-0060B0F159EF}' : u'Line',
	'{7D85BA17-75C5-4EBE-AA18-F7E60AE25733}' : u'BalloonStylesEnumerator',
	'{A110C93B-A3B5-4717-A697-87EA0126216F}' : u'BossFeatures',
	'{7C1BEFD9-4296-4794-B3A2-8025809570D8}' : u'BIMConnectors',
	'{B9036BF2-EBE0-4593-92B6-DBCD421C6BDF}' : u'CoilFeature',
	'{82B8F63A-474B-4DAC-AE2D-E9F5E9BB2C2E}' : u'iFeatureTableColumns',
	'{52D6C08A-B387-4F4C-A2E3-4F3CFFF276CE}' : u'TestProgram',
	'{6755F53A-DF74-4D7A-AB08-340C5AAD6F5C}' : u'DWGPolylineProxy',
	'{BBCEA345-055B-4625-ABCA-582C6BF7E440}' : u'OffsetSplineDimConstraint',
	'{ED68898D-4062-47D4-AC28-9B8A1F38CE90}' : u'DriveConstraintSettingsSink',
	'{7BB0E824-4852-4F1B-B43C-7F729A3D7EB8}' : u'CircularPatternFeature',
	'{92E914A0-9FEA-11D6-8E0B-0010B541CAA8}' : u'_AssemblySolverNodeSink',
	'{12DA4D02-DCE6-4F08-ADEB-9EE13C559C52}' : u'BIMConnector',
	'{0F13E8B9-A4C2-4477-93CA-FC2CD0D2C1B1}' : u'DriveSettingsSink',
	'{28DD48BD-8D70-11D4-8DDE-0010B541CAA8}' : u'TwoPointsWorkAxisDef',
	'{1DC369B0-C6C9-42B7-BA0F-5A2AB9CA79AE}' : u'FactoryOptions',
	'{641D6ED0-4DF1-4FA3-B04D-86107C00A62B}' : u'SplineFitPointsConstraint3D',
	'{4DEAC0A5-E998-4958-8344-D866385CECF2}' : u'DerivedAssemblyOccurrence',
	'{9A6F5F04-E0DD-463B-96C3-117B88E7BE25}' : u'FullSweepExtent',
	'{08DCE0A8-28F0-4513-A655-010AD06BC874}' : u'LeaderNotes',
	'{31C63BA8-7EB4-4816-A367-F99A12691690}' : u'FaceOffsetFeature',
	'{C80E7C12-B126-45F2-A228-704248D58530}' : u'ShellDefinition',
	'{AFEA608B-F136-4BD1-995B-333BCAFDED08}' : u'ThroughAllExtent',
	'{745A04C4-8445-412A-AFA7-33E778DA3059}' : u'SketchControlPointSplines3D',
	'{B1340A33-EB0D-4609-BA1E-B98A3D173794}' : u'Profiles3D',
	'{A52D98FA-2E72-4170-ABB4-6D10C2BCB095}' : u'DerivedAssemblyComponents',
	'{6B64AAF5-85DF-4FB5-ACAB-717DBBEE7DA4}' : u'ConcentricConstraint3DProxy',
	'{FDBEDE20-57AB-44CC-9A84-31E4D730E85D}' : u'FilletFullRoundSet',
	'{6B821DA7-B56B-44FC-859F-4DABA658C6E2}' : u'CommandCategory',
	'{F0684BBA-73A5-45B8-8D38-E64A53735C9E}' : u'iFeatureTableRow',
	'{B6B0211A-D77D-4D79-A529-7D8612C9A7A3}' : u'MiniToolbarSink',
	'{541E7231-CD23-4986-B26D-4C2B4F1E2DBE}' : u'SketchConstraintSettings',
	'{3BCDEC54-2F73-4114-A7CB-ACF5E823B67D}' : u'SketchPoints3D',
	'{3F51C434-F75E-487F-93A2-5D1438AD5D41}' : u'RuleFilletFeatureProxy',
	'{2EF323DC-CEC7-4E75-9C92-E7571F6653C3}' : u'OffsetWidthExtent',
	'{F36456A4-780C-4CA6-B420-5DBEFFBBCA7D}' : u'FlushConstraintProxy',
	'{60F87ABB-0D3B-47D0-A6A9-E9AAC919EF31}' : u'ComboBoxDefinition',
	'{53318B1D-70C7-4BB0-9103-73ABFA0B3094}' : u'ClientBrowserNodeDefinition',
	'{1435773B-06FC-46E8-B965-5845697D2A6B}' : u'SweepGraphics',
	'{6BA435DD-BBD6-11D4-8DE6-0010B541CAA8}' : u'NameValueMap',
	'{94F1E029-984C-4DDC-9B12-003982C02E06}' : u'DocumentSubTypeHandlerEventsSink',
	'{672C4DAF-1B67-4131-8F53-9274F42E44E9}' : u'RadiusModelDimension',
	'{3538A9B3-0A9F-4B3E-9FC9-3272AB0D7C2B}' : u'DrawingBOMRow',
	'{2B03891E-1B59-4576-8160-C61EA6E6D0DC}' : u'iFeatureOptions',
	'{9789E1AC-1767-4225-96DD-FD06F614AD59}' : u'ModelAnnotations',
	'{A8DB137E-896E-4B61-8813-E49040BBE99E}' : u'iPartTableRow',
	'{85672B0C-EA86-4DF1-B223-51DD72F29566}' : u'BossSets',
	'{AF669E3B-2FC3-4731-96C4-2CC724B98E60}' : u'iFeatureInputs',
	'{4062D31A-F8CE-4D38-B50A-6D8B1FB50D94}' : u'ModelDimensionDefinition',
	'{730B9714-80D2-4009-8904-1AEF4EAF3F23}' : u'EmbossFeatures',
	'{F8B2175E-285B-4787-B12A-6E485CA1885B}' : u'CornerRoundFeatureProxy',
	'{F0780498-03E3-471D-A733-92EFAC4FF0EE}' : u'ArcLengthDimConstraintProxy',
	'{E12CF633-9F24-427A-A6F9-D5A7D7BCB314}' : u'_VbaImplementationAssemblyEvents',
	'{B513304D-05B5-4DD7-AA23-E4BF2F120406}' : u'ModelAnnotationText',
	'{C1066E40-4E2F-45C2-A5AB-E2B4D1B84A1E}' : u'EllipticalArc',
	'{22D71B5C-2F5E-4A1B-9328-ABE89F78ABC6}' : u'iMateDefinitionsEnumerator',
	'{89832854-67B3-4DBF-B8E6-715435D51FE2}' : u'_DocPerformanceMonitor',
	'{BEBB7A1A-2E50-4C62-A4E1-64B2E9A18AE6}' : u'ReferenceFeaturesEnumerator',
	'{86EF3B55-8CEB-45E8-9C9C-5F4430679B7C}' : u'DirectEditOperation',
	'{87359527-E87E-456C-BDD3-F82FACBABAD2}' : u'ContentCenterDialogEvents',
	'{B4D0EB63-4D3B-42A6-BE38-855EB5DA68E3}' : u'VisibleOccurrenceFinder',
	'{A9427B73-D39C-4DA3-9330-3CEB71ECA2B9}' : u'BrowserFoldersEnumerator',
	'{DDD3ADB9-30D8-4E01-8E88-42ABF8645AD4}' : u'MaterialsEnumerator',
	'{76B0EC66-F962-4D22-9E96-3D02F49AD363}' : u'BrowserNodesEnumerator',
	'{98D51E77-8775-4472-8AB0-50BCA8F56023}' : u'DiameterGeneralDimension',
	'{D4C98D93-FA6C-4602-8EB8-2709938BFE74}' : u'DerivedParameters',
	'{F1779764-61F6-4C25-8B5D-6A6F41B57709}' : u'EdgeLoopDefinition',
	'{7D7EAE29-869F-48FB-AD5E-797AB5B87F65}' : u'PathAndGuideSurfaceSweepDef',
	'{6364B6D5-2994-46A5-8F53-03F63958B056}' : u'CommandBars',
	'{C11F6667-E5D4-4A7E-8C47-70AA423E7758}' : u'SurfaceGraphicsVertexList',
	'{9DACF05E-4734-4D7E-986A-EE320F8A85C7}' : u'LightingStyle',
	'{41473886-B1F1-4E65-9BEB-36F729B6A9F1}' : u'LumpDefinitions',
	'{A40068C9-5681-4B3D-961A-1C6360B20BFE}' : u'FilletRadiusEdgeSet',
	'{8F25CE45-DF1F-4669-BAA8-E2042ED68811}' : u'DistanceAndAngleChamferDef',
	'{5F15A208-8871-42B9-8421-D0555100A7D9}' : u'iFeatureTable',
	'{CB69F171-558E-11D3-B793-0060B0F159EF}' : u'Matrix',
	'{CB69F172-558E-11D3-B793-0060B0F159EF}' : u'Point',
	'{D70C53E3-58A6-48CA-95D2-AF6F4AAD04EA}' : u'ChangeManager',
	'{CB69F174-558E-11D3-B793-0060B0F159EF}' : u'Vector',
	'{6ED45F3A-BAF4-41FE-8907-970BB3CA48DF}' : u'ApplicationEventsObject',
	'{CB69F176-558E-11D3-B793-0060B0F159EF}' : u'UnitVector',
	'{CB69F177-558E-11D3-B793-0060B0F159EF}' : u'UnitVector2d',
	'{BCD3EFAF-0FEF-4AC1-8303-2A4BF18E96FC}' : u'ClientView',
	'{CB69F179-558E-11D3-B793-0060B0F159EF}' : u'Line2d',
	'{CB69F17A-558E-11D3-B793-0060B0F159EF}' : u'Plane',
	'{D4652AC1-D4B9-4D65-8C2B-942D74411B1C}' : u'VirtualComponentDefinition',
	'{08389E18-6E84-499B-8F1F-09AC53003178}' : u'MidSurfaceThickness',
	'{1DA08DFE-88EB-4ABE-8FA8-34FD098D65AA}' : u'DrawingViewEventsObject',
	'{F0854465-652D-4375-98A4-7C875BFE7A9C}' : u'UserCoordinateSystem',
	'{CF10C244-F350-4155-97FD-34A35D996272}' : u'NativeBrowserNodeDefinition',
	'{35C3BC01-5C75-4BDF-B92E-97205EE57219}' : u'InsertConstraintProxy',
	'{B25D15A6-B823-42FF-9ABB-781A3043ECB0}' : u'RepresentationsManager',
	'{2D6BA5C4-3929-44A3-8D59-5A173034BBF1}' : u'BIMCableTrayConnectorDefinition',
	'{1154D44F-DED2-4457-B862-8631D4D69FC6}' : u'PositionalRepresentations',
	'{4DF199B9-D7C8-4770-9954-2EFF94867CEC}' : u'BoundaryPatchLoop',
	'{619B5213-A92D-4D4B-BE3F-6CA4B1715A78}' : u'MateiMateDefinitionProxy',
	'{856FF591-895A-4A94-9FB1-16F5265C91C8}' : u'SketchArc3DProxy',
	'{99CBF031-2FFA-440F-B947-8470CD64E79C}' : u'TriangleFanGraphics',
	'{76A8F762-B6B5-4B18-916C-EC7C17B22618}' : u'ModelLeaderNodesEnumerator',
	'{01BAC9F1-F900-4E57-9FDB-F12232AEC9D2}' : u'SketchEquationCurves3D',
	'{9C9D6F69-F26B-4311-A688-17C04EC292BE}' : u'DraftAnalysis',
	'{14A842C0-8BD2-431B-B1DA-A487A6E35B18}' : u'SketchBlockDefinitionsEnumerator',
	'{2035E584-09E7-4B18-9698-014DEF44B10E}' : u'PerpendicularConstraint3D',
	'{B3D5D60A-6CE4-4F7B-A6A6-88A15E433F95}' : u'ImportedGenericComponentProxy',
	'{6F10D9EC-E95C-489C-A398-5B530FD1D820}' : u'ContentQuerySink',
	'{2772058F-17D8-4969-8D46-51860F09AC9B}' : u'UserInputEventsObject',
	'{4AA83B95-08F8-4415-9397-4BB5E8103290}' : u'Ribbons',
	'{6B73769B-1859-4202-87D4-2E508FC9434C}' : u'BIMExchangeServer',
	'{04370FAD-4F3A-4589-A7F8-6DFA839522D3}' : u'MoveFaceFeatures',
	'{7E4D60AD-496E-4336-96AA-5A2C6178C836}' : u'LeaderStyle',
	'{755B3C6B-3A92-4702-96AC-686382A91278}' : u'Light',
	'{48DDBD08-5630-4D9A-A71F-8F623A3ABB47}' : u'ChangeDefinitionSink',
	'{F44EE9AE-7D98-49C7-8634-700050114F38}' : u'WeldBeads',
	'{FC290B65-544A-4F65-B812-092CB93AA421}' : u'AutoCADBlockDefinitions',
	'{0BD0BDD4-2716-42A0-B258-09F689CFDFB5}' : u'RotateTranslateiMateDefinitionProxy',
	'{0D084DAB-C766-4595-A449-7625772E88D2}' : u'Color',
	'{929723D9-517D-4405-A5B5-263E3B02C6C4}' : u'CustomConstraint',
	'{3B1375EE-4B13-48AA-8A03-EDFDAEA85651}' : u'LibrarySketchedSymbolDefinition',
	'{97E8752C-E818-41FF-8C13-D10B6FBC522F}' : u'ThickenFeature',
	'{91578449-A1E5-4865-BF53-D297549308B0}' : u'WidthOffsetWidthExtent',
	'{8FFF6DFE-F659-4C77-81E5-DD9B70A37D90}' : u'SmoothConstraint',
	'{8B3FEE20-C49D-495B-AA3E-B90AE49B736B}' : u'iPartTableColumn',
	'{3AF77BAF-EECD-4301-823D-9B604FE5C176}' : u'UserInterfaceManager',
	'{3D67DF18-9BC6-4470-A9E3-C820CB4E821C}' : u'FileAccessEventsObject',
	'{0CB0F042-1627-49BF-B430-619A3AD6FADC}' : u'SketchEventsObject',
	'{6FD094BA-90C4-4C9D-A3B9-DF3A398ECE26}' : u'BaselineDimensionSet',
	'{325DB945-8B2D-4574-A023-A2864A85896A}' : u'RefoldFeatureProxy',
	'{85B493F3-342B-4D54-83A1-4EF9C50378D0}' : u'ModelSurfaceTextureSymbolDefinition',
	'{662FBA92-6903-4455-9395-207E48749986}' : u'TorusMidPlaneWorkPlaneDef',
	'{EEEC1AAC-5A0C-4405-B0A7-63EBCF82A3A3}' : u'NormalToCurveWorkPlaneDef',
	'{C4F1B40A-B7A7-4F92-A9A4-CF8B1DDDE124}' : u'FileUIEventsObject',
	'{A1D2EAAD-28A1-4692-BC13-883879C68894}' : u'DerivedAssemblyComponent',
	'{221D9E13-D105-485A-B538-1E3FB7250A71}' : u'StyleEventsObject',
	'{E0813E5B-4E25-4192-B86B-0A284E558D5D}' : u'MiniToolbarTextEditor',
	'{90602DB0-0BE4-48E2-864E-D853D3542959}' : u'LibraryFolder',
	'{0BF73FD9-1253-11D3-B789-0060B0F159EF}' : u'FileLocations',
	'{C7A9F576-7180-4DEE-BCC7-8E9DEABECEC4}' : u'AutoCADBlock',
	'{83B2573C-3DBB-44C1-B88D-2D12EF0A9EE2}' : u'PitchAndRevolutionCoilExtent',
	'{E408524C-B7A1-4F17-921E-160774F4DE5D}' : u'KnitFeature',
	'{556DCFA3-BD63-4B13-9C12-D99113AEAEFB}' : u'OrientedBox',
	'{EEB0116A-7B74-4A9C-B2FF-96BC31812249}' : u'InventorVBAProjects',
	'{560ACA74-2C16-428E-9D63-08569BD33300}' : u'MiniToolbarSlider',
	'{6F18AA5B-56B7-4880-90A5-190322278B8D}' : u'BoundaryPatchFeatureProxy',
	'{D0BD7B89-04B5-4165-8E8D-1DB705A02E47}' : u'UserCoordinateSystems',
	'{BB5A14E9-4213-4965-9B76-F9B33C807FB3}' : u'SingleHemDefinition',
	'{B0955199-1373-4868-9B86-4ABB2DC2A684}' : u'CheckPoint',
	'{F3393F71-A68F-442E-A03E-1B06B09D96A9}' : u'MiniToolbarDropdown',
	'{C173A073-012F-11D5-8DEA-0010B541CAA8}' : u'PatternConstraint',
	'{C173A075-012F-11D5-8DEA-0010B541CAA8}' : u'DimensionConstraints',
	'{90943B1A-D344-4227-8219-D1C6090697BB}' : u'RadiusDimConstraint3D',
	'{C173A079-012F-11D5-8DEA-0010B541CAA8}' : u'TwoPointDistanceDimConstraint',
	'{C173A07B-012F-11D5-8DEA-0010B541CAA8}' : u'TwoLineAngleDimConstraint',
	'{C173A07D-012F-11D5-8DEA-0010B541CAA8}' : u'ThreePointAngleDimConstraint',
	'{9CAF989F-33EA-11D3-B78F-0060B0F159EF}' : u'ReferencedOLEFileDescriptor',
	'{9CAF98A0-33EA-11D3-B78F-0060B0F159EF}' : u'ReferencedOLEFileDescriptors',
	'{C173A081-012F-11D5-8DEA-0010B541CAA8}' : u'RadiusDimConstraint',
	'{9CAF98A3-33EA-11D3-B78F-0060B0F159EF}' : u'FileSaveAs',
	'{C173A085-012F-11D5-8DEA-0010B541CAA8}' : u'TangentDistanceDimConstraint',
	'{C173A087-012F-11D5-8DEA-0010B541CAA8}' : u'SketchEllipticalArc',
	'{C173A089-012F-11D5-8DEA-0010B541CAA8}' : u'SketchEllipticalArcs',
	'{BA8CE4E1-3FC3-414C-A73A-26BDB38ECE70}' : u'TransactionEventsSink',
	'{575F2830-2B6A-11D4-B7A8-0060B0F159EF}' : u'PartComponentDefinitions',
	'{575F2831-2B6A-11D4-B7A8-0060B0F159EF}' : u'AssemblyComponentDefinitions',
	'{C173A095-012F-11D5-8DEA-0010B541CAA8}' : u'EllipticalArc2d',
	'{F5DA8C39-2BD7-4E77-BE94-81743E81ACC9}' : u'BendNote',
	'{7CC584DD-262F-45D6-A383-6705655F2435}' : u'DWGPolylines3DEnumerator',
	'{3A4B5B27-8B78-4584-83B5-6A088C6B87FF}' : u'DrawingNotes',
	'{50DE4356-9814-490A-8932-18E72420930E}' : u'AutoCADBlocks',
	'{57CFD4EC-1776-48D3-B5C4-7B6E015D0541}' : u'Material',
	'{8924897F-3F00-4220-BF8A-76CADC5A10DD}' : u'HolePlacementDefinition',
	'{5DBD70FD-AB80-4074-B105-EB28F2CB397A}' : u'SketchSplineHandle3D',
	'{BC6242DB-ABCC-4605-8A0F-9A42F26F9D9C}' : u'DWGPolyline3D',
	'{600D4AE6-12FB-47E9-86E6-46C8C2A9161E}' : u'BreakOutOperations',
	'{FFA15510-CD22-4C40-8DEE-4F846C3D5470}' : u'GraphicsTextureCoordinateSet',
	'{8E05BCC6-20B2-477A-A318-CB7116D8D0A7}' : u'BIMConnectorLink',
	'{4F589652-207C-11D4-B7A5-0060B0F159EF}' : u'ApprenticeServerDrawingDocument',
	'{F1C0EFF2-5035-4DDD-8086-060590676024}' : u'InteractionEventsSink',
	'{85A24FF2-F0E9-4BC4-9A69-34F8C683B41A}' : u'GeometricConstraints3D',
	'{67863AC3-95B7-4386-8A51-449E44AC2FBC}' : u'SketchEquationCurve3D',
	'{ECD82FDD-5B8F-4515-B3CE-1ED92B94C11F}' : u'CoilFeatureProxy',
	'{AD87B241-B3FD-475C-B369-AD3C5D3E3E0D}' : u'RefoldFeatures',
	'{47B53154-8132-47E5-8733-9D9B4268F21C}' : u'SurfaceTextureANSIDefinition',
	'{1DC001D8-CAAE-4132-A265-4E17E74A9410}' : u'InsertiMateDefinitionProxy',
	'{2A8678EA-A024-469A-80DC-D1EAD67847A3}' : u'Profile3D',
	'{29440031-7A2B-4713-907C-DCCE79375669}' : u'WireDefinitions',
	'{1C310044-05CF-4B79-9829-FE41BD1EB1A6}' : u'ContentTableRow',
	'{66E2ABF7-3454-41E6-9115-62879698C194}' : u'PointAndTangentWorkPlaneDef',
	'{E2E51C17-C894-45AF-9827-988D38C283C7}' : u'CircularPatternFeatures',
	'{BB91C845-BD7E-4470-948F-C5A069B21BBC}' : u'ClientFeature',
	'{8C2B0FE6-3B3F-4897-BD44-806DA59E436A}' : u'DWGPolylines2DEnumerator',
	'{15AD2867-FEE2-4A5B-9F07-FDC0A4FF5C72}' : u'AssemblyJointsEnumerator',
	'{2307500B-D075-4F5D-815D-7A1B8E90B20C}' : u'SketchPoint3D',
	'{3B4B3DE9-7B05-47A7-975A-2C370BBBF974}' : u'ShellFeatures',
	'{D96060F8-0E08-4E73-8D5E-37F506A1A738}' : u'TextureCoordinateSet',
	'{D4D0315D-6874-4E69-9BBB-6E3D28B9122A}' : u'TaperedThreadInfo',
	'{B159D948-7FC9-4D48-B482-FC7FD152AFCA}' : u'BrowserPanesSink',
	'{1A58DFEF-0B8C-44DF-97AF-4DAC85734B04}' : u'DrawingStylesManager',
	'{26C1C5B1-44AE-4180-8118-EDF2B8CB220B}' : u'LeaderNodesEnumerator',
	'{C958801B-73D0-4031-B9F6-5CDBCE975ABC}' : u'ComponentGraphics',
	'{7B550B22-4519-43D2-9A9E-5EC0D9FFCCD6}' : u'ErrorManager',
	'{F3D4C961-7227-4E32-90A3-C60A9EEFA90D}' : u'TextGraphics',
	'{D4BF045D-8DFB-44B5-9FFC-FE6ACADF2B23}' : u'GraphicsDataSet',
	'{25E59F53-ADFB-4B1B-8CF4-C8EAE80CA85F}' : u'AssetCategory',
	'{8B657FE9-BF0A-4AED-B1FB-166229D406B3}' : u'SketchOptions',
	'{916EFE1C-6493-4712-92D7-CD789914321A}' : u'RibbonPanel',
	'{4286D377-DC30-4195-9A04-E2C5A29AA72A}' : u'CentroidWorkPointDef',
	'{4E5273FA-20B0-41E3-BB29-03BB6C09B0FE}' : u'ToNextExtent',
	'{EF126FC8-7582-4E15-B5DC-194EEE2CEEDA}' : u'BrowserPanesEventsObject',
	'{A4126F98-E952-4997-BD2D-209D4788F70F}' : u'SketchControlPointSpline3D',
	'{D26E4888-3FA1-4A45-94E5-AA1A3A41B4AE}' : u'FreeMoveDefinition',
	'{C73A295D-CB57-4B32-AA53-652422FACF65}' : u'ToExtent',
	'{2022FEE8-01DA-481F-A515-D2D89C787EA8}' : u'Rows',
	'{B1EECF0D-991E-44FD-8244-61AB5E826B35}' : u'ImportedDWGComponentProxy',
	'{C7A68CD3-14FA-11D6-8E01-0010B541CAA8}' : u'ConcentricConstraintProxy',
	'{16372AAE-1133-4C4C-9A48-D9305D8358F3}' : u'SketchOffsetSplines',
	'{B7FE7553-8DF0-4F70-9798-C85438D3109E}' : u'PathSweepDef',
	'{C5BF9314-D319-44A4-BDFF-16142CE92D58}' : u'ModelHoleThreadNotes',
	'{1F76C4FA-DB71-4D87-8390-1529297ED5A9}' : u'RenderStyles',
	'{E60F81E1-49B3-11D0-93C3-7E0706000000}' : u'_AssemblyDocument',
	'{47005682-42D1-4831-A4BC-63AD38B98D6E}' : u'BIMComponent',
	'{FC23373B-FA59-43C7-BD1B-2618DFA1C8C0}' : u'GraphicsImageSet',
	'{C124F1E0-1B29-481D-A0CB-BA8A8AB69764}' : u'TwoPointDistanceDimConstraint3D',
	'{8D562D7A-4F0B-4EC8-8737-47DD28FB7323}' : u'SketchCircle3D',
	'{0B1630B9-41C0-4DCA-BCBC-2E9D0BA096FE}' : u'SurfaceTextureGOSTDefinition',
	'{6D0B30F0-4279-46EC-8D96-EDD140C3EC72}' : u'DWGArc',
	'{DBB345F5-06CB-4B20-96B8-C47EF589ECBE}' : u'GeneralOptions',
	'{8E9F0865-0AE2-4AAC-8E67-0CED8434114C}' : u'CentermarkStylesEnumerator',
	'{1B28061F-6494-47D6-B8A4-3F6EF0DF0642}' : u'FaceShellDefinitions',
	'{34ACFD9F-B9B0-4D81-B44C-55AEEAEE16BC}' : u'BIMComponentPropertySets',
	'{22A94C59-66DE-4B31-BA10-BCBB774B4AAF}' : u'FlatPunchResults',
	'{4E19FF37-38A9-494F-AC1E-557D5D01CDB4}' : u'AssemblyJointProxy',
	'{BA9FAF37-B4D2-45C1-BBBE-78E7B8ECB219}' : u'DWGPointProxy',
	'{587A7801-DF86-4DC8-BD20-ADA5FB1193C2}' : u'SurfaceTextureISODefinition',
	'{C0E159EB-2FFE-483E-B4CE-585BEE76E710}' : u'TwoPlanesWorkPlaneDef',
	'{1B73EA84-1B63-4F24-B295-B50EA9215C26}' : u'ObjectVisibility',
	'{B142CBF7-AE52-4AC4-ADAB-7A36A2A9A834}' : u'ClientBrowserNodeDefinitionSink',
	'{955CB4BF-782F-4A58-8538-4E1028EA5D20}' : u'RepresentationEvents',
	'{F8841598-132A-4A18-BE1F-EBDD2067C648}' : u'_VbaImplementationEvents',
	'{49A9C1BC-D718-4DCB-AAD8-8FB4285EFA45}' : u'AliasFreeformFeature',
	'{D93EE206-0CA6-401E-B74E-0D9E4F924751}' : u'StylesManager',
	'{6322C608-F92C-4CBB-9C17-B1661DA641AB}' : u'ProgressBarSink',
	'{C2083475-A259-414A-BED9-FC43291F4455}' : u'_DocPerformanceMonitorSink',
	'{A52071CF-BF9F-45BA-A7D5-E5AAA2682B4D}' : u'StyleEventsSink',
	'{0B8D52D2-8147-4407-B2E3-D982ED775F0C}' : u'SurfaceGraphicsFaceList',
	'{3697D2E9-C4C2-4FF5-A60D-F5EC68EACD27}' : u'DimensionStyle',
	'{4B01DD28-A1AF-4387-9F24-2B87442C1E94}' : u'UserInterfaceEventsObject',
	'{68517DF3-9E1D-44AA-B12D-08880086D61A}' : u'DrawingBOMs',
	'{062F6086-60DC-4550-93C5-A9B8CEA89ADB}' : u'ObjectDefaultsStylesEnumerator',
	'{F69435CA-41FA-4FDC-8E07-2D677A30AB2C}' : u'UnfoldMethod',
	'{AE309209-288A-4083-BEAB-7DFB7EC9947D}' : u'iMateDefinitions',
	'{7D6FF00B-9613-4E95-AA2F-484E089AAEA3}' : u'LinearModelDimension',
	'{33DE76BF-3E58-4EF2-AE90-AA540F2A6C52}' : u'_VbaImplementationPresentationEvents',
	'{EF0F253F-6AF9-40A8-BD13-B136E00B6588}' : u'CommandBar',
	'{E6478D92-2EBD-4363-8C27-A6891E942DBB}' : u'CircularOccurrencePatternProxy',
	'{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}' : u'CommandManager',
	'{715899F9-C5E6-4A31-96C7-151D74A852B8}' : u'PointClouds',
	'{E41CA526-545A-4782-A383-C44FC7523552}' : u'BIMConnectorDefinition',
	'{279EB42E-C733-4AA9-BFA8-2A8FCF2B2A4D}' : u'FreeDragMoveOperation',
	'{5993FFB7-877A-4AFA-9BAA-73D627DE0D39}' : u'FileDialogEventsObject',
	'{2F041963-4B68-415F-BE07-F1FB6C6342A3}' : u'LineLengthDimConstraint3DProxy',
	'{6AAD65B4-5F61-42C1-830A-A45C60809D76}' : u'MeasureEventsObject',
	'{0A1F6F03-BA19-49CD-8376-93A85FB08A2A}' : u'ClientFeatureDefinition',
	'{FD16E33C-AE0F-4CB3-8E44-9C6F2A9A8FF6}' : u'RevolveFeatureProxy',
	'{C66A1C65-43C3-4F1C-A22C-089F3F03349A}' : u'ModelDimension',
	'{744F35C4-CD6F-46C3-87B8-80425AB4AFA2}' : u'BIMConduitConnectorDefinition',
	'{6CBA9E79-C13B-46ED-BB14-6541A63B1A16}' : u'SketchEntities3DEnumerator',
	'{8A551127-A520-46FD-A9C4-5ECD271576FC}' : u'FaceDraftDefinition',
	'{FB83111D-DED9-462D-9BC5-95A6933ADF4C}' : u'RevisionTableRow',
	'{D0786DD9-AD8A-431B-B2A9-388211ABD7DD}' : u'ThreadFeatures',
	'{1993ABC5-7080-4CB1-9CE3-406B4B70B951}' : u'PointHolePlacementDefinition',
	'{1691F301-F2AF-48F4-946F-185CEF9A7EEE}' : u'Preparations',
	'{5538440B-E168-4C38-B817-56F50B538C96}' : u'BOMView',
	'{1F3DB03A-352E-44EA-807B-8D3C4FCF855C}' : u'ProjectedCutProxy',
	'{E083158B-C56B-4CB0-B637-C56896BDAF1C}' : u'ModelSurfaceTextureSymbol',
	'{63F4004E-C9FE-4B75-A7CB-F526543A5C29}' : u'CornerFeatures',
	'{5EC2AE01-F47C-4E11-B8CD-67A017E07132}' : u'GrillFeature',
	'{A907AE85-A78F-11D5-8DF8-0010B541CAA8}' : u'PartsLists',
	'{E54B3528-EB27-4A1A-8403-48A9846C93BB}' : u'GraphicsColorSet',
	'{A907AE87-A78F-11D5-8DF8-0010B541CAA8}' : u'PartsList',
	'{A907AE89-A78F-11D5-8DF8-0010B541CAA8}' : u'PartsListColumns',
	'{3C49109C-CDDD-4D4F-A4F3-A0CA3E9EF7F2}' : u'DistanceHeightExtent',
	'{A907AE8B-A78F-11D5-8DF8-0010B541CAA8}' : u'PartsListColumn',
	'{A907AE8D-A78F-11D5-8DF8-0010B541CAA8}' : u'PartsListRows',
	'{A907AE8F-A78F-11D5-8DF8-0010B541CAA8}' : u'PartsListRow',
	'{A907AE91-A78F-11D5-8DF8-0010B541CAA8}' : u'PartsListCell',
	'{FC6C5BEB-A2CE-4249-8C31-6B0E1E8030A9}' : u'QueryManager',
	'{A907AE97-A78F-11D5-8DF8-0010B541CAA8}' : u'TextBoxes',
	'{A907AE99-A78F-11D5-8DF8-0010B541CAA8}' : u'TextBox',
	'{71F90E58-8C83-4C68-9B75-2E14F8BF3A23}' : u'ConcentricHolePlacementDefinition',
	'{4479E5B2-48BF-4760-BA24-0A0CE854DF24}' : u'BooleanAssetValue',
	'{5F0359BB-A074-4CD1-98EF-F66DAE4649E9}' : u'FloatAssetValue',
	'{C7AF47E6-3FDE-469F-B258-85FE0390E7DA}' : u'iAssemblyTableColumns',
	'{FB78F43A-8F10-40F3-8C04-62EEA948C716}' : u'DerivedPartEntity',
	'{A907AEAF-A78F-11D5-8DF8-0010B541CAA8}' : u'Border',
	'{A907AEB1-A78F-11D5-8DF8-0010B541CAA8}' : u'BorderDefinitions',
	'{A907AEB3-A78F-11D5-8DF8-0010B541CAA8}' : u'BorderDefinition',
	'{A907AEB5-A78F-11D5-8DF8-0010B541CAA8}' : u'TitleBlockDefinitions',
	'{A907AEB7-A78F-11D5-8DF8-0010B541CAA8}' : u'TitleBlockDefinition',
	'{DBABE302-0C4A-4F2D-B67B-768F87C54E32}' : u'SketchFixedSpline3DProxy',
	'{A907AEB9-A78F-11D5-8DF8-0010B541CAA8}' : u'TitleBlock',
	'{A907AEBF-A78F-11D5-8DF8-0010B541CAA8}' : u'TextStyles',
	'{A907AEC1-A78F-11D5-8DF8-0010B541CAA8}' : u'TextStyle',
	'{FB4D47B9-777E-49C5-99CB-9CE5C345D66E}' : u'RepresentationEventsObject',
	'{E8528224-258B-471F-81E3-1F276425BC39}' : u'ObjectDefaultsStyle',
	'{BDAFC08A-5CAC-4E5A-B715-F2BCAFFD5282}' : u'BalloonTipObject',
	'{A907AED1-A78F-11D5-8DF8-0010B541CAA8}' : u'SketchedSymbolDefinitions',
	'{A907AED3-A78F-11D5-8DF8-0010B541CAA8}' : u'SketchedSymbolDefinition',
	'{A907AED5-A78F-11D5-8DF8-0010B541CAA8}' : u'SketchedSymbol',
	'{A907AED9-A78F-11D5-8DF8-0010B541CAA8}' : u'SketchedSymbols',
	'{4DA70A52-6AE0-4674-95A6-6D7E563CD589}' : u'ReferenceKeyEventsSink',
	'{46D8F255-F1A2-4C52-8D4B-29C02C8198FF}' : u'PunchNotes',
	'{A907AEE3-A78F-11D5-8DF8-0010B541CAA8}' : u'DefaultBorder',
	'{56C3574C-13A4-46AB-B981-4B45784B2156}' : u'AssemblyConstraintsEnumerator',
	'{63E2B412-8EDA-496C-BAF6-A28928F74091}' : u'DrawingDimension',
	'{99C8344C-60E3-46CA-A32D-1EF2010EB01D}' : u'BIMConnectorLinks',
	'{F3E768AB-B2BC-42B4-B95F-ED49BE550257}' : u'FeatureControlFrame',
	'{766A9447-A604-43C8-9393-2D2709837D1E}' : u'Asset',
	'{E52803C6-7F1E-4D7B-9C0E-D4FA6BFFA00D}' : u'BIMPipeConnectorDefinition',
	'{9E7FC002-194A-4CB7-9862-4A3308F586C8}' : u'TransitionalConstraintProxy',
	'{67CF708B-CA38-419D-8016-19CEAA5FBB7D}' : u'FileDescriptor',
	'{BA80AE34-5BB2-4C90-BFDE-64DA56286813}' : u'FileDialog',
	'{8E02BFEC-2C95-4685-83B8-E215F98BA844}' : u'CustomConstraint3D',
	'{2B564484-AF79-47BF-836B-15F288717791}' : u'FoldFeatures',
	'{D2F65CFD-A8D7-44D1-8262-9FD5BCA8FECA}' : u'ImportedComponents',
	'{6D92FD04-C569-4F19-8A54-A83B1CBA7080}' : u'TranslateTranslateConstraint',
	'{93545775-90CE-4E69-B0A5-4E3F23C30677}' : u'DWGBlockReferenceProxy',
	'{05EC93C4-CC47-450C-A826-FEC6692AD526}' : u'Centerline',
	'{6CFC2B95-2B15-486D-A100-0B83DA795626}' : u'MeasureEvents',
	'{BCDD5058-E7D5-4E88-8EF8-8D6370E0CBA3}' : u'BOMRowsEnumerator',
	'{0FC5FA72-0397-4522-9E58-764385FA9B69}' : u'FilenameAssetValue',
	'{956DA506-F82D-4924-A000-C1A66CDB3B49}' : u'GraphicsCoordinateSet',
	'{80DBF4D7-FEC3-454C-BF1C-65BCDB27188C}' : u'SketchFixedSplines3D',
	'{4AF3870E-AB8B-4567-94B5-C1850D292111}' : u'SketchArcs3D',
	'{ACC63CB3-EBF2-48E3-A0F4-48E3FC13ECED}' : u'ComboBoxDefinitionSink',
	'{B134AF6F-7FE5-4485-B5E8-493541D94E3F}' : u'FeatureBasedOccurrencePatternProxy',
	'{A7E03766-451A-4BFB-B4CF-FE7F1F258494}' : u'DirectEditDeleteOperation',
	'{691AF5CB-83DC-4AF2-B689-F70AFB0D5020}' : u'InteractionGraphics',
	'{BFA33A07-C4CE-4CAD-89BC-AF2C49FD5029}' : u'CoincidentConstraint3DProxy',
	'{E2012607-EC0A-4F31-A888-E389AF5667E7}' : u'DWGBlockReferencesEnumerator',
	'{AADD24A8-0094-41C6-BF61-C79E700AA1E2}' : u'PointCloudCrops',
	'{296442E1-7AB3-46B9-8494-7FBB585F6B50}' : u'_VbaImplementationDrawingEvents',
	'{7338F36B-6CD8-4296-90AE-EFEAC0FED72B}' : u'CosmeticWeld',
	'{CADFFDB1-11E6-4684-A35E-7EE2064AA46C}' : u'SweepFeatures',
	'{52223C79-EAAC-45CB-B000-35DBB1494A3D}' : u'ContentCenterDialog',
	'{2AD0B878-13E1-4BB0-BDFF-BBAA7DA553DD}' : u'LipFeatures',
	'{95C6C576-FC7A-4B16-B565-BFABEF69B013}' : u'InventorVBAProject',
	'{3978BB7A-4A07-475B-BD57-13A05A343EDB}' : u'FlangeDefinition',
	'{5DF8601E-6B16-11D3-B794-0060B0F159EF}' : u'ComponentDefinition',
	'{5DF8601F-6B16-11D3-B794-0060B0F159EF}' : u'ComponentDefinitionReference',
	'{5DF86020-6B16-11D3-B794-0060B0F159EF}' : u'ComponentOccurrence',
	'{5DF86022-6B16-11D3-B794-0060B0F159EF}' : u'ComponentDefinitions',
	'{5DF86023-6B16-11D3-B794-0060B0F159EF}' : u'ComponentDefinitionReferences',
	'{5DF86024-6B16-11D3-B794-0060B0F159EF}' : u'ComponentOccurrences',
	'{69190E26-316F-47BD-AE75-8B64641C18C8}' : u'PrintManager',
	'{7DDF539F-7AFE-44BD-BAF9-BBAE51A93721}' : u'MiniToolbarCheckBoxSink',
	'{A765255E-0264-4316-9F81-F5B051281001}' : u'AngularModelDimensionDefinition',
	'{BF8CF130-DAD5-444E-9DED-16AD1178DE2F}' : u'FlatPatternPlates',
	'{206F590B-1854-41A8-9ACE-CB18BCF1154B}' : u'ContourRollFeatureProxy',
	'{F55C4A2E-FEBB-4EEA-872D-C54B481B0948}' : u'ContentCenterDialogEventsObject',
	'{FE97EF73-E784-47FB-AA0B-D1891A8F1DF4}' : u'DockableWindows',
	'{DF566DD8-E3A3-45E3-844D-78F8C072ECDC}' : u'HemFeatures',
	'{D007B6F9-71BB-48FF-B14C-EE5D633CB0C3}' : u'UnitsOfMeasure',
	'{ABA7FFC5-E604-498E-B1B1-B829D4E059EC}' : u'HoleFeature',
	'{C18BB14E-4FEF-478B-BF34-4690DE9BFC6C}' : u'MouseEventsSink',
	'{B8E1A8FF-EE38-49CD-BC33-FBA4E8E6073C}' : u'OffsetSplineDimConstraintProxy',
	'{5DF86062-6B16-11D3-B794-0060B0F159EF}' : u'Box',
	'{5DF86063-6B16-11D3-B794-0060B0F159EF}' : u'Box2d',
	'{07FB0B7F-D08F-473F-8EF0-A5E6B4CBA3BC}' : u'Sketches3D',
	'{6C0C1E47-E731-4ECF-8EDD-EF8CE58E395E}' : u'FeatureDimension',
	'{11C8C1C5-74AB-415F-AE6B-F358CE0FDA4C}' : u'DerivedPartTransformDef',
	'{0A73D068-AC6B-4B51-8B6D-913B90A77741}' : u'TangentConstraint',
	'{C6345819-0FAA-45A0-BF96-3C946F130076}' : u'AssemblyOptions',
	'{5FCEA8CE-F9AE-4216-8AAD-2530EC41B619}' : u'DiameterModelDimensionDefinition',
	'{457D2D49-6354-461E-AE0F-2C42B371D313}' : u'DSServer',
	'{5DF86089-6B16-11D3-B794-0060B0F159EF}' : u'SurfaceBody',
	'{5DF8608A-6B16-11D3-B794-0060B0F159EF}' : u'FaceShell',
	'{5DF8608B-6B16-11D3-B794-0060B0F159EF}' : u'Face',
	'{5DF8608C-6B16-11D3-B794-0060B0F159EF}' : u'EdgeLoop',
	'{5DF8608D-6B16-11D3-B794-0060B0F159EF}' : u'EdgeUse',
	'{5DF8608E-6B16-11D3-B794-0060B0F159EF}' : u'Edge',
	'{5DF8608F-6B16-11D3-B794-0060B0F159EF}' : u'Vertex',
	'{5DF86091-6B16-11D3-B794-0060B0F159EF}' : u'FaceShells',
	'{5DF86092-6B16-11D3-B794-0060B0F159EF}' : u'Faces',
	'{5DF86093-6B16-11D3-B794-0060B0F159EF}' : u'EdgeLoops',
	'{5DF86094-6B16-11D3-B794-0060B0F159EF}' : u'EdgeUses',
	'{5DF86095-6B16-11D3-B794-0060B0F159EF}' : u'Edges',
	'{5DF86096-6B16-11D3-B794-0060B0F159EF}' : u'Vertices',
	'{5DF860A2-6B16-11D3-B794-0060B0F159EF}' : u'Cylinder',
	'{5DF860A3-6B16-11D3-B794-0060B0F159EF}' : u'Cone',
	'{5DF860A4-6B16-11D3-B794-0060B0F159EF}' : u'Torus',
	'{5DF860A5-6B16-11D3-B794-0060B0F159EF}' : u'Sphere',
	'{5DF860A6-6B16-11D3-B794-0060B0F159EF}' : u'BSplineSurface',
	'{C08C777F-2E1B-469D-A1A7-E379ED046444}' : u'PunchToolFeatures',
	'{5DF860AE-6B16-11D3-B794-0060B0F159EF}' : u'SurfaceBodies',
	'{5DF860B0-6B16-11D3-B794-0060B0F159EF}' : u'CurveEvaluator',
	'{5DF860B1-6B16-11D3-B794-0060B0F159EF}' : u'Curve2dEvaluator',
	'{5DF860B2-6B16-11D3-B794-0060B0F159EF}' : u'SurfaceEvaluator',
	'{31737D0F-56F3-40B8-8649-C8A5AB945D80}' : u'RotateTranslateConstraint',
	'{F2BCCD2A-83E0-4528-A039-318A93C7ABBA}' : u'TangentConstraint3DProxy',
	'{EF562DD1-92FA-11D4-8DE0-0010B541CAA8}' : u'ComponentOccurrencesEnumerator',
	'{4735D53B-FEF2-4671-9430-3D60964D850B}' : u'RegionProperties',
	'{51BAA695-F419-4D00-B6C5-7C32F4114562}' : u'CommandBarBaseCollection',
	'{6D634B29-2066-44CA-AA97-D87A2C95A172}' : u'iMateResult',
	'{41E90FED-639B-468D-A09E-30363D40DE7F}' : u'SketchesEnumerator',
	'{4D662CE2-D29B-42E0-BA74-715C311E5630}' : u'SurfaceBodyDefinition',
	'{B2EC7987-2BDE-47F6-8EE7-534C7B854B2B}' : u'CustomPropertyFormat',
	'{78B3596A-176A-43F5-A65C-4BDFFC042236}' : u'MeasureTools',
	'{08C74C78-5F8D-40B3-9D57-4507D5CEA79C}' : u'SketchEllipticalArcs3D',
	'{B13C95CF-8B79-4F03-8EF0-BE81A400529F}' : u'SnapFitFeatureProxy',
	'{8B6FA30B-DC7A-4603-8793-445D70FF073E}' : u'PartFeatureExtent',
	'{7FF4B4DA-DF87-4E58-8727-ADEBA3B6452B}' : u'SurfaceTextureSymbol',
	'{1F222D21-CBB5-4FC4-A6CF-0387224A7F2C}' : u'BIMElectricalConnectorDefinition',
	'{EFA08B24-F116-4751-90FA-46ADE09BF0B3}' : u'AttributeSet',
	'{18517A46-ABB7-4285-94B4-35B3277880F1}' : u'iAssemblyTableRow',
	'{2A5668A8-5EA5-45AE-B3DB-A4C7BD2F7E9D}' : u'SweepFeatureProxy',
	'{7AD96A84-A539-4220-B9AD-7A2854D518B8}' : u'ModelDimensions',
	'{EE21CD75-39FD-4683-BE24-BFBB9CA66EB4}' : u'GeneralDimension',
	'{C5A7AC9D-A15D-46B9-8582-31BD4E8D05CD}' : u'DWGPolyline2DProxy',
	'{B97AC4F4-708A-431E-90BA-AFDCC6623A84}' : u'ModelLeaderNotes',
	'{9B108AAB-237A-460D-BC99-40FAF5EABD65}' : u'RuleFilletFeatures',
	'{3CBE8AA5-3D92-11D5-8DEE-0010B541CAA8}' : u'WorkAxisProxy',
	'{CF891949-B3AD-4A38-9254-7CAFE0F3B7F6}' : u'DerivedPartComponents',
	'{E9455662-85DE-499A-9965-81270D314D70}' : u'DWGEllipticalArc',
	'{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}' : u'ObjectsEnumerator',
	'{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}' : u'LoftDefinition',
	'{F05DFBBD-F824-48A1-8272-A62F1A524F42}' : u'ExtrudeFeatures',
	'{E5CFA472-5D23-4486-8D2C-A4D8D564C196}' : u'DWGArcProxy',
	'{4EDC3AD5-669B-40A9-A3DC-3261C16F4642}' : u'PointCloudProxy',
	'{35A16D52-2DE8-4DF8-B8EB-83110BACD270}' : u'ButtonDefinitionHandler',
	'{F8FBACE4-75A7-4493-B2D8-492AC937F3E5}' : u'LoftSectionDimensions',
	'{E521F56F-13D5-4D80-95BA-10CB3B2F5918}' : u'ChamferNotes',
	'{E06998C3-E510-47D3-BE8D-2CD348F24456}' : u'ContentTableColumns',
	'{81807A32-C016-4239-8D61-28B44957393D}' : u'LayoutConstraintProxy',
	'{425EAA71-D590-4893-AFAB-012380A7CEBA}' : u'MateiMateDefinition',
	'{C6A2B48C-DBBC-4BA9-A98B-6EB63FB78AE4}' : u'DesignViewRepresentations',
	'{17BE1D0D-0A2B-4A92-9CB2-A9725D391143}' : u'DiameterModelDimensions',
	'{B03877E4-31F6-4B1E-8F38-FCCFD0B0DCAA}' : u'UnfoldFeature',
	'{06460F0C-B76C-49E4-B24A-3C60142219B9}' : u'RotateTranslateiMateDefinition',
	'{6129AB00-E4D1-45AD-B3AE-A873BDF452BF}' : u'SketchArc3D',
	'{221277C1-7963-4539-B2E5-E7E16D3C75AA}' : u'DrawingOptions',
	'{EEE9F58F-FD0B-4862-AE21-BAE203DFE23E}' : u'DrawingCurveSegment',
	'{C5EDE080-C83A-4D7F-9560-B867FD29DFD6}' : u'RevisionTableRows',
	'{1A88CE14-0590-4C13-B58A-C9B7FA1458C5}' : u'WebBrowserDockableWindow',
	'{8A0202C7-6ADF-454C-AF47-09E3027E8E7C}' : u'RipFeatures',
	'{1D32B73F-D1F8-4E1C-80B9-590FA6F008B2}' : u'FlatBendResults',
	'{3C83A20C-1648-40C3-9A28-FFDE72124D2C}' : u'ProjectedCuts',
	'{501F1ACA-00D4-47CF-A0D1-1F4D1BB1A633}' : u'PlanarMoveDefinition',
	'{8742661B-564A-4CE3-A32C-6F08894FB760}' : u'LipFeatureProxy',
	'{21BBAED3-F2FD-4A60-9AE4-7A10A8E2BC2D}' : u'CornerRoundDefinition',
	'{3FC94EB5-AEBD-4F3F-A2A4-B6CE57113C01}' : u'InventorServer',
	'{285898F7-E731-44FA-B327-540394EBE313}' : u'HelpEvents',
	'{68AF2955-0901-433D-B7C3-D91D637DD21C}' : u'ClientFeatures',
	'{C173A077-012F-11D5-8DEA-0010B541CAA8}' : u'OffsetDimConstraint',
	'{59D3FA3A-ACE0-11D3-B79A-0060B0F159EF}' : u'ApprenticeServerDocuments',
	'{650A171B-40E1-4C3B-B55E-DFB3D31C2CB8}' : u'ContentCenterOptions',
	'{986FCF92-8A47-4DEC-9007-DD852292DE71}' : u'PartOptions',
	'{AA044AA1-D685-11D3-B7A0-0060B0F159EF}' : u'AssemblyComponentDefinition',
	'{AA044AA2-D685-11D3-B7A0-0060B0F159EF}' : u'AssemblyConstraint',
	'{AA044AA3-D685-11D3-B7A0-0060B0F159EF}' : u'AssemblyConstraints',
	'{4758367B-5DAF-4CE3-BDF1-189FAD8D6BD2}' : u'RevisionTableStyle',
	'{F69024F9-970E-4223-82DD-6B4F0E3AF57F}' : u'CornerDefinition',
	'{5F24EB5E-169E-47C1-9C3D-401A01F4415B}' : u'SurfaceGraphics',
	'{7693ED6C-807E-443A-A3C0-A63010E5625A}' : u'RibbonPanels',
	'{C173A07F-012F-11D5-8DEA-0010B541CAA8}' : u'DiameterDimConstraint',
	'{3E0ED07A-F5ED-46BF-8903-EBC1B409A270}' : u'AssetTexture',
	'{41ADE507-16D9-4103-BD0C-FA1C196B9DAA}' : u'SheetMetalFeatures',
	'{DD8AB7FC-77D4-4EA8-83A9-A0C868DABFC0}' : u'ReferenceComponent',
	'{1B986C9A-B329-45B0-B682-95F04FF16E87}' : u'DerivedPartComponentProxy',
	'{7958ED54-7E29-490B-9963-BF61E39E98E0}' : u'CosmeticBendFeatureProxy',
	'{B0A76319-7649-4B77-9159-0975E700253B}' : u'MoveFaceDefinition',
	'{4A2D7396-8300-4424-B9B7-EB9A8CA5D89E}' : u'CosmeticWelds',
	'{2FA1D3CF-EAFF-4D47-9E13-E5B074C1565C}' : u'MassProperties',
	'{F20B72F3-D856-45E8-A71A-0753F12D7A10}' : u'PointCloudScans',
	'{78D752FD-9090-4AEA-9CF2-247ABA9D1936}' : u'SplitFeature',
	'{582865AB-F113-4939-8796-336EA266F8B2}' : u'CommandBarBase',
	'{C77D9639-C58A-4E5A-BAE0-14966E37DDEE}' : u'FaceDraftFeatures',
	'{71360893-BD99-4D41-96CD-A3BD2AE0DB4D}' : u'CoreCavityFeatureProxy',
	'{F30319D0-9C9E-40BC-96AC-62D2E9302E5B}' : u'TrailsEnumerator',
	'{F8FEB6D6-1D1A-4472-9429-1FF06A76DB9E}' : u'DriveSettingsObject',
	'{5C93A2CD-ECCA-4998-9DC4-D439BD9FE3DB}' : u'DraftAnalyses',
	'{9B5D2EC6-A4BD-4B3A-8A34-069EE52B009D}' : u'ButtonDefinitionSink',
	'{F777456B-314C-4F8E-87E0-196CB7FC8D32}' : u'DrawingViewEventsSink',
	'{C52EE54D-B18E-4CB3-AEE3-7D0375F92948}' : u'ParametersEnumerator',
	'{54E4411A-7349-4591-991E-9F930A01EB83}' : u'BendDefinition',
	'{598714D9-653D-4D2B-B7BB-139C3E9E38B1}' : u'UserCoordinateSystemDefinition',
	'{C173A091-012F-11D5-8DEA-0010B541CAA8}' : u'Arc2d',
	'{8AF6DB71-B75D-4D21-A837-4A6699E972BC}' : u'BOM',
	'{F6F33557-6984-11D5-8DF3-0010B541CAA8}' : u'DebugInstrumentationObject',
	'{F6F33559-6984-11D5-8DF3-0010B541CAA8}' : u'DebugInstrumentation',
	'{F6F3355B-6984-11D5-8DF3-0010B541CAA8}' : u'DebugInstrumentationSink',
	'{A2F174A9-9D82-4AF1-B80C-67FB45B59923}' : u'TableFormat',
	'{3DFE3282-5B67-431A-A890-040098957C1C}' : u'Balloons',
	'{68D1E13F-F6A4-47FD-AAC0-5545A57B712B}' : u'InteractionEventsObject',
	'{A7AF22DD-A689-4BEA-84BF-AEE3496BB26E}' : u'ContourFlangeFeatures',
	'{F8F30CD3-A44B-4C8A-B9D2-287361B0BD26}' : u'RotateRotateConstraint',
	'{7BF80981-BF32-101A-8BBB-00AA00300CAB}' : u'IPictureDisp',
	'{DA33F19F-7C3F-11D3-B794-0060B0F159EF}' : u'Matrix2d',
	'{DA33F1A3-7C3F-11D3-B794-0060B0F159EF}' : u'PartComponentDefinition',
	'{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}' : u'PartFeature',
	'{DA33F1A5-7C3F-11D3-B794-0060B0F159EF}' : u'PartFeatures',
	'{5D175430-8A8D-47F7-AABE-50C2E9B65D89}' : u'BreakOutOperation',
	'{55DBDB4E-BC61-4D53-84F6-86CF24267DD8}' : u'DrawingStandardStyle',
	'{F0541886-3BF7-4E4D-8A11-D113578E5110}' : u'RevolutionAndHeightCoilExtent',
	'{E9E1E669-7C31-486B-A5A6-FD0825ABCB28}' : u'BrowserNodeDefinition',
	'{F9885CB4-7B68-45E3-953F-B287BE1C6FAF}' : u'AssemblyWorkAxisDef',
	'{4F16A71E-1337-40DE-B13F-DB996F9A716E}' : u'FilletFeatureProxy',
	'{159DE5F6-0CF1-48F6-87AA-2865091762D3}' : u'ContourFlangeFeatureProxy',
	'{BF18368A-A9B1-4295-9242-18D1AC91F8D3}' : u'SketchOffsetSplineProxy',
	'{5D8B9732-07F2-4E90-A4AB-C98FB56944A1}' : u'ReplaceFaceFeature',
	'{54D7BD09-6FA0-46F5-B427-F2432560A8C3}' : u'MiniToolbarButtonSink',
	'{3A32960B-A64E-4257-B24F-240C7E68C065}' : u'DockableWindow',
	'{0F8F253B-5ED8-4AE0-9C62-3DEFDCCD0BC4}' : u'ShellThicknessFaceSet',
	'{CD4C47ED-C403-4F42-B3BF-0A90F3E89D81}' : u'ApplicationEventsSink',
	'{AA1A04EB-B571-4568-86E6-7732B8330E9C}' : u'BendsEnumerator',
	'{FC6CACA3-208B-40AD-8B3A-0949B6CBBD3A}' : u'ImportedModelEntities',
	'{4A943DD0-592A-4E36-8E2C-D2E9DD54B2F5}' : u'FlushiMateDefinition',
	'{773586BE-A5CE-422F-9036-FAFC8451F011}' : u'SweepFeature',
	'{F93BBC7A-1A75-47D8-9E93-FD1B188AB4DB}' : u'DriveSettings',
	'{BAC6577B-6985-4B55-BADC-8113EFF69A3C}' : u'CompositeiMateDefinition',
	'{C802F139-6C51-4A73-ABAE-BF5E88687E00}' : u'RevisionTableColumn',
	'{206AFE1A-FAFA-4DAF-A569-1AF60672D63B}' : u'BendNotes',
	'{24FAC734-1A3D-404E-A28B-7CC1AD47DCA1}' : u'InventorVBAComponents',
	'{88C36A1E-2212-4E9C-BBDB-3155DC8C06E9}' : u'FreeformFeature',
	'{6D7C8AC8-722D-46C8-B6D9-F6001F1EDD2D}' : u'DerivedPartComponent',
	'{31B7388A-3B81-4568-B697-9C1F0D09E7AC}' : u'LegacyDistanceHeightExtent',
	'{6757C085-699B-474B-9566-61221A64A09F}' : u'FeatureGraphics',
	'{2BC16E62-07F5-4106-B5BD-58C7C660DA2C}' : u'SketchHolePlacementDefinition',
	'{209DF795-8088-4158-969C-0CC120E0A2A3}' : u'SplitFeatures',
	'{FA48B024-CC3B-458F-B0EB-6FE4CBEC35DD}' : u'SketchCircles3D',
	'{B9694561-1C36-4D14-9930-4B8152E1984F}' : u'CosmeticBendFeature',
	'{942BDD59-6622-4CF0-BAD6-4F4EAD7A4DCA}' : u'DWGBlockReference',
	'{7C693E2E-D4D3-433A-A90F-112E3C52E543}' : u'SketchSplineHandle3DProxy',
	'{CF3DEE6F-DBB2-4393-A409-5D0ADC6CB12C}' : u'Machining',
	'{CE96A92D-B3F9-4607-9E47-30722770F9AD}' : u'DWGPoint',
	'{26F03E86-7DA4-4789-AACC-DE231C4C35E5}' : u'ContentCenterDialogEventsSink',
	'{CFA8AC15-B4C1-4703-A672-DAED79017FF3}' : u'AngleiMateDefinitionProxy',
	'{C38DE680-2374-487B-86F8-E3DA8012DE66}' : u'SketchEquationCurves',
	'{75091477-A808-4B93-AF11-14C0CD466611}' : u'WireframeDisplayOptions',
	'{84526202-5E30-403F-8700-397646B4BBD0}' : u'iFeatureEntityInput',
	'{BA8A81FD-71F7-4BE4-A009-1CC6731723FD}' : u'ClientFeatureElement',
	'{EC5AD11E-A3AB-4C86-85BD-61DEBF623987}' : u'ProjectAssetLibraries',
	'{BABF5BAF-9878-11D4-8DE2-0010B541CAA8}' : u'PartEventsSink',
	'{0169EC1F-0694-4353-B28D-3D74B59402D0}' : u'TutorialsManager',
	'{5B078EF2-5839-4B6A-97D1-BB8F5D9CFD78}' : u'RibDefinition',
	'{249D0F99-CAD8-4B05-9A8C-AAF415CEA2DC}' : u'DWGPolyline',
	'{AC581AF3-E3C8-4011-9140-3B64D555FA05}' : u'FlushConstraint',
	'{11D880AF-2B60-4816-A74A-73526CFE6FDD}' : u'BrowserNodeDefinitionSink',
	'{579B848D-41FD-4A4E-87F8-58A213360623}' : u'SketchEvents',
	'{A335F5F6-7194-409E-94A7-45B617264920}' : u'FilletVariableRadiusEdgeSet',
	'{9374403D-49B0-4DA3-A4CA-55DDAB40D8E1}' : u'FilletConstantRadiusEdgeSet',
	'{1F6B29F0-6C04-4D11-8ACE-9D41C2904FCD}' : u'DocumentEventsObject',
	'{49F63CD1-212B-4BCB-B43C-5CAF969A2EAC}' : u'SilhouetteCurveProxy',
	'{12EC238A-7178-44C6-BF92-F95F87CD7592}' : u'DerivedAliasComponents',
	'{298849A9-ECAB-4234-9675-6FAA66A95E4D}' : u'ReferenceFeature',
	'{6886F154-F98E-4287-BF33-F63CB776B6B2}' : u'PointInference',
	'{6886F155-F98E-4287-BF33-F63CB776B6B2}' : u'PointInferenceEnumerator',
	'{C16DE191-DEEC-449E-BEF1-1F1220233FB3}' : u'LoftedFlangeDefinition',
	'{9BC9A7EC-A0AD-433B-BB3C-9AC30C9030E4}' : u'UserInterfaceEventsSink',
	'{AF22C0E0-AEBC-4009-BD3E-85EBF9C9ED58}' : u'AnalyticEdgeWorkAxisDef',
	'{5A213EAD-8C62-4EE8-B99A-61A09F2F56E3}' : u'MiniToolbarComboBoxSink',
	'{E0B90B3E-0907-49B2-8E51-438C950F3A4B}' : u'TableStylesEnumerator',
	'{ABC49BF6-3E83-45A6-AF98-059245620FF4}' : u'iFeatureTableCell',
	'{AE621339-6CA8-486C-BF06-E683D2EE3A8E}' : u'_SegPerformanceMonitor',
	'{13A31354-BFF7-45CC-B749-2CE174780E77}' : u'HoleTable',
	'{AE0AA5DD-80A7-4094-B58C-06304422CE34}' : u'CompositeiMateDefinitionProxy',
	'{6ADEEB5C-21C6-4995-91AA-7FD0CE1D0073}' : u'DrawingBOMRows',
	'{38876920-588A-4F80-A4B1-1F2E3562FB19}' : u'GroundConstraint3D',
	'{AB36A045-09FE-4A67-8637-E08CC2735092}' : u'_VbaApplication',
	'{63C5D5FD-8348-4246-BE53-619E8C48EC6F}' : u'RevisionTableCell',
	'{1FA42157-89A8-4DA0-A943-888BF014E072}' : u'HoleTableStylesEnumerator',
	'{080ECFB1-9C78-4A73-8FC9-7A438D08B3A6}' : u'DirectionAndDistanceMoveDefinition',
	'{57184DE5-2055-47CD-BC40-0277AD066D70}' : u'FeatureDimensionProxy',
	'{762B1B03-F049-467E-8BFC-DB28CF0DAD27}' : u'ContourRollFeatures',
	'{3283562C-885D-4693-9C77-4A60865FD185}' : u'PanelBar',
	'{C7EAA071-3EFA-4D2F-87BD-C41ABA98C678}' : u'BossFeatureProxy',
	'{5401A856-D03A-4418-AAA2-F1B677FA410D}' : u'TriadEventsSink',
	'{545F2567-592E-45DA-A262-77BD7E546F7A}' : u'HighlightSet',
	'{53A282CD-46BF-4A34-BE2D-1CB7FF469B34}' : u'SurfaceTextureGBDefinition',
	'{8AAC5924-81F8-4760-9BA0-3BD408FA7BA5}' : u'MiniToolbarDropdownSink',
	'{6AC3D773-1202-450D-9CD2-3557B1395C64}' : u'SheetFormats',
	'{1CEE32D6-4997-4E37-ADBB-9AE5873BF30D}' : u'RuledSurfaceFeatureProxy',
	'{E8D1DB25-5BBF-4635-B2A9-2ECC3A150373}' : u'MoldDefinition',
	'{037C3FDB-8A3C-443F-8CF6-993D3295335C}' : u'TextBoxConstraint',
	'{A095B86B-84EF-4364-888E-1F6F03EAA73F}' : u'MaterialAsset',
	'{669AFAAA-7F38-44FB-B50A-161D5C713C69}' : u'RestFeature',
	'{F98E10EB-6BA5-461D-A3D7-5A90CCE47734}' : u'FlatPatternOrientations',
	'{A4555442-8328-402E-BBF5-EDC7D808E522}' : u'TestCases',
	'{F8957621-7E89-4CB8-AFCA-CE11A556E7A2}' : u'ThreadFeature',
	'{BA9EC28C-765B-4481-8A8C-20489290B35E}' : u'AssemblySymmetryConstraint',
	'{3485FEA9-8865-44EE-8F03-72F46DAB0634}' : u'PointCloudPoint',
	'{EB7E9B67-F77A-4ACE-A3CB-1D5C93F7EE9D}' : u'LayoutConstraint',
	'{92353969-0350-11D3-B787-0060B0F159EF}' : u'GraphicsPreferences',
	'{9235396B-0350-11D3-B787-0060B0F159EF}' : u'ObjectsEnumeratorByVariant',
	'{9235396D-0350-11D3-B787-0060B0F159EF}' : u'UserInputEvents',
	'{AB61EB61-7785-4854-9498-8210B3DA80B2}' : u'CornerChamferFeatures',
	'{4FD9CE51-8E4D-4E4B-865F-FC4F0D5A0D5C}' : u'TangentiMateDefinitionProxy',
	'{46D51BD4-B58D-4C94-BA7A-124B184AC687}' : u'AttributeManager',
	'{8C1243A8-F557-4626-A5F1-8B9F988B2EFC}' : u'CoreCavityFeature',
	'{135F0952-BF41-444D-A962-8A7805AB2E78}' : u'SketchControlPointSplines',
	'{BD020927-670F-4F30-943B-75A2EC87E052}' : u'SketchLine3DProxy',
	'{D65B8777-CF40-4542-9A0F-28F2F6EF0678}' : u'RibFeature',
	'{38D353FC-D30E-4B08-B73A-785787D4D7AD}' : u'RipFeature',
	'{E6885A36-3C1C-43A1-9206-81706779DA32}' : u'BendFeatureProxy',
	'{8DD13222-E35F-4EEA-93BA-87F73A069481}' : u'RadiusDimConstraint3DProxy',
	'{A031AE7E-B6DF-49AB-820F-51FF71C1364A}' : u'ChangeDefinition',
	'{B00506C6-BEB7-47F6-8B1B-A5CB5DCD09B3}' : u'FileManager',
	'{28DD48B5-8D70-11D4-8DDE-0010B541CAA8}' : u'WorkAxes',
	'{28DD48B7-8D70-11D4-8DDE-0010B541CAA8}' : u'WorkAxis',
	'{28DD48B9-8D70-11D4-8DDE-0010B541CAA8}' : u'LineWorkAxisDef',
	'{C10BEC9D-DBA2-4035-9D15-11EA363B9A00}' : u'DrawingEvents',
	'{FA403DAE-32E0-4C17-BB7C-CD3626A9BFA9}' : u'DragContext',
	'{28DD48BF-8D70-11D4-8DDE-0010B541CAA8}' : u'RevolvedFaceWorkAxisDef',
	'{CB8542A0-1559-4E06-BAAE-EFA0BFEF86A7}' : u'CutFeature',
	'{112F95FB-41E9-466C-9ACC-1074F5512831}' : u'ClientFeatureElements',
	'{28DD48C3-8D70-11D4-8DDE-0010B541CAA8}' : u'LineAndPlaneWorkAxisDef',
	'{28DD48C5-8D70-11D4-8DDE-0010B541CAA8}' : u'FixedWorkAxisDef',
	'{28DD48C7-8D70-11D4-8DDE-0010B541CAA8}' : u'WorkPoints',
	'{28DD48C9-8D70-11D4-8DDE-0010B541CAA8}' : u'WorkPoint',
	'{28DD48CB-8D70-11D4-8DDE-0010B541CAA8}' : u'ThreePlanesWorkPointDef',
	'{F7EC4513-DB91-4D3D-ABB6-699D301F4387}' : u'FlatBendResult',
	'{28DD48CF-8D70-11D4-8DDE-0010B541CAA8}' : u'LineAndFaceWorkPointDef',
	'{28DD48D1-8D70-11D4-8DDE-0010B541CAA8}' : u'PointWorkPointDef',
	'{E25D1002-8B00-4E7A-A6F3-DF7BDCC7A63A}' : u'DWGPolylinesEnumerator',
	'{28DD48D3-8D70-11D4-8DDE-0010B541CAA8}' : u'MidPointWorkPointDef',
	'{28DD48D5-8D70-11D4-8DDE-0010B541CAA8}' : u'FixedWorkPointDef',
	'{1CA68293-D200-42E3-B54E-FEB349B302D3}' : u'CircularPatternFeatureProxy',
	'{DA05EA7F-D509-4D65-AA86-AB596110425C}' : u'ThreadFeatureProxy',
	'{9FEBA8BF-6BB5-421E-82DE-F1C4A1639C70}' : u'Layer',
	'{8EB2E33C-2CF3-41E6-9B08-C0C0D15DF5EE}' : u'RevolveFeatures',
	'{20C6159F-9ACD-4AA6-B616-1CC57A6F91CA}' : u'FaceOffsetDefinition',
	'{B2CB30BD-4B68-4D6C-8A07-3122FE52E6B9}' : u'StandardThreadInfo',
	'{3CBD2849-0258-4583-9CE0-578A71CB7483}' : u'ReplaceFaceFeatures',
	'{AAF23B5F-E2FE-471C-85AA-E37FCE6DE651}' : u'_DocPerformanceMonitorObject',
	'{E59EEDF7-48F4-4328-AF62-EBBE19BD09C1}' : u'EdgeWidthExtent',
	'{10FCE1AE-95AF-49F4-99FD-B391C181212F}' : u'FoldFeatureProxy',
	'{FD350F5E-E3C9-4268-BCF4-0DEA91B6F8EF}' : u'ArcLengthDimConstraint',
	'{206B59AE-22A6-11D4-B7A8-0060B0F159EF}' : u'Sheet',
	'{206B59AF-22A6-11D4-B7A8-0060B0F159EF}' : u'Sheets',
	'{206B59B0-22A6-11D4-B7A8-0060B0F159EF}' : u'DraftingStandard',
	'{206B59B1-22A6-11D4-B7A8-0060B0F159EF}' : u'DrawingView',
	'{6E5CDAB2-6BA5-4EAD-B357-78646BE0A813}' : u'File',
	'{E861980A-A56F-416A-BF52-876C8A06CE4E}' : u'ShellFeature',
	'{3163F506-342D-4D68-8AB1-39C306DCA6F6}' : u'ParallelConstraint3DProxy',
	'{4B98058A-A232-47FD-9186-1070297036FB}' : u'_VbaImplementationPartEvents',
	'{70109AA0-63C1-11D2-B78B-0060B0EC020B}' : u'Application',
	'{70109AA1-63C1-11D2-B78B-0060B0EC020B}' : u'Document',
	'{70109AA2-63C1-11D2-B78B-0060B0EC020B}' : u'Documents',
	'{68E4EA6F-3BEA-4F89-9335-F46CDF1AB005}' : u'CheckPointsEnumerator',
	'{70109AA4-63C1-11D2-B78B-0060B0EC020B}' : u'Views',
	'{70109AAA-63C1-11D2-B78B-0060B0EC020B}' : u'FileUIEvents',
	'{70109AAC-63C1-11D2-B78B-0060B0EC020B}' : u'DocumentEvents',
	'{70109AAD-63C1-11D2-B78B-0060B0EC020B}' : u'ApplicationEvents',
	'{CFC1C004-270D-4C19-BBE5-5D380A2A7D7E}' : u'FlatPunchResult',
	'{B7B652AD-7411-429D-92AC-663F9183F7F6}' : u'LevelOfDetailRepresentations',
	'{9788ECD5-7355-4AFC-8784-B139CAC98DF3}' : u'iMateResults',
	'{1644E1D5-9BD5-11D5-8DF7-0010B541CAA8}' : u'DrawingSketch',
	'{1644E1D7-9BD5-11D5-8DF7-0010B541CAA8}' : u'DrawingSketches',
	'{369933DF-0F63-46AA-919B-17C91F385C9E}' : u'TestManager',
	'{721CC25E-D96C-4E25-BED5-04EF710574B4}' : u'RuledSurfaceFeatures',
	'{F2930064-7C6A-4FF7-8B87-D98EAC520AA1}' : u'BaselineDimensionSets',
	'{D3EDB5BC-7B47-42B9-9D77-F3A2676EC15B}' : u'DocumentSubType',
	'{400A64D5-7150-42F6-943E-F190518265CA}' : u'GraphicsDataSets',
	'{70984603-E322-4AC8-B6DE-2F5A31AF0910}' : u'Column',
	'{FD93BF70-B8C9-4CEE-8AEB-AAC34B534803}' : u'FaceOffsetPreview',
	'{AAC6E2B5-64B0-440C-A5A2-2AED0D4D7191}' : u'MiniToolbarTextEditorObject',
	'{C5195DC5-0D96-45C2-8E51-BE1A305AC086}' : u'SketchFixedSplineProxy',
	'{8C1619BB-08F8-458D-B1B9-DEE4B63A3D07}' : u'RadiusGeneralDimension',
	'{EF375552-9B4F-4384-9775-4D4EE910DA33}' : u'ClientFeatureProxy',
	'{37D2C08C-F2F6-4D4A-9A53-CEBC0A504DA1}' : u'SketchSplineHandleProxy',
	'{CAD5C3C6-C42C-4F1A-A6E2-5D8746198027}' : u'ClientApplication',
	'{F90311E1-7249-40AF-A597-8AFF681BFA93}' : u'ApprenticeDrawingPrintManager',
	'{609506AD-969B-4FEA-9DA5-D2FC535472FA}' : u'SphereCenterPointWorkPointDef',
	'{F8D97A2E-CC4D-49EF-8FFF-F16F2FB13929}' : u'ProjectPath',
	'{8BEE2F07-0ACD-4A3C-A5BC-E064C8C0DBA8}' : u'ContentTableRows',
	'{559C5073-6378-47FD-AA38-DE0BB46A9268}' : u'NonParametricBaseFeatureDefinition',
	'{10DE860A-67D1-47ED-A23A-291BD48E25E9}' : u'PointCloudRegions',
	'{2F77E2FF-BAD3-43A4-9874-8A99E824E060}' : u'TextBoxConstraintProxy',
	'{6D7C3BDC-9CE1-4F23-82CC-2F001A326F89}' : u'SketchEquationCurve',
	'{70E4E4A0-D090-41AF-8B0A-FFDB9F97B58B}' : u'SurfaceTextureSymbolDefinition',
	'{F41437F2-9B75-4C35-857C-98646F87B551}' : u'DerivedPartUniformScaleDef',
	'{4F1B00F2-FA18-46EA-9C2F-97574189230D}' : u'TeardropHemDefinition',
	'{9048CE40-F6A5-422D-A816-CBE5E03B28D6}' : u'AngleConstraint',
	'{21E8F0AC-DFCD-4800-B07A-6E0C492CC447}' : u'ProjectedCut',
	'{B894B815-AEF1-4FAA-938A-2131E2E5190F}' : u'WebViews',
	'{EAFC6907-44B0-482F-A30F-A46E227A57BC}' : u'DirectEditDeleteOperationProxy',
	'{AB510BBF-B893-47F7-ACC6-8F22836C5D8C}' : u'KeyboardEventsSink',
	'{91B9E6B9-B526-45A8-A7FD-0D2FFD1D6EF5}' : u'ComboBoxDefinitionObject',
	'{64D6BFDF-5B47-48C1-AC74-1BE2C24757B2}' : u'SketchImages',
	'{4FE10280-6679-4500-B7CE-411995D157E7}' : u'InsertiMateDefinition',
	'{30630D32-6807-4D69-8E77-224FD90A21BF}' : u'BSplineCurveDefinition',
	'{076C16D1-4994-11D4-9E0F-0010A4C72F07}' : u'SoftwareVersion',
	'{ECEA0373-8BE9-4970-A696-C967A9718017}' : u'EdgeUseDefinitions',
	'{D7347916-69D8-4972-AEBE-95BE5672BED2}' : u'ProfilePath3D',
	'{71A0E8AF-8F3E-485D-BB40-7C98163F9C14}' : u'VbaApplication',
	'{09A5CE88-D529-499E-82EF-246D8DC4F5B3}' : u'OccurrencePattern',
	'{BD32F579-5C70-453E-BD6F-41D11EF640FD}' : u'KeyboardEventsObject',
	'{AE27E3D2-63C8-4D39-B2CA-A6387AE5D7B3}' : u'BendConstraint',
	'{18DED264-417F-4B81-828C-B8806397C7C3}' : u'DerivedAssemblyDefinition',
	'{E8BE2118-716C-40FD-8BC0-2517B253E4F9}' : u'CollinearConstraint3D',
	'{B3721DAB-0BAD-4296-8C1E-6608FC0F6049}' : u'BalloonValueSets',
	'{5D0AB9A7-FCDB-4815-837B-BDCADEE5CEB2}' : u'UnfoldMethods',
	'{977D767F-C958-44E8-AB59-8F7267DEBBA1}' : u'SurfaceGraphicsEdgeList',
	'{53D15C9C-4920-4B58-8804-8567A94D1643}' : u'ParameterTables',
	'{1D36C391-7C11-45B6-A818-687BA77FD2AC}' : u'KeyboardEvents',
	'{63FB8F95-6B59-4039-B9E1-F6D74E1B3716}' : u'ReplaceFaceFeatureProxy',
	'{26C57F9F-A6AC-4FCD-BE7C-DAE2F0940E8E}' : u'MirrorFeatures',
	'{7C9B84A9-127C-42B6-A0A7-6CDC39B98CDE}' : u'SurfaceGraphicsVertex',
	'{81342C4A-E898-4566-AA9B-735E88874E56}' : u'CustomParameterGroup',
	'{9AB0A7C1-DDEE-400D-B526-287FB2EB6DDD}' : u'CurveGraphics',
	'{A5F4CA62-8A29-408E-AC56-0B95E44CE781}' : u'SplineFitPointsConstraint3DProxy',
	'{8006A016-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchLine',
	'{66829BB6-656B-431C-BF5C-0BF53DBA225D}' : u'ClientGraphicsCollection',
	'{8006A018-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchLines',
	'{A5B827BD-83C7-4CCA-8DCA-06CD10C2237E}' : u'LightingStyles',
	'{8006A022-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchPoint',
	'{8006A024-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchPoints',
	'{8006A026-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchConstraintsEnumerator',
	'{50C3C4B3-5029-44E8-BF12-C1D09530CCF5}' : u'RevisionTableStylesEnumerator',
	'{C6DE930F-09D7-487F-A4C9-401AA8B19879}' : u'GraphicsNodeProxy',
	'{88F528C1-AE9A-457B-8A19-A6224F473A62}' : u'CustomTable',
	'{8006A032-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchArcs',
	'{834C1008-E416-4616-A66B-262175D8E852}' : u'MiniToolbarComboBox',
	'{8006A034-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchSplines',
	'{8006A036-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchEllipses',
	'{8006A038-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchCircles',
	'{2A705B9C-82D0-4F14-9137-164642028E77}' : u'RectangularPatternFeatureProxy',
	'{8006A03A-ECC4-11D4-8DE9-0010B541CAA8}' : u'Profile',
	'{061C46D9-4A71-40EB-9DDC-4D425A6ABE3E}' : u'CutAcrossBendsExtent',
	'{8006A046-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchArc',
	'{8006A048-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchSpline',
	'{8006A04A-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchEllipse',
	'{8006A04C-ECC4-11D4-8DE9-0010B541CAA8}' : u'SketchCircle',
	'{281176E3-4EDC-4F4E-9804-6716B7B9059D}' : u'SmoothConstraint3D',
	'{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}' : u'ControlDefinition',
	'{B9831DEF-A198-48C1-8023-F5F05E55B092}' : u'DerivedParameterTable',
	'{917CE8E7-741A-48A3-8E15-89A6DA053C40}' : u'ColorScheme',
	'{C18888BF-ACD9-481C-BE9C-F8921846BE2D}' : u'TextBoxProxy',
	'{BABF5BB7-9878-11D4-8DE2-0010B541CAA8}' : u'PartEvents',
	'{3CBE8A9F-3D92-11D5-8DEE-0010B541CAA8}' : u'WorkPlaneProxy',
	'{8006A072-ECC4-11D4-8DE9-0010B541CAA8}' : u'GeometricConstraints',
	'{BABF5BBF-9878-11D4-8DE2-0010B541CAA8}' : u'AssemblyEventsSink',
	'{8006A074-ECC4-11D4-8DE9-0010B541CAA8}' : u'CoincidentConstraint',
	'{3CBE8AA7-3D92-11D5-8DEE-0010B541CAA8}' : u'WorkPointProxy',
	'{8006A076-ECC4-11D4-8DE9-0010B541CAA8}' : u'CollinearConstraint',
	'{BABF5BC3-9878-11D4-8DE2-0010B541CAA8}' : u'AssemblyEvents',
	'{8006A078-ECC4-11D4-8DE9-0010B541CAA8}' : u'ConcentricConstraint',
	'{FA561B14-D9E1-4ABD-B6E6-CC8A6A88B268}' : u'DrawingEventsSink',
	'{8006A07A-ECC4-11D4-8DE9-0010B541CAA8}' : u'SplineFitPointConstraint',
	'{3CBE8AAD-3D92-11D5-8DEE-0010B541CAA8}' : u'TransitionalConstraint',
	'{8006A07C-ECC4-11D4-8DE9-0010B541CAA8}' : u'OffsetConstraint',
	'{8006A07E-ECC4-11D4-8DE9-0010B541CAA8}' : u'EqualLengthConstraint',
	'{8006A080-ECC4-11D4-8DE9-0010B541CAA8}' : u'EqualRadiusConstraint',
	'{8006A082-ECC4-11D4-8DE9-0010B541CAA8}' : u'GroundConstraint',
	'{8006A084-ECC4-11D4-8DE9-0010B541CAA8}' : u'HorizontalConstraint',
	'{8006A086-ECC4-11D4-8DE9-0010B541CAA8}' : u'HorizontalAlignConstraint',
	'{8006A088-ECC4-11D4-8DE9-0010B541CAA8}' : u'MidpointConstraint',
	'{8006A08A-ECC4-11D4-8DE9-0010B541CAA8}' : u'ParallelConstraint',
	'{5987714B-D55A-4AED-8AE5-97C062EC1F68}' : u'WorkSurfaces',
	'{8006A08C-ECC4-11D4-8DE9-0010B541CAA8}' : u'PerpendicularConstraint',
	'{8006A08E-ECC4-11D4-8DE9-0010B541CAA8}' : u'SymmetryConstraint',
	'{8006A090-ECC4-11D4-8DE9-0010B541CAA8}' : u'TangentSketchConstraint',
	'{8006A092-ECC4-11D4-8DE9-0010B541CAA8}' : u'VerticalConstraint',
	'{8006A094-ECC4-11D4-8DE9-0010B541CAA8}' : u'VerticalAlignConstraint',
	'{79B234B7-D73B-43B2-91BC-75A419703C12}' : u'DerivedPartDefinition',
	'{32958A3F-CEA1-4390-946D-3D2F2E92675B}' : u'DockableWindowsEventsObject',
	'{4B5F98A9-D670-4DDF-A7CE-8AFCEE0990CA}' : u'UnitAttributes',
	'{5250C13F-196F-442E-86E8-68C87B75CABE}' : u'ParameterTable',
	'{51182028-01DC-4629-AD22-8BFF0D74FA1A}' : u'DerivedAliasComponentProxy',
	'{F2780C41-65D5-43E1-A259-E05D08ED1659}' : u'DisplaySettings',
	'{46785C3B-7F4A-11D4-8DDB-0010B541CAA8}' : u'WorkPlanes',
	'{46785C3D-7F4A-11D4-8DDB-0010B541CAA8}' : u'WorkPlane',
	'{A5AFB9DC-4066-4800-A459-E4A7E4E433B6}' : u'Style',
	'{46785C3F-7F4A-11D4-8DDB-0010B541CAA8}' : u'ThreePointsWorkPlaneDef',
	'{6307798C-50E3-4E9E-B502-038DA82B7C74}' : u'EdgeUseDefinition',
	'{46785C41-7F4A-11D4-8DDB-0010B541CAA8}' : u'TwoLinesWorkPlaneDef',
	'{46785C43-7F4A-11D4-8DDB-0010B541CAA8}' : u'LineAndPointWorkPlaneDef',
	'{46785C45-7F4A-11D4-8DDB-0010B541CAA8}' : u'LinePlaneAndAngleWorkPlaneDef',
	'{6359FE67-0814-4847-9F33-72E0BB9EB688}' : u'SketchFixedSplines',
	'{46785C4B-7F4A-11D4-8DDB-0010B541CAA8}' : u'PlaneAndPointWorkPlaneDef',
	'{AE2CB260-129A-494C-9F8C-AD8140271E8A}' : u'CommandCategories',
	'{12BF1F8A-5679-468F-A820-DA5532624CEA}' : u'MirrorFeature',
	'{228EA2B9-974A-48DF-8E17-7EAE50A79AFD}' : u'RadialMarkingMenus',
	'{5E46D694-BC48-4071-9B6A-8A7F6DDBB685}' : u'CustomConstraint3DProxy',
	'{7BCA4B05-379A-4960-BE68-236689EDAEF1}' : u'TrimFeatureProxy',
	'{3E1A7894-35A3-41C3-9AF9-1E501AD1D747}' : u'LibraryFolders',
	'{6C65399A-B4E9-42DB-8659-6E13E4B07050}' : u'PartsListStyle',
	'{1DF75C0E-591B-45B3-8233-37924B5019DB}' : u'SheetFormat',
	'{3614BB38-60E8-42E0-84E1-A0045BFB25D4}' : u'ModelLeaderNoteDefinition',
	'{9A19AF07-A6BF-43AA-ABF3-870CA1CF329F}' : u'HardwareOptions',
	'{D99ADCF5-8187-4381-979E-499E017C7C0C}' : u'BrowserPane',
	'{E493FF48-3A9A-4A71-9C0D-27D79B3138C2}' : u'DrawingSettings',
	'{77B88412-A66B-43BE-BEE2-06CFE38B0C70}' : u'Tolerance',
	'{B01CC9E0-93E8-4482-9321-D8F52A7AB213}' : u'iPartTableRows',
	'{2A1047EF-0B48-413B-92FD-6CA45A488DA6}' : u'Polyline2d',
	'{F575FA3E-1825-4671-A825-FD1F09E1EC96}' : u'ChangeProcessor',
	'{C13EA1C0-2DD0-4B64-9938-0E4804316912}' : u'ExpressionList',
	'{22324A8F-65DF-48BC-84CD-8A3B457B6A6E}' : u'SmoothConstraintProxy',
	'{B6B5DC40-96E3-11D2-B774-0060B0F159EF}' : u'_Application',
	'{DB93184E-4A45-4C38-96B4-42051502413D}' : u'ApplicationUtilities',
	'{851B66FA-B31A-453D-8628-2DE2A5768C59}' : u'DocumentEventsSink',
	'{C9EBE756-798A-4E78-8CC4-DA91D7737321}' : u'Polyline3d',
	'{19B7AC3A-9E5C-424E-AE7D-33B805717AF5}' : u'DWGPointsEnumerator',
	'{532E5229-0B80-4B9B-968F-69BC150C59CC}' : u'HemDefinition',
	'{9C8B2909-8C33-481E-8CF5-9C269B4E54DC}' : u'ClientNodeResources',
	'{D8AF1BF3-67C1-4EB2-8DA0-6E7625B5291E}' : u'ContentCenterEvents',
	'{9ACB775D-8E1E-4A38-9121-7E1467526860}' : u'ChangeDefinitions',
	'{A3788117-9A81-4D70-A8C8-C3FF3895E3D2}' : u'OrdinateDimensionsEnumerator',
	'{BB41DDFD-351A-4AC7-9294-0FF1D2710C07}' : u'FaceShellDefinition',
	'{BC465119-C96D-4E6C-B5FE-AE114280B6A0}' : u'SnapFitFeature',
	'{46A4AA12-70D3-4BEC-B059-D285F084B979}' : u'SheetMetalStyle',
	'{D480B516-E785-4CEE-B43C-FD4E3B6055F4}' : u'RenderStyle',
	'{395CFC80-16C4-4289-A9F3-06E09E329D95}' : u'GeneralNotes',
	'{02F3D9FA-F750-4C1B-8A2E-A2C5BB99C76C}' : u'AnnotationPlanes',
	'{33A71A9E-0E21-4B70-A688-604C897D3A5A}' : u'DrawingNote',
	'{9A104FEF-2749-4112-AA6D-937CB4F44420}' : u'WorkSurfaceProxy',
	'{E41AB38F-1708-4CAB-AA12-A29E5B3CE6FA}' : u'HoleTableRow',
	'{E15EF363-30C7-420B-91DE-B76BE5F6007F}' : u'FreeformFeatures',
	'{16DC54D8-5357-4ECC-9EB5-E4BDD7DB287C}' : u'BossFeature',
	'{2C167867-83FF-11D4-8DDB-0010B541CAA8}' : u'PlaneAndOffsetWorkPlaneDef',
	'{2C167869-83FF-11D4-8DDB-0010B541CAA8}' : u'LineAndTangentWorkPlaneDef',
	'{2C16786B-83FF-11D4-8DDB-0010B541CAA8}' : u'PlaneAndTangentWorkPlaneDef',
	'{2C16786F-83FF-11D4-8DDB-0010B541CAA8}' : u'FixedWorkPlaneDef',
	'{268D663B-4B37-11D6-8E06-0010B541CAA8}' : u'WeldsComponentDefinition',
	'{5BAB1E1A-F66B-4021-A008-A16E939CA863}' : u'ChangeProcessorSink',
	'{2C16787B-83FF-11D4-8DDB-0010B541CAA8}' : u'ViewsEnumerator',
	'{6299A1B5-4F87-4209-B024-B002D3438E61}' : u'MiniToolbarSliderObject',
	'{2C16787F-83FF-11D4-8DDB-0010B541CAA8}' : u'PlanarSketch',
	'{17FD3E5D-FF18-4E1C-AE86-C9A5A295B2BE}' : u'RectangularOccurrencePatternProxy',
	'{0420658E-CCD1-4100-BFA1-AD78AA655551}' : u'LanguageTools',
	'{176AA199-DDEA-4CA9-B7EC-0437918DF800}' : u'BalloonTips',
	'{4A355C86-508E-4A45-80C3-001139E9FD81}' : u'ExtendFeatures',
	'{7F1F13A7-39BD-4720-AB79-E17BC3922427}' : u'PitchAndHeightCoilExtent',
	'{665564D4-83B4-4B86-A365-CAA6B0EBA6C2}' : u'CombineFeatureProxy',
	'{B1F0562A-BC71-44E3-89B6-5583BB50CD09}' : u'TableParameter',
	'{D23F0671-F983-4D09-8E5A-2BAB64BFB549}' : u'PunchNote',
	'{505BB0CA-670E-4D54-AB26-F66A64DBB72C}' : u'AssetsEnumerator',
	'{F2948971-943D-4CBB-88B0-20E0B48B8573}' : u'ModelFeatureControlFrame',
	'{6BA435D7-BBD6-11D4-8DE6-0010B541CAA8}' : u'TransientObjects',
	'{6BA435D9-BBD6-11D4-8DE6-0010B541CAA8}' : u'TranslationContext',
	'{D88ABC2A-BA2E-4E03-AABE-E052F004A177}' : u'TestResult',
	'{6BA435DB-BBD6-11D4-8DE6-0010B541CAA8}' : u'DataMedium',
	'{321398AC-E78C-43DF-B1A6-5BE90C133680}' : u'BalloonTipSink',
	'{CEF827E8-5A0A-452D-83BB-1A88815C1601}' : u'NotebookOptions',
	'{FBC2D851-EC7F-4D70-B13C-98B57B785E97}' : u'InventorVBAMember',
	'{F369E470-65BE-4BB7-B3E8-AB32C9F6CC22}' : u'PathAndSectionTwistsSweepDef',
	'{148406BE-AC67-4E05-B5E9-A427269D3A28}' : u'RuledSurfaceDefinition',
	'{5B94A1C2-5FA9-4093-87DD-11B7115B9F02}' : u'OccurrencePatternElementProxy',
	'{C343ED7B-A129-11D3-B799-0060B0F159EF}' : u'Command',
	'{E3B2EB5A-FE46-4DA6-8DDD-6135E2120CB2}' : u'BSplineCurve2dDefinition',
	'{CBC02A91-4346-4459-8A47-C845B0A4051F}' : u'RevisionTableColumns',
	'{C343ED82-A129-11D3-B799-0060B0F159EF}' : u'ApprenticeServer',
	'{C343ED83-A129-11D3-B799-0060B0F159EF}' : u'ApprenticeServerDocument',
	'{C343ED84-A129-11D3-B799-0060B0F159EF}' : u'ApprenticeServerComponent',
	'{AF6AFE3F-4249-410E-A4F8-9399EE807D30}' : u'TextureMap',
	'{246ADF11-4A5F-43AF-ADDE-440B0532ED2F}' : u'PointAndPlaneDistanceDimConstraint3DProxy',
	'{131DB1C8-39A0-41F6-B881-9B49050D08DC}' : u'DesignProjects',
	'{312EFE2A-648A-4715-85F4-B7A1EF02CCB9}' : u'AngleExtent',
	'{334FE9E9-7C63-4924-8ADC-42DB57B7B688}' : u'MiniToolbarValueEditorSink',
	'{A783590A-7480-4A9E-BDA3-D805C2CD7281}' : u'RuleFilletFeature',
	'{6047CD23-889D-458D-9AFF-3CD3EB248BAA}' : u'ASideDefinitions',
	'{94ABF5D8-E979-494E-84D3-883672074BD4}' : u'FilletFeatures',
	'{21F02BD0-F849-49E1-A1EC-A04A8F49AE05}' : u'BrowserPaneObject',
	'{528C9A32-4173-420A-AD05-B6FBF8382212}' : u'Parameters',
	'{5475DDC1-3397-46D6-A7A3-E1C34FA5BD7E}' : u'FlangeFeature',
	'{3913A482-D11A-4B13-A6B1-C1310F935B09}' : u'DirectEditRotateOperation',
	'{40E01FF0-E437-4C55-83A4-8E3FA8B19225}' : u'VertexDefinition',
	'{25C0112A-8E78-45F9-A50F-3C4E14AB60E2}' : u'TangentConstraintProxy',
	'{EBDAEE90-2DE0-42E5-8AA0-823A643DB4B3}' : u'GraphicsPrimitive',
	'{069D986F-6DED-4D48-900F-B53674E46499}' : u'ContentCenterEventsObject',
	'{32E4A319-C5E8-11D2-B77F-0060B0F159EF}' : u'FileAccessEvents',
	'{32E4A31B-C5E8-11D2-B77F-0060B0F159EF}' : u'GenericObject',
	'{36B9F8B4-FD23-4AC9-A41F-4778F124C0B7}' : u'SketchBlockProxy',
	'{1C7C9D34-E0E8-40D6-BA67-820B97B4C966}' : u'BalloonTip',
	'{9A9B007B-18C5-4C27-BBA5-1D8F7E9B9A30}' : u'EdgeLoopDefinitions',
	'{48F6DB32-6623-4944-BBF1-12A26E47107A}' : u'LeaderNode',
	'{852C83B9-26EC-4FDA-89D5-E031523AEE01}' : u'FeatureControlFrameStylesEnumerator',
	'{16B36EBE-2DFA-4474-B11B-DF3D57C109B0}' : u'BoundaryPatchFeature',
	'{C3CB1896-B26C-4862-8652-5208013D95A7}' : u'SketchEllipticalArc3D',
	'{42E1EF4D-7D8F-49EA-95A4-B4661D4983AA}' : u'UserCoordinateSystemSettings',
	'{1CE97D79-6535-4D0F-9A51-57734766BEDC}' : u'RibbonTabs',
	'{98588913-EE07-4969-8939-3DFDEE09180E}' : u'TrimFeature',
	'{B32BC09F-4DC6-4655-A457-8B7E8934CAAA}' : u'CommandControlsEnumerator',
	'{0FCBB605-3830-4C3F-95F6-76A4CB15F659}' : u'SketchImageProxy',
	'{34295D6D-002B-40DC-B1E9-E0D658532EF0}' : u'iFeatureTableColumn',
	'{C14E0C19-443E-41D2-95B5-B46AB974CF0D}' : u'LoftedFlangeFeatures',
	'{DB2B25D3-66F3-47CC-9DBF-D6B7468EE76E}' : u'RevisionTables',
	'{75445952-FFF4-405D-B057-E2EFD1B882BC}' : u'PathProxy',
	'{72DDFCC0-DEBA-46D6-AA95-3B4B91E957F6}' : u'SketchEquationCurve3DProxy',
	'{E4C09561-E779-4A00-A835-E8D43E08A290}' : u'Sketch3D',
	'{DF1920AB-6CC5-4C6A-AA29-F4D3B0A30BA6}' : u'ImportedDWGComponent',
	'{F22EBF2F-9F55-45FD-96DB-AABFBD40C177}' : u'MiniToolbarListItem',
	'{C2FEB1BC-115B-443B-A18C-F88B2FCBB7BA}' : u'PanelBarObject',
	'{928894AE-2111-43EB-B77C-4E1A7388CD75}' : u'iMateDefinition',
	'{A12C6DFA-6381-41A2-9037-13AFE5B1EFBD}' : u'GroundPlaneSettings',
	'{600E3CEE-1600-4999-ACE4-7CED6483BECE}' : u'FaceFeature',
	'{2B4C4468-F71B-44EE-BAC6-C68CD4F8DDA1}' : u'CategoryManager',
	'{DD22F707-6FC9-481B-A3FD-44FDA2D695A2}' : u'PositionalRepresentation',
	'{39E63B3F-3A40-4735-9C8F-012AFB75F087}' : u'HelpEventsSink',
	'{F329734C-AAC4-40B9-A1A0-A051679C1EC7}' : u'SurfaceTextureStyle',
	'{EF8803D3-9ADF-4B81-9097-6529ED782861}' : u'SheetSettings',
	'{740E1B50-7EC5-4C4E-B94B-CCEB4FB5C489}' : u'AnnotationPlaneDefinition',
	'{790B4EB3-7947-4D08-9510-372E93A24CF1}' : u'AttributeSets',
	'{A86A47DC-AAFE-4565-9E26-CBEEB2C1C8E5}' : u'SketchedSymbolDefinitionLibraries',
	'{FAD47DA5-3A14-4A2C-9A70-7BCDD992D8A7}' : u'NativeBrowserNodeDefinitionObject',
	'{711F30CD-A00B-4015-93A8-397EC8F5A284}' : u'UserInputEventsSink',
	'{9BAC756F-6695-4C8B-A25C-16D29002F114}' : u'LeaderStylesEnumerator',
	'{C7131135-82E7-45EA-BB86-15DA083F6A04}' : u'AutoCADBlockDefinition',
	'{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}' : u'LoftFeature',
	'{F302D8D2-7DF4-4AD2-9933-9037EB507A90}' : u'iFeatureVectorInput',
	'{5ABB74D4-90C9-490E-A58F-A2FE0986AFBC}' : u'OutOfProcessInventorServerObject',
	'{CEFDC141-B989-4BF3-BDD7-8308D8089FFE}' : u'MateConstraint',
	'{0FEC3515-6F9A-4BFB-BD87-7070E60B0010}' : u'DWGSplinesEnumerator',
	'{7A458570-4422-40E6-B40E-008C2183AF1C}' : u'DWGEntityProxy',
	'{09E02BBB-8953-4E69-8686-B0AADCFF8D02}' : u'EnvironmentBase',
	'{E34C07F3-B8FF-4181-ADC4-DEE3D6550961}' : u'PointCloudRegion',
	'{81710E0C-B8F1-4D04-BDDF-AC92C274CC81}' : u'DisabledCommandList',
	'{FD1878BB-56AD-44CD-9186-11BC84E584A4}' : u'SketchEntity3D',
	'{04B1FC27-4477-491B-A640-3C313E9AC402}' : u'BalloonStyle',
	'{61899B80-0F4D-49F5-A3FF-E727155139FD}' : u'MoveDefinition',
	'{BB075EDC-49B3-4F03-8737-5E20737B1AEB}' : u'AnalysisManager',
	'{2BF92C40-9E07-4F12-B6A3-C5DAA12D3A61}' : u'ContentQueryObject',
	'{A7EA6C3E-D3A4-48BB-B600-E8D1097B9A55}' : u'LoftedFlangeFeature',
	'{6947535C-49CA-43FC-8B6D-95ACFE104275}' : u'EnvironmentBaseHandler',
	'{7D3BDDB1-82EF-4AF6-80C2-96BED3462559}' : u'SketchControlPointSpline3DProxy',
	'{36DB2A89-F970-4C03-AA8A-7864122D553B}' : u'DocumentInterest',
	'{8CBEA17E-7987-4C21-B3AA-429602F6BAA8}' : u'FileDialogEvents',
	'{07F8CD55-9194-4CDB-8403-6BFC4F99D1EE}' : u'BOMQuantity',
	'{6ABB8219-4962-11D5-8DEE-0010B541CAA8}' : u'OccurrencePatternElement',
	'{D5F8CF99-AF1F-4089-A638-F6889762C1D6}' : u'SketchControlPointSpline',
	'{6ABB821F-4962-11D5-8DEE-0010B541CAA8}' : u'EllipseRadiusDimConstraint',
	'{8A11BC6C-E0A4-4954-851A-A5E43144046C}' : u'MoveAlongRayMoveOperation',
	'{C71B52F5-89E4-486C-B80E-8AC74650EB34}' : u'ChamferNote',
	'{CB5F8603-7F21-4B44-A5C1-CD471AB5EA08}' : u'MoldSplitResult',
	'{BF000E43-1F0C-464A-A9F3-E1C5EEBA433E}' : u'PathAndGuideRailSweepDef',
	'{5EE74326-54FB-4C26-97AD-B78830B6E0C0}' : u'DWGEllipticalArcProxy',
	'{E232F1FF-D6C3-421F-B650-AFAC768279D5}' : u'HoleTableCell',
	'{2C292AFE-8044-4E68-AB51-56340FBF0231}' : u'ToHeightExtent',
	'{1EBEC999-3A4D-4A4C-A35A-3F2E773DD56D}' : u'BrowserPanes',
	'{16EF0082-3213-4E37-AF75-5CB2BF738741}' : u'CommandBarList',
	'{2F9E3271-4E14-4B76-9581-602AED994066}' : u'MiniToolbarSliderSink',
	'{E19AC563-EC57-4E4A-9FE3-35AEB2C6B59A}' : u'GrillFeatureProxy',
	'{DD3E1C70-8EDA-466B-B455-5CCE10BBA910}' : u'SketchEllipticalArc3DProxy',
	'{3BE697C4-0242-46F3-A420-27E86761D1D7}' : u'DecalFeatureProxy',
	'{EE0E6545-A868-4A60-A152-2AF4C5FB44DC}' : u'ShellFeatureProxy',
	'{1753D82F-BEAA-4770-82B9-78FFBF2BEC3D}' : u'RotateRotateConstraintProxy',
	'{27716230-E826-46E8-90FB-923D38D6F6F8}' : u'DrawingEventsObject',
	'{8510D6EA-9A97-4CC9-A2A8-221FFC610AB4}' : u'UserParameter',
	'{DE07F599-C9C0-4843-8EFE-D5083EBEFB1D}' : u'CommandControls',
	'{F2E7C272-A777-41B1-B217-C31B8CFAEF77}' : u'ModelLeader',
	'{F5CC3DD7-BC15-476C-853B-3E63BA66A29B}' : u'DWGArcsEnumerator',
	'{2190DB7B-9EAB-45D5-B9E0-B7FE50E1F50B}' : u'TestInputOutput',
	'{9D2A8D7D-D599-4D54-BDE0-586E5E18880D}' : u'GraphicsIndexSet',
	'{3138A370-A692-42B1-8C91-7981A9A0F12C}' : u'LoftSectionDimension',
	'{AEFCDC34-A275-44DF-8A40-DF4B0BFD215F}' : u'ImportedDWGComponentDefinition',
	'{7289A75E-C37E-468C-904F-B2BADC61F272}' : u'Assets',
	'{D755CFCA-9E02-4A08-AFE8-7178E818C763}' : u'DocumentDescriptor',
	'{907F6639-A091-4B19-B1B4-E677D960934C}' : u'TriangleStripGraphics',
	'{0249C8A3-806D-4A1D-8BC0-4699BE1203AF}' : u'_Document',
	'{7771DA50-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'SimulationManager',
	'{7771DA51-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DynamicSimulations',
	'{7771DA52-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DynamicSimulation',
	'{7771DA53-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DSLoads',
	'{7771DA54-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DSLoad',
	'{7771DA55-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DSLoadDefinition',
	'{7771DA56-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DSValue',
	'{7771DA57-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DSValueGraph',
	'{7771DA58-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DSJoints',
	'{7771DA59-AFDF-4E9A-9055-1CAA9B9CFFE5}' : u'DSSettings',
	'{D4AAD36D-D0D1-4BFC-9C3A-C4718D3D9209}' : u'TextStylesEnumerator',
	'{834BFEF4-D052-4139-93F2-D4F08F3A3121}' : u'SurfaceGraphicsEdge',
	'{D8297E9E-DD8B-4C8D-9271-186CAE8E00C1}' : u'GraphicsNormalSet',
	'{F78F8237-3CAA-467D-AB38-6998DF84B3BE}' : u'DrawingBOMColumns',
	'{A4791D9E-EEA1-4524-8543-174DA9CC42B3}' : u'ProjectOptionsButton',
	'{1907E11C-C275-4008-95FA-9AC7539E1A7C}' : u'SelectionPreferences',
	'{2390C0D0-A03F-4526-B4B1-7FBFC3C9A66E}' : u'ContourFlangeFeature',
	'{58370C0B-5F01-422A-AA66-DC7FD8AAC4CD}' : u'CutFeatureProxy',
	'{70180CA4-8BB6-4D2A-B750-E7A17EF35B99}' : u'SketchEquationCurveProxy',
	'{78B82408-F848-4E5B-A657-67059CC86235}' : u'SurfaceTextureJISDefinition',
	'{3C69FF6F-6ADD-4CF5-8E9B-32CBD2B6BBF7}' : u'iFeatureTemplateDescriptor',
	'{0DC3C610-F23D-44AD-B688-A47CAB5B04CB}' : u'PunchToolFeature',
	'{B4F71C8B-BC8D-47F1-A327-9275F5FB443D}' : u'SilhouetteCurves',
	'{0AD283F9-4020-423B-9C18-A192FEBFA285}' : u'MirrorFeatureProxy',
	'{85C83167-947D-46E2-A802-92D529B48E37}' : u'SketchConstraints3DEnumerator',
	'{E9AFE0F2-46D5-4022-B668-F0AE494C48B1}' : u'DerivedPartCoordinateSystemDef',
	'{16ADC90A-A29D-40A9-93E4-4C858E8C7830}' : u'MiniToolbarCheckBox',
	'{091BB62A-D3D9-4DBE-B8DA-69D51538AC92}' : u'KnitFeatureProxy',
	'{611271CA-48EE-4EBF-9ACD-CCD081142400}' : u'SketchSplines3D',
	'{E58169E1-CCA4-432A-9626-A37ABF5F287E}' : u'RuledSurfaceFeature',
	'{DBADC913-8652-4B4E-B13E-B356CC4E9BEE}' : u'ButtonDefinitionObject',
	'{73919DC1-220E-4EC9-B716-072D6046A3AD}' : u'ParallelConstraint3D',
	'{F2286BBF-D48E-4F85-A613-A48AF46893BC}' : u'InterferenceResults',
	'{48694BB1-0E75-4A39-94E0-C7C133C23305}' : u'DisplayOptions',
	'{0DE9D15F-7E51-4861-BD72-050A86BA17AD}' : u'GeometricConstraint3D',
	'{6E9FA739-9CD7-49D3-85B9-72F260BFBF52}' : u'MidSurfaceThicknesses',
	'{C029F46A-865A-4466-BE55-DF72750C8865}' : u'FileManagerEventsObject',
	'{FFFA6714-4FA1-4191-B746-8F0493DF7C06}' : u'CurveAndEntityWorkPointDef',
	'{FA24DA04-D875-4E23-AD4E-312F5B7EC61A}' : u'FreeformFeatureProxy',
	'{ED254D15-6E11-409A-83A0-BB085F017204}' : u'SnapFitFeatures',
	'{6E45ED1A-92ED-469A-9CE0-79C26C9CB5E5}' : u'PointCloud',
	'{5C5381D9-CB23-4BD1-885F-744E8C90B9BB}' : u'InteractionEvents',
	'{24B7B991-46D9-45F8-82CD-05212ECFC6DD}' : u'FaceCollection',
	'{6486F293-4BCF-42EA-91A3-08C82ADBED52}' : u'CoreCavityDefinition',
	'{2B7A8B03-DD00-4DB8-94F9-9BFF87DB8C06}' : u'iFeatureComponent',
	'{8C80204E-CFE9-43C8-BFAE-4D022F3E2339}' : u'UnfoldFeatures',
	'{933CA2AC-EC02-4BA1-9B5B-AFDEDFF20CBF}' : u'SketchSpline3DProxy',
	'{50325C62-766C-41C2-A97C-8951BD4D0E56}' : u'PointCloudPointProxy',
	'{436A627D-919B-4B92-B242-268F7266D8A1}' : u'RibFeatures',
	'{152C858E-87FE-45AD-867B-80622EF4B8AC}' : u'EmbossFeatureProxy',
	'{0945D4EC-0E81-4062-8AC1-E4DE4BB8CBF9}' : u'Centermarks',
	'{181A614B-8F7D-4E15-BCF9-08ECC5F225E2}' : u'ModelFeatureControlFrameRows',
	'{A4AE6207-A45C-4454-9CF6-867D56403BD1}' : u'SketchedSymbolDefinitionLibrary',
	'{FAF83927-A3E9-4ABC-BBCF-AA1D983010F8}' : u'AnnotationPlane',
	'{407A9D14-6E3A-4F39-9AD6-CDD8873B9FCB}' : u'TwoLineAngleDimConstraint3DProxy',
	'{7DE603B3-DAA7-4364-BC8B-77295B53D1DB}' : u'FilletFeature',
	'{95B2DD02-374C-41C5-998C-7FCF8BDCA452}' : u'iFeatureParameterInput',
	'{24A0170B-C253-4A3C-9639-5DE9818A8F31}' : u'LoftFeatures',
	'{2F5EC0C5-5335-4677-BB14-5621C1140D1B}' : u'EnvironmentManager',
	'{9C7891F4-F438-445A-AD22-8FB29E343231}' : u'AssemblyJoint',
	'{B5461253-09AA-11D5-8DEC-0010B541CAA8}' : u'ProfilePath',
	'{DEB206F5-3467-4860-869E-97479BA38D36}' : u'DerivedAssemblyOccurrences',
	'{189559A8-0C9B-4F77-93E9-8330AAAD7943}' : u'SelectSet',
	'{9C693BB0-7C99-4D06-961E-99936273C492}' : u'DecalFeature',
	'{DB89B455-6C7F-4008-986F-05D5218DA204}' : u'CameraEvents',
	'{18F5F2F4-26CB-49E9-A105-F83638FEFB3E}' : u'DWGLine',
	'{1290504E-696F-4480-8126-04A65C7DA45E}' : u'DrawingBOM',
	'{D23D422B-C248-4EA4-98AF-9E6390C99964}' : u'Environments',
	'{90D115A7-34B8-4E35-9242-8B3FAB10CAB5}' : u'SurfaceTextureDINDefinition',
	'{ABCACDBB-5EAF-4AF5-86A0-FB2DB0502D5D}' : u'BreakOperation',
	'{2CBE5BA6-3501-4389-AF3F-AD114C0DAB5A}' : u'BendPartFeature',
	'{2C30965F-FD0D-4D6E-AC98-797F2F0E2DEB}' : u'CoilFeatures',
	'{F5BB5A51-A89B-425E-A747-23CD25D3C186}' : u'VertexDefinitions',
	'{84385A0E-4B73-48FE-B948-CB83894F2E61}' : u'LinearModelDimensionDefinition',
	'{9F5047CD-939F-4F15-930C-5C77CEB50BAA}' : u'WireDefinition',
	'{FA1ACA84-839B-4F18-97FA-5AA81875B0EB}' : u'DeleteFaceFeatureProxy',
	'{C44DF7B9-A598-407F-AE04-2594D11B9DC7}' : u'CoreCavityFeatures',
	'{93224595-EAF4-4AE2-9604-16A2854AFF4B}' : u'ButtonDefinitionHandlerObject',
	'{C7A68CBD-14FA-11D6-8E01-0010B541CAA8}' : u'SketchLineProxy',
	'{2A922EEA-AE03-4C69-9986-D79D5A5A24DA}' : u'HelpEventsObject',
	'{607CC753-5796-4409-85F4-9EA576EAA417}' : u'LineSegment',
	'{C6C1652F-6D5B-495D-B7E5-F4DEB205BA25}' : u'FilletSetbackVertex',
	'{294E366C-86B9-4CF7-9CF9-10D83787D2A6}' : u'GeneralDimensionsEnumerator',
	'{AFD8E323-2B44-4657-89F2-4C50233D287A}' : u'RepresentationEventsSink',
	'{18757DD9-20E4-4DF9-9585-1AC6D0B941FB}' : u'SurfaceGraphicsFace',
	'{CE45B869-6097-4A49-81B4-0FB7A350079C}' : u'PartEventsObject',
	'{F24F9821-0EE5-4157-A555-45B97DE14D6D}' : u'LevelOfDetailRepresentation',
	'{A50B89A5-B9C9-449C-AD62-813F12D80A5D}' : u'ModelingEventsObject',
	'{4BF433DE-1B2F-4ADE-B71C-0C826CF2CC88}' : u'CommandBarControl',
	'{3AB23287-16A5-4B3B-964B-00C27869CD23}' : u'Ribbon',
	'{D2666468-C11D-42F3-AB1E-6E590C5AA182}' : u'LineStripGraphics',
	'{0E4C2356-1844-43F1-BAFA-45AA948EDAD8}' : u'TableParameters',
	'{2F27448C-CB52-4D34-87AE-6D75E01F5623}' : u'ContentTableCell',
	'{8574FEAB-B050-439E-AC97-9704A217E5A1}' : u'ProgressBar',
	'{C7A68CD1-14FA-11D6-8E01-0010B541CAA8}' : u'CollinearConstraintProxy',
	'{807562AB-40E2-47D3-9FDC-E74E2D1E5724}' : u'ViewList',
	'{B9D982C4-3FFF-4796-AD6D-C6D1F16D7BA9}' : u'ControlDefinitions',
	'{A5F6343C-7FE9-431E-BF12-A7308A57CE91}' : u'Balloon',
	'{D60D7065-70F2-4E41-AE17-17E36EE573DF}' : u'LinearModelDimensions',
	'{AB9D8E26-4BEC-4E22-84B0-B1ECDED332D8}' : u'AssemblyJointDefinition',
	'{ADA699FB-D9E7-4879-A1A3-86D9F2C6F57F}' : u'RectangularPatternFeatures',
	'{F8CA1F67-2904-4C91-88F3-F79683227118}' : u'ExpressionLimits',
	'{B148630A-2ECA-4159-8FF2-77CD1B7A79A5}' : u'MidSurfaceFeatures',
	'{A0481EEA-2031-11D3-B78D-0060B0F159EF}' : u'ApplicationAddIns',
	'{A0481EEB-2031-11D3-B78D-0060B0F159EF}' : u'ApplicationAddIn',
	'{25188AF6-308D-4181-879A-1B1084288928}' : u'NonLinearEdgeWorkPointDef',
	'{58614F83-BD65-4B95-9C8B-92280B06D2F1}' : u'GraphicsNode',
	'{C7A68CDB-14FA-11D6-8E01-0010B541CAA8}' : u'EqualRadiusConstraintProxy',
	'{C7FD7CEA-3C30-4BCF-A6E4-A458D3A0F728}' : u'DirectEditFeatureProxy',
	'{BDC1CFE2-865D-46A5-83C9-8FDAD55EA7F0}' : u'ClientFeatureElementProxy',
	'{EC6AB9BC-0F8E-49E6-B809-09E5962BA707}' : u'Sketches3DEnumerator',
	'{F5CB0108-0E0A-416F-AE41-83FAE56D3D10}' : u'MoveFaceFeatureProxy',
	'{D9E903E5-29EE-4164-8701-2CB853CFEE99}' : u'RotateRotateiMateDefinitionProxy',
	'{E83434B4-B12D-4A6F-A2DC-BFA52D3C5FA7}' : u'InventorVBAMembers',
	'{E0519C23-A426-4FA3-BB30-AC5FBEAD137E}' : u'CommandControl',
	'{DAA25411-1CB8-4FE2-8F10-1E98740E0889}' : u'BendFeatures',
	'{87056D9A-B0B2-4BD0-A6EC-51E9D893A502}' : u'SketchLine3D',
	'{1C0E39F2-15F3-41EA-94C1-62AD59AD25D9}' : u'RigidBodyJoint',
	'{6FF869B7-4D60-4A01-9CCA-9F5F71433014}' : u'RefoldFeature',
	'{CAEB520A-F52E-4F2B-AE02-CE0BF9944814}' : u'DocumentSubTypeHandlerObject',
	'{C7A68CE9-14FA-11D6-8E01-0010B541CAA8}' : u'SymmetryConstraintProxy',
	'{CD3A37C9-E647-41AA-B0D9-4EED2A875789}' : u'ButtonDefinition',
	'{B1DA2E33-F616-41D4-917A-CEB1138058D0}' : u'DocumentInterests',
	'{89B5C2F2-A577-41F7-953A-916CF31BC7D5}' : u'Features',
	'{4A60CB5E-1EE8-4180-A801-194704F3021E}' : u'DesignProjectManager',
	'{64868FC5-AFD9-4602-A5D5-02D93B65BB05}' : u'CornerFeatureProxy',
	'{ED859179-A285-41B4-A736-55215294134D}' : u'TestPrograms',
	'{8BC9C1AA-4238-4112-A5FC-15F3765E5336}' : u'TextureMaps',
	'{D092DF11-377A-47AA-92DA-664BE32DDDD4}' : u'ASideDefinition',
	'{12959B9F-4EF1-4834-83C1-7950F2321878}' : u'ReferenceParameter',
	'{FA169DD0-A365-49D9-9572-F0F23F2B634E}' : u'AnnotationPlaneDefinitionsEnumerator',
	'{247E2AC0-3948-4DD9-88A1-0AC87A794BC7}' : u'MidSurfaceFeature',
	'{9CF770DE-2A15-4069-A057-AB247ACCFAFC}' : u'SectionDrawingView',
	'{86338055-4538-47A0-BD9B-06A8C4BD8D93}' : u'Path',
	'{6C6BEFAC-FECC-47A9-8A4C-68210FE441C3}' : u'ContentCenterEventsSink',
	'{916D7FDB-CFE6-4FB1-8921-694DC9CD2793}' : u'ModelParameter',
	'{F6A6A22F-70E4-418E-BC65-F39947C6D1E7}' : u'DirectEditMoveOperation',
	'{69F95DF7-6F84-4FF8-8060-AB921DF1E4F1}' : u'DirectEditFeatures',
	'{1F878EE1-06B7-4C7F-9339-920BEFCFE63D}' : u'RibFeatureProxy',
	'{3822A30C-5DAB-449B-8AAA-BDA9DEF3FBF5}' : u'CornerRoundFeature',
	'{52909F65-AE2E-4997-B3F5-527FE09BF5BE}' : u'MapPointCurve',
	'{8530B3FF-DBD2-4C75-A6EC-0755B8229AE7}' : u'ApprenticePrintManager',
	'{0B87CDBE-3271-46A7-9C95-259667C9FFCF}' : u'ModelDatumIdentifierDefinition',
	'{E17AC68F-D333-4DF4-BBAD-BDD9B8377C9C}' : u'DistanceChamferDef',
	'{9ACFBDEF-B81B-4B4D-8EA6-8453F1DD6285}' : u'ClientNodeResource',
	'{B9F30FBA-DABE-4327-AAB3-65E2160135C1}' : u'iPartFactory',
	'{6A0A9BAD-53F2-4254-A34E-9262F980B5CE}' : u'EmbossFeature',
	'{899DB1B0-F06A-4856-AADC-561B79C0E1A8}' : u'MiniToolbarValueEditor',
	'{C7A68CF9-14FA-11D6-8E01-0010B541CAA8}' : u'ThreePointAngleDimConstraintProxy',
	'{AD3341ED-F50C-46F3-AB93-601CA37413E6}' : u'PartFeaturesEnumerator',
	'{0E1AE204-AD92-497C-A48C-979715C3A035}' : u'ChamferFeatureProxy',
	'{C7A68CFB-14FA-11D6-8E01-0010B541CAA8}' : u'DiameterDimConstraintProxy',
	'{DE936728-E326-4EE4-A671-9AC25F43868C}' : u'DirectEditOperations',
	'{B25B8DC2-B557-4E6B-81D2-A7D0C2A992F4}' : u'NormalToSurfaceWorkAxisDef',
	'{B4A5B240-ED5B-4F0F-B5C7-A1D21FB85939}' : u'ReferenceKeyEventsObject',
	'{5F08DCB5-FE15-4511-9A2E-A3FB10968F2A}' : u'AssemblyEventsObject',
	'{0AEBFB16-385B-4663-B17C-D07F576F2C70}' : u'InsertConstraint',
	'{E2CF70B0-55E2-49E6-81AC-41FD6A6C3DB2}' : u'PerpendicularConstraint3DProxy',
	'{047BD59F-24A4-40D2-A47E-6FED9726BA88}' : u'DirectEditSizeOperation',
	'{65A5B1BC-9F61-4F5D-A113-66EDC3DAAAC0}' : u'SculptSurface',
	'{8AC1686D-0646-41D5-A28F-05353181AEBA}' : u'ContentCenter',
	'{AD623DC3-5354-483D-99A1-C7ADDB0C06CF}' : u'TextureAssetValue',
	'{DD60CA37-AB7B-491F-AD9E-C9DF3B4B5BBB}' : u'HighlightSets',
	'{010971C0-0359-4820-A5EA-5EB9E6FFDA76}' : u'CombineFeatures',
	'{644AE247-EFBA-49FA-9F55-384CA82DB549}' : u'RevisionTable',
	'{3A62D311-C21A-4DD3-83C0-A23507CA385E}' : u'SketchLines3D',
	'{27AAE3A7-29EC-4C49-9845-97318E4C6905}' : u'LumpDefinition',
	'{E49C9290-6D71-4C14-8B15-3595306A49D6}' : u'DrawingCurvesEnumerator',
	'{8D039683-92D8-4F9E-995C-1FDF01AA16D0}' : u'TrailSegment',
	'{F870DE76-265A-4AD2-BACB-5E0137EF0B3A}' : u'GroundConstraint3DProxy',
	'{9DFB56E1-F6A4-4D2A-99CE-47CBB8A3145D}' : u'RotateTranslateConstraintProxy',
	'{29C4F94E-2656-4727-8510-2B0DAF6FCEFE}' : u'AngularModelDimensions',
	'{3CF51EB9-B426-482F-98B0-8CE17BDCDEED}' : u'Styles',
	'{DF8C6267-186F-4A45-8BD4-2545484B102E}' : u'AssetLibraries',
	'{CA6A960F-9215-4EF3-AFFC-A90D277BEF4F}' : u'BendOptions',
	'{DDC2F383-3824-49E3-837C-7387D4775893}' : u'_AppPerformanceMonitor',
	'{D50258F5-140B-4AE1-BCC7-3CB2438B04E1}' : u'iFeatures',
}
VTablesToClassMap = {}
VTablesToPackageMap = {
	'{5DF86097-6B16-11D3-B794-0060B0F159EF}' : 'IRxPlane',
	'{5DF86098-6B16-11D3-B794-0060B0F159EF}' : 'IRxCylinder',
	'{5DF86099-6B16-11D3-B794-0060B0F159EF}' : 'IRxCone',
	'{5DF8609A-6B16-11D3-B794-0060B0F159EF}' : 'IRxSphere',
	'{5DF8609B-6B16-11D3-B794-0060B0F159EF}' : 'IRxTorus',
	'{5DF8609C-6B16-11D3-B794-0060B0F159EF}' : 'IRxBSplineSurface',
	'{9235396C-0350-11D3-B787-0060B0F159EF}' : 'IRxUserInputEvents',
	'{9D7CECDD-2CF1-11D4-B7A8-0060B0F159EF}' : 'IRxComponentOccurrence',
	'{95105315-340B-4406-AAB1-2039EAA23E7D}' : 'IRxApprenticeServer',
	'{863741CF-1A34-11D5-8DEC-0010B541CAA8}' : 'IRxTranslatorAddInServer2',
	'{CB69F159-558E-11D3-B793-0060B0F159EF}' : 'IRxFacetsOld',
	'{CB69F15A-558E-11D3-B793-0060B0F159EF}' : 'IRxStrokesOld',
	'{CB69F15B-558E-11D3-B793-0060B0F159EF}' : 'IRxMatrix',
	'{CB69F15C-558E-11D3-B793-0060B0F159EF}' : 'IRxMatrix2d',
	'{CB69F15D-558E-11D3-B793-0060B0F159EF}' : 'IRxPoint',
	'{DAEA25A5-513E-41CA-BB8F-8E88B507C52E}' : 'IRxStrokes',
	'{CB69F15F-558E-11D3-B793-0060B0F159EF}' : 'IRxVector',
	'{CB69F160-558E-11D3-B793-0060B0F159EF}' : 'IRxVector2d',
	'{CB69F161-558E-11D3-B793-0060B0F159EF}' : 'IRxUnitVector',
	'{CB69F162-558E-11D3-B793-0060B0F159EF}' : 'IRxUnitVector2d',
	'{CB69F163-558E-11D3-B793-0060B0F159EF}' : 'IRxLine',
	'{CB69F164-558E-11D3-B793-0060B0F159EF}' : 'IRxLine2d',
	'{32E4A318-C5E8-11D2-B77F-0060B0F159EF}' : 'IRxFileAccessEvents',
	'{00C8476D-E79F-11D2-B785-0060B0F159EF}' : 'IRxReferencedFileDescriptor',
	'{00C8476F-E79F-11D2-B785-0060B0F159EF}' : 'IRxEnumReferencedFileDescriptors',
	'{C0E7110B-2136-11D4-8DD0-0010B541CAA8}' : 'IRxFileAndReferencesOld2',
	'{D4606260-75D8-48EA-A3C3-A971E2384118}' : 'IRxFileAndReferences',
	'{FA34A3FE-F063-11D3-B7A2-0060B0F159EF}' : 'IRxEllipticalCylinder',
	'{0000000C-0000-0000-C000-000000000046}' : 'IStream',
	'{70109AA6-63C1-11D2-B78B-0060B0EC020B}' : 'IRxFileUIEvents',
	'{70109AA7-63C1-11D2-B78B-0060B0EC020B}' : 'IRxDocumentEvents',
	'{70109AA8-63C1-11D2-B78B-0060B0EC020B}' : 'IRxApplicationEvents',
	'{97ED8AED-EF9D-11D3-B7A2-0060B0F159EF}' : 'IRxEllipticalCone',
	'{C1B42715-92E9-4278-BD5F-6DCE4B25FEBE}' : 'IRxTransientGeometry',
	'{E3571290-DB40-11D2-B783-0060B0F159EF}' : 'IRxEnumApplicationAddIns',
	'{E3571291-DB40-11D2-B783-0060B0F159EF}' : 'IRxApplicationAddIn',
	'{E3571292-DB40-11D2-B783-0060B0F159EF}' : 'IRxApplicationAddInServer',
	'{E3571297-DB40-11D2-B783-0060B0F159EF}' : 'IRxApplicationAddInSiteOld',
	'{0A5CE3AB-073D-11D4-B7A4-0060B0F159EF}' : 'IRxApprenticeServerOld',
	'{2C9F9B60-8967-11D2-86B1-080009DB6864}' : 'IRxEnumFileAndReferences',
	'{6A2718FD-4CCB-46D8-857A-CB83113FD4B9}' : 'IRxApplicationAddInSite',
	'{5DF8606A-6B16-11D3-B794-0060B0F159EF}' : 'IRxEdgeLoop',
	'{023BEB56-898C-11D2-86B1-080009DB6864}' : 'IRxFileAndReferencesOld',
	'{59D3FA3B-ACE0-11D3-B79A-0060B0F159EF}' : 'IRxEnumComponentDocuments',
	'{5DF8600C-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentDocument',
	'{5DF8600D-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentDefinition',
	'{5DF8600E-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentDefinitionReference',
	'{5DF8600F-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentOccurrenceOld',
	'{5DF86010-6B16-11D3-B794-0060B0F159EF}' : 'IRxGeometryProxy',
	'{5DF86011-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumComponentDefinitions',
	'{5DF86012-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumComponentOccurrences',
	'{5DF86013-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumComponentDefinitionReferences',
	'{5DF86015-6B16-11D3-B794-0060B0F159EF}' : 'IRxGeometricLocate',
	'{2894395B-1E28-4516-8308-6AD0911B83D5}' : 'IRxFacets',
	'{73F35CCB-ED6E-11D2-B785-0060B0F159EF}' : 'IRxPropertySets',
	'{73F35CCD-ED6E-11D2-B785-0060B0F159EF}' : 'IRxPropertySet',
	'{5DF86026-6B16-11D3-B794-0060B0F159EF}' : 'IRxReferenceKey',
	'{73F35CCF-ED6E-11D2-B785-0060B0F159EF}' : 'IRxProperty',
	'{5DF86028-6B16-11D3-B794-0060B0F159EF}' : 'IRxReferenceKeyManager',
	'{5DF8602A-6B16-11D3-B794-0060B0F159EF}' : 'IRxBox',
	'{5DF8602B-6B16-11D3-B794-0060B0F159EF}' : 'IRxBox2d',
	'{5DF8602E-6B16-11D3-B794-0060B0F159EF}' : 'IRxCircle',
	'{5DF8602F-6B16-11D3-B794-0060B0F159EF}' : 'IRxCircle2d',
	'{5DF86030-6B16-11D3-B794-0060B0F159EF}' : 'IRxEllipseFull',
	'{5DF86031-6B16-11D3-B794-0060B0F159EF}' : 'IRxEllipseFull2d',
	'{5DF86032-6B16-11D3-B794-0060B0F159EF}' : 'IRxBSplineCurve',
	'{5DF86033-6B16-11D3-B794-0060B0F159EF}' : 'IRxBSplineCurve2d',
	'{5DF86076-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumVertices',
	'{AE277671-2FDC-11D3-B78F-0060B0F159EF}' : 'IRxTransactionEvents',
	'{5DF8603C-6B16-11D3-B794-0060B0F159EF}' : 'IRxCurveEvaluator',
	'{5DF8603D-6B16-11D3-B794-0060B0F159EF}' : 'IRxCurve2dEvaluator',
	'{00000100-0000-0000-C000-000000000046}' : 'IEnumUnknown',
	'{5DF8606B-6B16-11D3-B794-0060B0F159EF}' : 'IRxEdgeUse',
	'{6ECCBC7B-A50D-11D4-8DE4-0010B541CAA8}' : 'IRxTranslatorAddInServer',
	'{0000010B-0000-0000-C000-000000000046}' : 'IPersistFile',
	'{0000010C-0000-0000-C000-000000000046}' : 'IPersist',
	'{5DF86027-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumReferenceKeys',
	'{5DF86067-6B16-11D3-B794-0060B0F159EF}' : 'IRxSurfaceBody',
	'{5DF86068-6B16-11D3-B794-0060B0F159EF}' : 'IRxFaceShell',
	'{5DF86069-6B16-11D3-B794-0060B0F159EF}' : 'IRxFace',
	'{9CAF9896-33EA-11D3-B78F-0060B0F159EF}' : 'IRxReferencedOLEFileDescriptor',
	'{9CAF9897-33EA-11D3-B78F-0060B0F159EF}' : 'IRxEnumReferencedOLEFileDescriptors',
	'{5DF8606C-6B16-11D3-B794-0060B0F159EF}' : 'IRxEdge',
	'{5DF8606D-6B16-11D3-B794-0060B0F159EF}' : 'IRxVertex',
	'{5DF8606E-6B16-11D3-B794-0060B0F159EF}' : 'IRxSurfaceEvaluator',
	'{5DF8606F-6B16-11D3-B794-0060B0F159EF}' : 'IRxAlternateSurfaceBody',
	'{5DF86070-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumSurfaceBodies',
	'{5DF86071-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumFaceShells',
	'{5DF86072-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumFaces',
	'{5DF86073-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumEdgeLoops',
	'{5DF86074-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumEdgeUses',
	'{5DF86075-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumEdges',
	'{CB69F15E-558E-11D3-B793-0060B0F159EF}' : 'IRxPoint2d',
	'{42C7E0BE-FDCF-11D2-B785-0060B0F159EF}' : 'IRxFileSaveAs',
	'{42C7E0BF-FDCF-11D2-B785-0060B0F159EF}' : 'IRxFileLocations',
	'{0C733A30-2A1C-11CE-ADE5-00AA0044773D}' : 'ISequentialStream',
}


NamesToIIDMap = {
	'Profile3DProxy' : '{75120650-FD69-4DFD-A738-9E5E34F5934B}',
	'LeaderStyle' : '{7E4D60AD-496E-4336-96AA-5A2C6178C836}',
	'MoveAlongRayMoveOperation' : '{8A11BC6C-E0A4-4954-851A-A5E43144046C}',
	'RigidBodyResults' : '{E09DAF1C-7738-4CDB-B26B-5DE6A2B37573}',
	'SketchEntities3DEnumerator' : '{6CBA9E79-C13B-46ED-BB14-6541A63B1A16}',
	'SweepDefinition' : '{938C8A20-C60B-47C8-A9F4-CDAA7CE06095}',
	'ContentCenterDialog' : '{52223C79-EAAC-45CB-B000-35DBB1494A3D}',
	'PathProxy' : '{75445952-FFF4-405D-B057-E2EFD1B882BC}',
	'Sheets' : '{206B59AF-22A6-11D4-B7A8-0060B0F159EF}',
	'SurfaceTextureANSIDefinition' : '{47B53154-8132-47E5-8733-9D9B4268F21C}',
	'WebView' : '{CCEBC8A5-7171-47B6-B9DC-067DAC0C79E7}',
	'CommandBarButton' : '{E538F3DF-5386-4537-ABDB-82C476C4274D}',
	'PointCloudPoint' : '{3485FEA9-8865-44EE-8F03-72F46DAB0634}',
	'BossSet' : '{FB1FDFB0-239C-4040-9B22-7ACACCFFE82E}',
	'TrimFeatures' : '{109C1DF4-2290-44AC-9E90-A108D090B4E9}',
	'BalloonTipSink' : '{321398AC-E78C-43DF-B1A6-5BE90C133680}',
	'IRxCircle2d' : '{5DF8602F-6B16-11D3-B794-0060B0F159EF}',
	'TestResult' : '{D88ABC2A-BA2E-4E03-AABE-E052F004A177}',
	'IRxUserInputEvents' : '{9235396C-0350-11D3-B787-0060B0F159EF}',
	'SketchControlPointSplines' : '{135F0952-BF41-444D-A962-8A7805AB2E78}',
	'PatternConstraintProxy' : '{C7A68CF1-14FA-11D6-8E01-0010B541CAA8}',
	'DrawingBOMCell' : '{2FBF7141-4414-423B-9F95-3C6489DC47B9}',
	'RipFeatureProxy' : '{A77799B5-136D-4FEB-9902-CAEC8E122A24}',
	'SketchPoint3DProxy' : '{9AA5A91E-286C-4F3E-A93D-863BAFD4B80C}',
	'CoincidentConstraint3DProxy' : '{BFA33A07-C4CE-4CAD-89BC-AF2C49FD5029}',
	'SurfaceGraphics' : '{5F24EB5E-169E-47C1-9C3D-401A01F4415B}',
	'DSValueGraph' : '{7771DA57-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'FeatureDimensionProxy' : '{57184DE5-2055-47CD-BC40-0277AD066D70}',
	'FaceShellDefinitions' : '{1B28061F-6494-47D6-B8A4-3F6EF0DF0642}',
	'HighlightSet' : '{545F2567-592E-45DA-A262-77BD7E546F7A}',
	'IRxFileAndReferencesOld' : '{023BEB56-898C-11D2-86B1-080009DB6864}',
	'ContentQuerySink' : '{6F10D9EC-E95C-489C-A398-5B530FD1D820}',
	'LoftedFlangeFeatures' : '{C14E0C19-443E-41D2-95B5-B46AB974CF0D}',
	'FoldFeatureProxy' : '{10FCE1AE-95AF-49F4-99FD-B391C181212F}',
	'PlanarMoveDefinition' : '{501F1ACA-00D4-47CF-A0D1-1F4D1BB1A633}',
	'ThreadFeature' : '{F8957621-7E89-4CB8-AFCA-CE11A556E7A2}',
	'ContourRollFeatures' : '{762B1B03-F049-467E-8BFC-DB28CF0DAD27}',
	'FeatureDimension' : '{6C0C1E47-E731-4ECF-8EDD-EF8CE58E395E}',
	'Profiles' : '{523EF757-245A-11D5-8DEC-0010B541CAA8}',
	'Faces' : '{5DF86092-6B16-11D3-B794-0060B0F159EF}',
	'ProjectPaths' : '{7B4F757F-55D3-4078-9AED-61AD15AC9AD5}',
	'ClientApplication' : '{CAD5C3C6-C42C-4F1A-A6E2-5D8746198027}',
	'ParallelConstraint' : '{8006A08A-ECC4-11D4-8DE9-0010B541CAA8}',
	'ReferencedOLEFileDescriptor' : '{9CAF989F-33EA-11D3-B78F-0060B0F159EF}',
	'FeaturePatternElement' : '{1A60195B-72BF-4714-9392-1212EC6260CB}',
	'SketchEquationCurves' : '{C38DE680-2374-487B-86F8-E3DA8012DE66}',
	'DetailDrawingView' : '{3B39A185-9BED-4494-993C-26762D8A2D5F}',
	'ModelLeaderNodesEnumerator' : '{76A8F762-B6B5-4B18-916C-EC7C17B22618}',
	'ChamferNotes' : '{E521F56F-13D5-4D80-95BA-10CB3B2F5918}',
	'Wire' : '{A267D26D-EA7D-444F-8D54-7316BF10DD96}',
	'EllipseFull2d' : '{49CB4BB8-872A-11D3-8524-0060B0F0B5B7}',
	'CameraEventsSink' : '{839AA92C-F073-4BB6-9657-51061150E17C}',
	'WorkPlane' : '{46785C3D-7F4A-11D4-8DDB-0010B541CAA8}',
	'WorkSurface' : '{D136B45B-7B03-4027-9759-AECD06393300}',
	'iFeatureComponents' : '{62F5FBCA-EC38-48F5-9CA7-1D38FED4D443}',
	'IRxEnumEdgeUses' : '{5DF86074-6B16-11D3-B794-0060B0F159EF}',
	'RibFeature' : '{D65B8777-CF40-4542-9A0F-28F2F6EF0678}',
	'TrimFeature' : '{98588913-EE07-4969-8939-3DFDEE09180E}',
	'FlatPatternOrientations' : '{F98E10EB-6BA5-461D-A3D7-5A90CCE47734}',
	'HorizontalConstraint' : '{8006A084-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchPointProxy' : '{C7A68CBF-14FA-11D6-8E01-0010B541CAA8}',
	'GeneralNotes' : '{395CFC80-16C4-4289-A9F3-06E09E329D95}',
	'ParameterTables' : '{53D15C9C-4920-4B58-8804-8567A94D1643}',
	'TwoPlanesWorkPlaneDef' : '{C0E159EB-2FFE-483E-B4CE-585BEE76E710}',
	'VisibleOccurrenceFinder' : '{B4D0EB63-4D3B-42A6-BE38-855EB5DA68E3}',
	'OccurrencePatternElements' : '{CDF65ADD-9C11-4AB9-8F2E-AB6F83FED7C2}',
	'CustomConstraint3DProxy' : '{5E46D694-BC48-4071-9B6A-8A7F6DDBB685}',
	'HoleThreadNote' : '{C1516EB6-AEA2-412F-B1D0-9C609D152E21}',
	'TitleBlock' : '{A907AEB9-A78F-11D5-8DF8-0010B541CAA8}',
	'EdgeUseDefinitions' : '{ECEA0373-8BE9-4970-A696-C967A9718017}',
	'FileDescriptorsEnumerator' : '{C64DD969-DCB0-4FA9-AD0A-E09744466D61}',
	'BSplineSurface' : '{5DF860A6-6B16-11D3-B794-0060B0F159EF}',
	'OGSSceneNode' : '{BED3CF92-D335-4DC0-BA98-76F2E8A6A963}',
	'TutorialsManager' : '{0169EC1F-0694-4353-B28D-3D74B59402D0}',
	'PointCloudCrops' : '{AADD24A8-0094-41C6-BF61-C79E700AA1E2}',
	'DistanceHeightExtent' : '{3C49109C-CDDD-4D4F-A4F3-A0CA3E9EF7F2}',
	'WireEdgeDefinition' : '{D29F9AF1-3383-40AC-94BA-69057A213AAD}',
	'DynamicSimulation' : '{7771DA52-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'ProjectPath' : '{F8D97A2E-CC4D-49EF-8FFF-F16F2FB13929}',
	'SketchEventsSink' : '{3B71CB69-62FB-40D1-BEF9-3B0C255C8DD4}',
	'FileUIEventsObject' : '{C4F1B40A-B7A7-4F92-A9A4-CF8B1DDDE124}',
	'MoveFeatureProxy' : '{70FCCBEE-EF8F-4917-98E0-B26399EAB6CE}',
	'EqualLengthConstraintProxy' : '{C7A68CD9-14FA-11D6-8E01-0010B541CAA8}',
	'HoleTableStylesEnumerator' : '{1FA42157-89A8-4DA0-A943-888BF014E072}',
	'TestConfiguration' : '{66B08E3B-4411-44C0-9A17-2C818A5BB08F}',
	'MoveFeature' : '{F0AF7CF3-7F4E-4A34-B384-7C98CE2843B2}',
	'ImportedComponents' : '{D2F65CFD-A8D7-44D1-8262-9FD5BCA8FECA}',
	'AssemblyWorkAxisDef' : '{F9885CB4-7B68-45E3-953F-B287BE1C6FAF}',
	'UserInterfaceEventsSink' : '{9BC9A7EC-A0AD-433B-BB3C-9AC30C9030E4}',
	'RevisionTable' : '{644AE247-EFBA-49FA-9F55-384CA82DB549}',
	'ApplicationAddInServer' : '{E3571293-DB40-11D2-B783-0060B0F159EF}',
	'HolePlacementDefinition' : '{8924897F-3F00-4220-BF8A-76CADC5A10DD}',
	'SketchCircle3D' : '{8D562D7A-4F0B-4EC8-8737-47DD28FB7323}',
	'SketchEllipse3D' : '{8F014D19-4B2F-4DD1-9010-FE75815C297C}',
	'TestCase' : '{3588F0A6-950E-402A-BFB1-C0ECB1B2EE44}',
	'MoldSplitResult' : '{CB5F8603-7F21-4B44-A5C1-CD471AB5EA08}',
	'AssetLibrary' : '{BE5F1900-C9E6-49B4-BA3A-1BC7FF49DCD0}',
	'ContourFlangeFeature' : '{2390C0D0-A03F-4526-B4B1-7FBFC3C9A66E}',
	'PlaneAndTangentWorkPlaneDef' : '{2C16786B-83FF-11D4-8DDB-0010B541CAA8}',
	'SurfaceBody' : '{5DF86089-6B16-11D3-B794-0060B0F159EF}',
	'SketchPoints' : '{8006A024-ECC4-11D4-8DE9-0010B541CAA8}',
	'FlatBendResults' : '{1D32B73F-D1F8-4E1C-80B9-590FA6F008B2}',
	'SketchedSymbolDefinitionLibrary' : '{A4AE6207-A45C-4454-9CF6-867D56403BD1}',
	'LumpDefinition' : '{27AAE3A7-29EC-4C49-9845-97318E4C6905}',
	'ApprenticeServerDocument' : '{C343ED83-A129-11D3-B799-0060B0F159EF}',
	'MiniToolbarSink' : '{B6B0211A-D77D-4D79-A529-7D8612C9A7A3}',
	'FlangeFeatureProxy' : '{494427B8-E911-4706-9814-35980AC5621D}',
	'ModelLeaderNotes' : '{B97AC4F4-708A-431E-90BA-AFDCC6623A84}',
	'iFeatureComponent' : '{2B7A8B03-DD00-4DB8-94F9-9BFF87DB8C06}',
	'Sphere' : '{5DF860A5-6B16-11D3-B794-0060B0F159EF}',
	'SketchArc' : '{8006A046-ECC4-11D4-8DE9-0010B541CAA8}',
	'ObjectCollectionByVariant' : '{FD9487E1-57A9-419B-A365-14323D1B1CD9}',
	'RibbonPanels' : '{7693ED6C-807E-443A-A3C0-A63010E5625A}',
	'WorkPoints' : '{28DD48C7-8D70-11D4-8DDE-0010B541CAA8}',
	'RepresentationsManager' : '{B25D15A6-B823-42FF-9ABB-781A3043ECB0}',
	'IRxReferenceKeyManager' : '{5DF86028-6B16-11D3-B794-0060B0F159EF}',
	'ContentTableCell' : '{2F27448C-CB52-4D34-87AE-6D75E01F5623}',
	'AnnotationPlanes' : '{02F3D9FA-F750-4C1B-8A2E-A2C5BB99C76C}',
	'iAssemblyTableRows' : '{CE99120C-2AEC-4916-AB66-C14F780325A7}',
	'WorkSurfaces' : '{5987714B-D55A-4AED-8AE5-97C062EC1F68}',
	'DSLoadDefinition' : '{7771DA55-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'KnitFeature' : '{E408524C-B7A1-4F17-921E-160774F4DE5D}',
	'SplineFitPointsConstraint3DProxy' : '{A5F4CA62-8A29-408E-AC56-0B95E44CE781}',
	'ChangeProcessorObject' : '{62246192-FF8D-4715-997D-09E760061B5C}',
	'AngularGeneralDimension' : '{5D81FF33-0E80-4FC7-A02B-D955952B2EC9}',
	'BSplineCurve' : '{49CB4BB9-872A-11D3-8524-0060B0F0B5B7}',
	'IRxEnumReferenceKeys' : '{5DF86027-6B16-11D3-B794-0060B0F159EF}',
	'Vertices' : '{5DF86096-6B16-11D3-B794-0060B0F159EF}',
	'SelectEventsObject' : '{21F3FEA8-2DF7-47B5-9C4C-33BB28E97D1C}',
	'IRxComponentOccurrence' : '{9D7CECDD-2CF1-11D4-B7A8-0060B0F159EF}',
	'DraftingStandard' : '{206B59B0-22A6-11D4-B7A8-0060B0F159EF}',
	'IRxMatrix' : '{CB69F15B-558E-11D3-B793-0060B0F159EF}',
	'FileOpenOptions' : '{F7EDD327-75BC-4976-A0AE-7696B54D461D}',
	'AutomatedCenterlineSettings' : '{E72E9ED9-8A10-4292-9792-96FA51ECD810}',
	'FreeformFeature' : '{88C36A1E-2212-4E9C-BBDB-3155DC8C06E9}',
	'TextStyle' : '{A907AEC1-A78F-11D5-8DF8-0010B541CAA8}',
	'FileOptions' : '{EB213A42-0727-48F0-9BCF-C55F6CB4CD78}',
	'Styles' : '{3CF51EB9-B426-482F-98B0-8CE17BDCDEED}',
	'BendConstraintProxy' : '{9533BA5C-A32F-45DA-AE06-32EBE35E8CFF}',
	'DerivedPartComponent' : '{6D7C8AC8-722D-46C8-B6D9-F6001F1EDD2D}',
	'ReferenceKeyManager' : '{1405C19D-F8AC-41AD-AAB2-D0923BD45C15}',
	'OffsetDimConstraint' : '{C173A077-012F-11D5-8DEA-0010B541CAA8}',
	'IRxApplicationEvents' : '{70109AA8-63C1-11D2-B78B-0060B0EC020B}',
	'RevolutionAndHeightCoilExtent' : '{F0541886-3BF7-4E4D-8A11-D113578E5110}',
	'BendPartFeatureProxy' : '{D54EA6F2-9FB4-43A3-A0C6-C93AF9991E28}',
	'SketchSplineProxy' : '{C7A68CC3-14FA-11D6-8E01-0010B541CAA8}',
	'PositionalRepresentations' : '{1154D44F-DED2-4457-B862-8631D4D69FC6}',
	'FilletFeatures' : '{94ABF5D8-E979-494E-84D3-883672074BD4}',
	'TorusMidPlaneWorkPlaneDef' : '{662FBA92-6903-4455-9395-207E48749986}',
	'Transaction' : '{AE277674-2FDC-11D3-B78F-0060B0F159EF}',
	'SketchEllipseProxy' : '{C7A68CC5-14FA-11D6-8E01-0010B541CAA8}',
	'IRxTransientGeometry' : '{C1B42715-92E9-4278-BD5F-6DCE4B25FEBE}',
	'CornerOptions' : '{37076B79-AB7A-4E6B-8E9D-8D68D28C272E}',
	'Sketch3D' : '{E4C09561-E779-4A00-A835-E8D43E08A290}',
	'SnapFitFeatures' : '{ED254D15-6E11-409A-83A0-BB085F017204}',
	'GraphicsDataSet' : '{D4BF045D-8DFB-44B5-9FFC-FE6ACADF2B23}',
	'ComboBoxDefinitionObject' : '{91B9E6B9-B526-45A8-A7FD-0D2FFD1D6EF5}',
	'BoundaryPatchFeature' : '{16B36EBE-2DFA-4474-B11B-DF3D57C109B0}',
	'iFeatureTemplateDescriptors' : '{2520A915-6F04-4248-B5A3-05B15E651FD9}',
	'Sketch' : '{5FDB5E25-C96F-11D5-8DF9-0010B541CAA8}',
	'OffsetConstraintProxy' : '{C7A68CD7-14FA-11D6-8E01-0010B541CAA8}',
	'SelectionPreferences' : '{1907E11C-C275-4008-95FA-9AC7539E1A7C}',
	'TableStyle' : '{A957DFC5-7AC5-497F-A7AF-5438FAFAD6B4}',
	'WorkPlaneProxy' : '{3CBE8A9F-3D92-11D5-8DEE-0010B541CAA8}',
	'CoilFeature' : '{B9036BF2-EBE0-4593-92B6-DBCD421C6BDF}',
	'UserParameter' : '{8510D6EA-9A97-4CC9-A2A8-221FFC610AB4}',
	'iFeatureOptions' : '{2B03891E-1B59-4576-8160-C61EA6E6D0DC}',
	'TangentConstraintProxy' : '{25C0112A-8E78-45F9-A50F-3C4E14AB60E2}',
	'IRxCircle' : '{5DF8602E-6B16-11D3-B794-0060B0F159EF}',
	'PartsListRow' : '{A907AE8F-A78F-11D5-8DF8-0010B541CAA8}',
	'Cell' : '{CE3FEA37-5793-4814-B9E4-88C84DC0BEEE}',
	'ModelFeatureControlFrameRows' : '{181A614B-8F7D-4E15-BCF9-08ECC5F225E2}',
	'PointAndTangentWorkPlaneDef' : '{66E2ABF7-3454-41E6-9115-62879698C194}',
	'IRxMatrix2d' : '{CB69F15C-558E-11D3-B793-0060B0F159EF}',
	'SurfaceTextureBSIDefinition' : '{201C8CF3-0801-49F5-B87E-F39CEA7508D7}',
	'PropertySet' : '{73F35CC7-ED6E-11D2-B785-0060B0F159EF}',
	'GroundConstraint3DProxy' : '{F870DE76-265A-4AD2-BACB-5E0137EF0B3A}',
	'IRxPlane' : '{5DF86097-6B16-11D3-B794-0060B0F159EF}',
	'SketchBlock' : '{08A3AC40-A684-4F8B-8033-7D0FE23AFBE3}',
	'iFeatureInputs' : '{AF669E3B-2FC3-4731-96C4-2CC724B98E60}',
	'Sketch3DSettings' : '{1D23FF98-1FB3-434F-847F-452217821819}',
	'InventorVBAArgument' : '{25944748-FC4C-4214-A0AC-627BDF178793}',
	'InterferenceResult' : '{FA452CED-C585-4568-BACD-C3DBFAC85D97}',
	'CosmeticWeld' : '{7338F36B-6CD8-4296-90AE-EFEAC0FED72B}',
	'PathAndGuideRailSweepDef' : '{BF000E43-1F0C-464A-A9F3-E1C5EEBA433E}',
	'CutFeatureProxy' : '{58370C0B-5F01-422A-AA66-DC7FD8AAC4CD}',
	'TestCases' : '{A4555442-8328-402E-BBF5-EDC7D808E522}',
	'Edge' : '{5DF8608E-6B16-11D3-B794-0060B0F159EF}',
	'ExpressionList' : '{C13EA1C0-2DD0-4B64-9938-0E4804316912}',
	'RadiusModelDimensionDefinition' : '{62D66B29-1EA9-48CA-A6C6-6D6FF7785213}',
	'PointToPointRipTypeDef' : '{2E264D50-AF7C-4FDE-96DA-12EBD46CAB9B}',
	'SketchFillRegions' : '{A7993C2A-CFCA-4455-BC79-B15952DBF102}',
	'Features' : '{89B5C2F2-A577-41F7-953A-916CF31BC7D5}',
	'ClientFeatureElementProxy' : '{BDC1CFE2-865D-46A5-83C9-8FDAD55EA7F0}',
	'IRxEdge' : '{5DF8606C-6B16-11D3-B794-0060B0F159EF}',
	'SelectSet' : '{189559A8-0C9B-4F77-93E9-8330AAAD7943}',
	'CornerChamferDefinition' : '{E16AEA74-FC21-4762-85D9-A4B20B06A095}',
	'ModelSurfaceTextureSymbol' : '{E083158B-C56B-4CB0-B637-C56896BDAF1C}',
	'PitchAndRevolutionCoilExtent' : '{83B2573C-3DBB-44C1-B88D-2D12EF0A9EE2}',
	'ArcLengthDimConstraintProxy' : '{F0780498-03E3-471D-A733-92EFAC4FF0EE}',
	'CheckPoint' : '{B0955199-1373-4868-9B86-4ABB2DC2A684}',
	'ContentCenter' : '{8AC1686D-0646-41D5-A28F-05353181AEBA}',
	'TestManager' : '{369933DF-0F63-46AA-919B-17C91F385C9E}',
	'ReferenceParameters' : '{1304BB1D-95AE-4738-80F8-CCCA1ABCFF6B}',
	'DistanceChamferDef' : '{E17AC68F-D333-4DF4-BBAD-BDD9B8377C9C}',
	'TestPrograms' : '{ED859179-A285-41B4-A736-55215294134D}',
	'CosmeticBendFeature' : '{B9694561-1C36-4D14-9930-4B8152E1984F}',
	'SketchImages' : '{64D6BFDF-5B47-48C1-AC74-1BE2C24757B2}',
	'RenderStyles' : '{1F76C4FA-DB71-4D87-8390-1529297ED5A9}',
	'CoreCavityDefinition' : '{6486F293-4BCF-42EA-91A3-08C82ADBED52}',
	'FaceShellProxy' : '{46AEA72E-4302-11D4-B7AB-0060B0F159EF}',
	'FlushConstraint' : '{AC581AF3-E3C8-4011-9140-3B64D555FA05}',
	'DrawingNotes' : '{3A4B5B27-8B78-4584-83B5-6A088C6B87FF}',
	'MiniToolbarControls' : '{79093216-BF48-46A2-9BFA-2D15CCB8BADD}',
	'Centermark' : '{37697A9E-01B1-4581-B52D-B8758FBA364E}',
	'CoreCavityFeatureProxy' : '{71360893-BD99-4D41-96CD-A3BD2AE0DB4D}',
	'ApplicationAddInSite' : '{E3571299-DB40-11D2-B783-0060B0F159EF}',
	'BIMComponentDescription' : '{03B09E04-FA49-40EA-AE2D-FF7972025350}',
	'DockableWindowsEventsSink' : '{863F993F-413C-4965-B391-CE4CF47616DB}',
	'DrawingEventsSink' : '{FA561B14-D9E1-4ABD-B6E6-CC8A6A88B268}',
	'SplitFeatures' : '{209DF795-8088-4158-969C-0CC120E0A2A3}',
	'AngleiMateDefinitionProxy' : '{CFA8AC15-B4C1-4703-A672-DAED79017FF3}',
	'SketchSplineHandleProxy' : '{37D2C08C-F2F6-4D4A-9A53-CEBC0A504DA1}',
	'GraphicsColorMapper' : '{AFA9F4D2-A1D8-42C3-8BFA-994FFAB1BEA4}',
	'InsertConstraintProxy' : '{35C3BC01-5C75-4BDF-B92E-97205EE57219}',
	'ContentTableRows' : '{8BEE2F07-0ACD-4A3C-A5BC-E064C8C0DBA8}',
	'FileDialogEventsSink' : '{BF078925-9AC1-485E-9638-4DE87CABBCB7}',
	'GeometricConstraints' : '{8006A072-ECC4-11D4-8DE9-0010B541CAA8}',
	'IRxFaceShell' : '{5DF86068-6B16-11D3-B794-0060B0F159EF}',
	'WeldmentComponentDefinition' : '{9A750C49-0384-4CD8-B1D9-DAADD3E28657}',
	'FileAccessEventsSink' : '{E51041E7-5DB6-4951-9F76-3ACA9B2E2A66}',
	'MirrorFeatureProxy' : '{0AD283F9-4020-423B-9C18-A192FEBFA285}',
	'SketchSpline3DProxy' : '{933CA2AC-EC02-4BA1-9B5B-AFDEDFF20CBF}',
	'PartFeatureExtent' : '{8B6FA30B-DC7A-4603-8793-445D70FF073E}',
	'SurfaceGraphicsFace' : '{18757DD9-20E4-4DF9-9585-1AC6D0B941FB}',
	'DirectEditOperations' : '{DE936728-E326-4EE4-A671-9AC25F43868C}',
	'ReferencedFileDescriptors' : '{9E0BA9CB-E916-11D2-B785-0060B0F159EF}',
	'ModelHoleThreadNotes' : '{C5BF9314-D319-44A4-BDFF-16142CE92D58}',
	'BIMComponentPropertySets' : '{34ACFD9F-B9B0-4D81-B44C-55AEEAEE16BC}',
	'ViewsEnumerator' : '{2C16787B-83FF-11D4-8DDB-0010B541CAA8}',
	'MateConstraintProxy' : '{531B0D86-9BDA-4992-8D31-C42A8788000B}',
	'ProfilePathProxy' : '{C7A68CCD-14FA-11D6-8E01-0010B541CAA8}',
	'DWGLinesEnumerator' : '{C70B926C-2519-4760-B513-DB4FD170208A}',
	'SurfaceBodyProxy' : '{46AEA729-4302-11D4-B7AB-0060B0F159EF}',
	'ContentCenterDialogEventsSink' : '{26F03E86-7DA4-4789-AACC-DE231C4C35E5}',
	'ClientBrowserNodeDefinitionObject' : '{CABA7470-1B47-492D-A62E-EE7213257C05}',
	'_AppPerformanceMonitor' : '{DDC2F383-3824-49E3-837C-7387D4775893}',
	'FileMetadata' : '{BEE271DA-318F-471D-AF24-296B6F59B392}',
	'OccurrencePatternElementProxy' : '{5B94A1C2-5FA9-4093-87DD-11B7115B9F02}',
	'BoundaryPatchLoops' : '{4CD53A13-201C-402A-A729-EFEB24A1417C}',
	'IRxEnumVertices' : '{5DF86076-6B16-11D3-B794-0060B0F159EF}',
	'SilhouetteCurve' : '{F9CB0F15-28B0-4D98-A658-F906D8B0D965}',
	'PerpendicularConstraintProxy' : '{C7A68CE7-14FA-11D6-8E01-0010B541CAA8}',
	'FamilyManager' : '{BFB40FAA-DEC6-4C84-BBA2-8FD424F3C564}',
	'ConcentricHolePlacementDefinition' : '{71F90E58-8C83-4C68-9B75-2E14F8BF3A23}',
	'DirectEditFeatures' : '{69F95DF7-6F84-4FF8-8060-AB921DF1E4F1}',
	'AttributeSetsEnumerator' : '{1734EB03-2921-11D5-A4C1-00C04F6B9531}',
	'ButtonDefinitionObject' : '{DBADC913-8652-4B4E-B13E-B356CC4E9BEE}',
	'VerticalConstraintProxy' : '{C7A68CED-14FA-11D6-8E01-0010B541CAA8}',
	'CircularPatternFeatures' : '{E2E51C17-C894-45AF-9827-988D38C283C7}',
	'PunchToolFeatures' : '{C08C777F-2E1B-469D-A1A7-E379ED046444}',
	'HeadsUpDisplayOptions' : '{F440685C-03F8-49FF-8B68-79E575AF5A5E}',
	'TestResults' : '{8378680D-EA06-405D-986A-8406E0E874B0}',
	'SketchSpline' : '{8006A048-ECC4-11D4-8DE9-0010B541CAA8}',
	'FilletFeature' : '{7DE603B3-DAA7-4364-BC8B-77295B53D1DB}',
	'FreeformFeatureProxy' : '{FA24DA04-D875-4E23-AD4E-312F5B7EC61A}',
	'OrdinateDimensions' : '{EEB73D62-BB10-4FDA-84B2-B27521C833A1}',
	'BendFeature' : '{BBC883B2-B5E1-44C9-A98F-E7221FC17F3D}',
	'SurfaceTextureDINDefinition' : '{90D115A7-34B8-4E35-9242-8B3FAB10CAB5}',
	'GraphicsColorSet' : '{E54B3528-EB27-4A1A-8403-48A9846C93BB}',
	'StandardThreadInfo' : '{B2CB30BD-4B68-4D6C-8A07-3122FE52E6B9}',
	'Cylinder' : '{5DF860A2-6B16-11D3-B794-0060B0F159EF}',
	'FaceOffsetFeature' : '{31C63BA8-7EB4-4816-A367-F99A12691690}',
	'TextureMap' : '{AF6AFE3F-4249-410E-A4F8-9399EE807D30}',
	'ProfilePath' : '{B5461253-09AA-11D5-8DEC-0010B541CAA8}',
	'IRxApplicationAddInSiteOld' : '{E3571297-DB40-11D2-B783-0060B0F159EF}',
	'DrawingSettings' : '{E493FF48-3A9A-4A71-9C0D-27D79B3138C2}',
	'IntersectionCurveProxy' : '{D2CF1030-CA32-48F6-8865-298BE7E11CCC}',
	'StyleEventsObject' : '{221D9E13-D105-485A-B538-1E3FB7250A71}',
	'ButtonDefinitionHandlerEventsSink' : '{96750E11-92EA-457A-BF5E-6FA15C44B8EE}',
	'IRxFace' : '{5DF86069-6B16-11D3-B794-0060B0F159EF}',
	'SketchBlocks' : '{A9C5B884-2122-4DBB-A94E-EB75ED78A160}',
	'Columns' : '{151E96E1-59DA-4732-B025-4AA7A1C9AF27}',
	'CollinearConstraintProxy' : '{C7A68CD1-14FA-11D6-8E01-0010B541CAA8}',
	'RadiusDimConstraintProxy' : '{C7A68CFD-14FA-11D6-8E01-0010B541CAA8}',
	'ViewList' : '{807562AB-40E2-47D3-9FDC-E74E2D1E5724}',
	'SketchEquationCurve3DProxy' : '{72DDFCC0-DEBA-46D6-AA95-3B4B91E957F6}',
	'IRxTorus' : '{5DF8609B-6B16-11D3-B794-0060B0F159EF}',
	'SnapFitFeature' : '{BC465119-C96D-4E6C-B5FE-AE114280B6A0}',
	'AssemblyJoint' : '{9C7891F4-F438-445A-AD22-8FB29E343231}',
	'ClientFeatureElements' : '{112F95FB-41E9-466C-9ACC-1074F5512831}',
	'AnnotationPlane' : '{FAF83927-A3E9-4ABC-BBCF-AA1D983010F8}',
	'RadiusGeneralDimension' : '{8C1619BB-08F8-458D-B1B9-DEE4B63A3D07}',
	'IRxEnumReferencedOLEFileDescriptors' : '{9CAF9897-33EA-11D3-B78F-0060B0F159EF}',
	'FlatBendResult' : '{F7EC4513-DB91-4D3D-ABB6-699D301F4387}',
	'ConcentricConstraint3DProxy' : '{6B64AAF5-85DF-4FB5-ACAB-717DBBEE7DA4}',
	'ClientView' : '{BCD3EFAF-0FEF-4AC1-8303-2A4BF18E96FC}',
	'FullSweepExtent' : '{9A6F5F04-E0DD-463B-96C3-117B88E7BE25}',
	'LibraryFolder' : '{90602DB0-0BE4-48E2-864E-D853D3542959}',
	'PlanarSketches' : '{A03B2CAF-A5F8-4522-BF79-CF4D497DCF4E}',
	'BooleanAssetValue' : '{4479E5B2-48BF-4760-BA24-0A0CE854DF24}',
	'GeometricConstraint' : '{B5461257-09AA-11D5-8DEC-0010B541CAA8}',
	'UnfoldFeatures' : '{8C80204E-CFE9-43C8-BFAE-4D022F3E2339}',
	'iPartTableColumns' : '{4C9E5B40-4741-4AD9-AACC-47C2BAD5E903}',
	'ImportedGenericComponentDefinition' : '{53196161-A966-4EE7-9080-3F75C7D5876D}',
	'PartsListCell' : '{A907AE91-A78F-11D5-8DF8-0010B541CAA8}',
	'SketchSplineHandle3D' : '{5DBD70FD-AB80-4074-B105-EB28F2CB397A}',
	'EdgeLoop' : '{5DF8608C-6B16-11D3-B794-0060B0F159EF}',
	'CosmeticWelds' : '{4A2D7396-8300-4424-B9B7-EB9A8CA5D89E}',
	'GrillFeatures' : '{6AC23513-A004-4DC5-B77D-6D18BCB5E43E}',
	'DirectEditSizeOperationProxy' : '{3181BFE4-BAD1-4C7A-9107-114093E4238A}',
	'ReferenceFeatureProxy' : '{3D65F35E-2F1A-469E-9E5D-E02437A6E3BA}',
	'ApprenticeServerDocuments' : '{59D3FA3A-ACE0-11D3-B79A-0060B0F159EF}',
	'CutFeature' : '{CB8542A0-1559-4E06-BAAE-EFA0BFEF86A7}',
	'IRxReferencedOLEFileDescriptor' : '{9CAF9896-33EA-11D3-B78F-0060B0F159EF}',
	'OutOfProcessInventorServerObject' : '{5ABB74D4-90C9-490E-A58F-A2FE0986AFBC}',
	'MiniToolbarTextEditorSink' : '{32F5072E-8F1B-4889-898F-A512619D7D74}',
	'ContourFlangeFeatureProxy' : '{159DE5F6-0CF1-48F6-87AA-2865091762D3}',
	'SketchCircle3DProxy' : '{D4B12468-31B2-4885-BE17-B55DE2D561AF}',
	'ChamferFeatureProxy' : '{0E1AE204-AD92-497C-A48C-979715C3A035}',
	'PointGraphics' : '{114E3531-FE3B-4042-A454-372A6B98F26F}',
	'ThreePointsWorkPlaneDef' : '{46785C3F-7F4A-11D4-8DDB-0010B541CAA8}',
	'DocumentEventsSink' : '{851B66FA-B31A-453D-8628-2DE2A5768C59}',
	'RevolveFeatureProxy' : '{FD16E33C-AE0F-4CB3-8E44-9C6F2A9A8FF6}',
	'LipFeature' : '{5404EF69-8B8C-4CCF-BC9B-D9BC8B4F4A2E}',
	'DrawingStandardStylesEnumerator' : '{415A6C89-2B25-4884-B2E3-78BC8CAB9AC2}',
	'IRxCurveEvaluator' : '{5DF8603C-6B16-11D3-B794-0060B0F159EF}',
	'FlatPunchResult' : '{CFC1C004-270D-4C19-BBE5-5D380A2A7D7E}',
	'DWGArc' : '{6D0B30F0-4279-46EC-8D96-EDD140C3EC72}',
	'LoftFeatures' : '{24A0170B-C253-4A3C-9639-5DE9818A8F31}',
	'DWGPoint' : '{CE96A92D-B3F9-4607-9E47-30722770F9AD}',
	'ReplaceFaceFeatures' : '{3CBD2849-0258-4583-9CE0-578A71CB7483}',
	'IRxEnumFaces' : '{5DF86072-6B16-11D3-B794-0060B0F159EF}',
	'GraphicsPrimitive' : '{EBDAEE90-2DE0-42E5-8AA0-823A643DB4B3}',
	'WeldBead' : '{D8DEC5C0-4E92-4D60-B107-6D5FBBA9923A}',
	'TriangleFanGraphics' : '{99CBF031-2FFA-440F-B947-8470CD64E79C}',
	'RigidBodyGroup' : '{611952AC-F765-4950-8863-36C465FA2370}',
	'UnitVector2d' : '{CB69F177-558E-11D3-B793-0060B0F159EF}',
	'DecalFeatures' : '{0218B59B-0CE5-4CA1-9A3B-F7D266C4E75F}',
	'SurfaceTextureSymbolDefinition' : '{70E4E4A0-D090-41AF-8B0A-FFDB9F97B58B}',
	'PartFeaturesEnumerator' : '{AD3341ED-F50C-46F3-AB93-601CA37413E6}',
	'CustomParameterGroups' : '{ADE1D7A7-3CF2-49E7-8476-79677765D850}',
	'DiameterModelDimension' : '{098FDC37-8060-4944-AD0E-B55FEC55CA8C}',
	'RevisionTableRow' : '{FB83111D-DED9-462D-9BC5-95A6933ADF4C}',
	'ShellFeatures' : '{3B4B3DE9-7B05-47A7-975A-2C370BBBF974}',
	'AssetCategories' : '{047360BD-1872-4C10-8538-01518FD7F750}',
	'IRxUnitVector2d' : '{CB69F162-558E-11D3-B793-0060B0F159EF}',
	'ContentFamily' : '{30E22548-6DE0-43B7-A8EE-E379A9C86F7D}',
	'RotateRotateConstraintProxy' : '{1753D82F-BEAA-4770-82B9-78FFBF2BEC3D}',
	'ModelDimensionDefinition' : '{4062D31A-F8CE-4D38-B50A-6D8B1FB50D94}',
	'OrdinateDimensionSet' : '{71BA345E-F3F9-49C9-917C-D7DFC284A07F}',
	'FilenameAssetValue' : '{0FC5FA72-0397-4522-9E58-764385FA9B69}',
	'FeatureControlFrame' : '{F3E768AB-B2BC-42B4-B95F-ED49BE550257}',
	'ModelSurfaceTextureSymbolDefinition' : '{85B493F3-342B-4D54-83A1-4EF9C50378D0}',
	'DraftAnalysis' : '{9C9D6F69-F26B-4311-A688-17C04EC292BE}',
	'FileManager' : '{B00506C6-BEB7-47F6-8B1B-A5CB5DCD09B3}',
	'RunoffSurfaceDefinition' : '{6D78B55D-0148-442F-9EF5-E00611FCD8FF}',
	'FileManagerEventsObject' : '{C029F46A-865A-4466-BE55-DF72750C8865}',
	'DirectEditMoveOperation' : '{F6A6A22F-70E4-418E-BC65-F39947C6D1E7}',
	'SketchPoint3D' : '{2307500B-D075-4F5D-815D-7A1B8E90B20C}',
	'BreakOperations' : '{1880ABD8-B826-4258-A2F1-31B5E5740FA6}',
	'ImportedGenericComponentProxy' : '{B3D5D60A-6CE4-4F7B-A6A6-88A15E433F95}',
	'AssemblyDocument' : '{29F0D465-C114-11D2-B77F-0060B0F159EF}',
	'IRxFileLocations' : '{42C7E0BF-FDCF-11D2-B785-0060B0F159EF}',
	'DirectEditScaleOperation' : '{D3067CC6-4526-4797-B62D-54AF0E415A47}',
	'BossFeatures' : '{A110C93B-A3B5-4717-A697-87EA0126216F}',
	'ApplicationEventsSink' : '{CD4C47ED-C403-4F42-B3BF-0A90F3E89D81}',
	'MirrorFeatures' : '{26C57F9F-A6AC-4FCD-BE7C-DAE2F0940E8E}',
	'CornerRoundFeatures' : '{5908F091-036B-49E5-9685-3228EB2EE3E2}',
	'MoveFaceFeatureProxy' : '{F5CB0108-0E0A-416F-AE41-83FAE56D3D10}',
	'FileLocations' : '{0BF73FD9-1253-11D3-B789-0060B0F159EF}',
	'BossFeature' : '{16DC54D8-5357-4ECC-9EB5-E4BDD7DB287C}',
	'PathEntity' : '{6B9C5A03-557E-477A-A6E4-D2E00FB5B812}',
	'PartDocument' : '{29F0D463-C114-11D2-B77F-0060B0F159EF}',
	'FaceOffsetFeatures' : '{3FD23B6F-222D-485D-A9E8-164C497B17F8}',
	'TransientBRep' : '{2BFE4397-C369-4CEF-90C9-D5C8AE90BC9F}',
	'PathEntityProxy' : '{A19C2D06-4C43-41EC-93EB-AD104ABEE1B9}',
	'BOMViews' : '{12A24FCF-4CBD-403D-9E32-ECE5DC3297E9}',
	'SketchesEnumerator' : '{41E90FED-639B-468D-A09E-30363D40DE7F}',
	'ParameterTable' : '{5250C13F-196F-442E-86E8-68C87B75CABE}',
	'Property' : '{73F35CC9-ED6E-11D2-B785-0060B0F159EF}',
	'SurfaceGraphicsEdge' : '{834BFEF4-D052-4139-93F2-D4F08F3A3121}',
	'BreakOutOperation' : '{5D175430-8A8D-47F7-AABE-50C2E9B65D89}',
	'ChangeDefinitions' : '{9ACB775D-8E1E-4A38-9121-7E1467526860}',
	'RuleFilletFeature' : '{A783590A-7480-4A9E-BDA3-D805C2CD7281}',
	'SketchBlockDefinition' : '{F393AB2C-8A8B-4B69-9F0D-91FFA842A53F}',
	'ReplaceFaceFeature' : '{5D8B9732-07F2-4E90-A4AB-C98FB56944A1}',
	'DistanceExtent' : '{A7D32953-D38C-4EB4-B9D0-79F7275B37C1}',
	'BIMDuctConnectorDefinition' : '{1FE852AA-E1B7-4160-8F8D-302E0B46BC52}',
	'CircularPatternFeatureProxy' : '{1CA68293-D200-42E3-B54E-FEB349B302D3}',
	'AngularModelDimension' : '{1BFD9261-5C05-4BF4-9A9F-F5323F3C8E69}',
	'_VbaImplementationEvents' : '{F8841598-132A-4A18-BE1F-EBDD2067C648}',
	'Environment' : '{4E27C06E-4D6A-4E53-9F84-32A0643623CF}',
	'HoleFeatures' : '{A0DB05CD-57E9-47C9-9D33-E648BB57226A}',
	'IRxBSplineCurve2d' : '{5DF86033-6B16-11D3-B794-0060B0F159EF}',
	'DimensionConstraint3D' : '{460D3833-0485-4B61-8A1A-C9E8008FAFCC}',
	'RadiusDimConstraint3D' : '{90943B1A-D344-4227-8219-D1C6090697BB}',
	'ModelFeatureControlFrameRow' : '{D0F606AE-494C-4810-8280-071F5A56824F}',
	'Sketches3D' : '{07FB0B7F-D08F-473F-8EF0-A5E6B4CBA3BC}',
	'ThreadTableQuery' : '{5A0B6FAA-1405-4AB1-AFE9-786462FADF33}',
	'SketchEllipticalArc' : '{C173A087-012F-11D5-8DEA-0010B541CAA8}',
	'Column' : '{70984603-E322-4AC8-B6DE-2F5A31AF0910}',
	'ComponentDefinitionReferences' : '{5DF86023-6B16-11D3-B794-0060B0F159EF}',
	'ThreadInfo' : '{1470BE5E-D0B2-4177-A484-3528D6B0FC37}',
	'SheetSettings' : '{EF8803D3-9ADF-4B81-9097-6529ED782861}',
	'ControlDefinition' : '{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}',
	'CutFeatures' : '{994CF5C9-F097-43AB-8741-76D5DD3DC2BA}',
	'Application' : '{70109AA0-63C1-11D2-B78B-0060B0EC020B}',
	'SheetMetalStyles' : '{5B9228F3-FB28-487E-9EC2-D948901CA89F}',
	'DSDegreesOfFreedom' : '{055EC024-CD9B-4983-97E2-2EC073939046}',
	'LibrarySketchedSymbolDefinition' : '{3B1375EE-4B13-48AA-8A03-EDFDAEA85651}',
	'IRxPropertySets' : '{73F35CCB-ED6E-11D2-B785-0060B0F159EF}',
	'IntersectionCurve' : '{25FF655F-9C78-4C55-9166-51E299DB6565}',
	'BOMView' : '{5538440B-E168-4C38-B817-56F50B538C96}',
	'EllipseFull' : '{49CB4BB7-872A-11D3-8524-0060B0F0B5B7}',
	'DocumentEventsObject' : '{1F6B29F0-6C04-4D11-8ACE-9D41C2904FCD}',
	'MiniToolbarButtonSink' : '{54D7BD09-6FA0-46F5-B427-F2432560A8C3}',
	'DWGBlockReference' : '{942BDD59-6622-4CF0-BAD6-4F4EAD7A4DCA}',
	'ModelSurfaceTextureSymbols' : '{5FCCBA74-9BA4-49C7-95D3-FC9E7D76EFB3}',
	'DrawingViews' : '{206B59B2-22A6-11D4-B7A8-0060B0F159EF}',
	'ModelAnnotationsEnumerator' : '{8F656C43-9BFD-4BAE-AF23-A21067DDED8E}',
	'TableParameter' : '{B1F0562A-BC71-44E3-89B6-5583BB50CD09}',
	'CommandBarControls' : '{67B1BC45-4518-4DB9-A5D3-C0364374BB80}',
	'ContentCenterEventsObject' : '{069D986F-6DED-4D48-900F-B53674E46499}',
	'ExtrudeFeatureProxy' : '{C75F478E-81C5-4E92-BC2A-630E598E34E5}',
	'FreeformFeatures' : '{E15EF363-30C7-420B-91DE-B76BE5F6007F}',
	'ComponentOccurrence' : '{5DF86020-6B16-11D3-B794-0060B0F159EF}',
	'SurfaceGraphicsVertexList' : '{C11F6667-E5D4-4A7E-8C47-70AA423E7758}',
	'DockableWindow' : '{3A32960B-A64E-4257-B24F-240C7E68C065}',
	'IRxApprenticeServer' : '{95105315-340B-4406-AAB1-2039EAA23E7D}',
	'SnapFitFeatureProxy' : '{B13C95CF-8B79-4F03-8EF0-BE81A400529F}',
	'FaceDraftFeature' : '{EA1D0D38-93AD-48BB-84AC-7707FAC29BAF}',
	'AliasFreeformFeatures' : '{3C007201-8D66-47BD-AD94-2012FF75C4C5}',
	'TangentSketchConstraintProxy' : '{C7A68CEB-14FA-11D6-8E01-0010B541CAA8}',
	'Color' : '{0D084DAB-C766-4595-A449-7625772E88D2}',
	'VirtualComponentDefinition' : '{D4652AC1-D4B9-4D65-8C2B-942D74411B1C}',
	'IRxVertex' : '{5DF8606D-6B16-11D3-B794-0060B0F159EF}',
	'RevisionTableColumn' : '{C802F139-6C51-4A73-ABAE-BF5E88687E00}',
	'PointCloudPointProxy' : '{50325C62-766C-41C2-A97C-8951BD4D0E56}',
	'Centermarks' : '{0945D4EC-0E81-4062-8AC1-E4DE4BB8CBF9}',
	'TwoPointDistanceDimConstraintProxy' : '{C7A68CF5-14FA-11D6-8E01-0010B541CAA8}',
	'DirectEditFeatureProxy' : '{C7FD7CEA-3C30-4BCF-A6E4-A458D3A0F728}',
	'LinearModelDimension' : '{7D6FF00B-9613-4E95-AA2F-484E089AAEA3}',
	'SketchLines3D' : '{3A62D311-C21A-4DD3-83C0-A23507CA385E}',
	'PartsListColumns' : '{A907AE89-A78F-11D5-8DF8-0010B541CAA8}',
	'SplineFitPointsConstraint3D' : '{641D6ED0-4DF1-4FA3-B04D-86107C00A62B}',
	'LineSegment' : '{607CC753-5796-4409-85F4-9EA576EAA417}',
	'DecalFeature' : '{9C693BB0-7C99-4D06-961E-99936273C492}',
	'MidpointConstraintProxy' : '{C7A68CE3-14FA-11D6-8E01-0010B541CAA8}',
	'EnvironmentManager' : '{2F5EC0C5-5335-4677-BB14-5621C1140D1B}',
	'RuledSurfaceDefinition' : '{148406BE-AC67-4E05-B5E9-A427269D3A28}',
	'CoincidentConstraint' : '{8006A074-ECC4-11D4-8DE9-0010B541CAA8}',
	'SplitFeature' : '{78D752FD-9090-4AEA-9CF2-247ABA9D1936}',
	'PerpendicularConstraint' : '{8006A08C-ECC4-11D4-8DE9-0010B541CAA8}',
	'DSJoints' : '{7771DA58-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'RegionProperties' : '{4735D53B-FEF2-4671-9430-3D60964D850B}',
	'TransientGeometry' : '{97ECB3AE-6C6E-4D8A-A91E-564314494EB8}',
	'TwoLineAngleDimConstraint' : '{C173A07B-012F-11D5-8DEA-0010B541CAA8}',
	'ProjectOptionsButtonObject' : '{4F599909-D43A-4090-BC23-3616A075A02D}',
	'AssemblyJointsEnumerator' : '{15AD2867-FEE2-4A5B-9F07-FDC0A4FF5C72}',
	'DWGEntityProxy' : '{7A458570-4422-40E6-B40E-008C2183AF1C}',
	'WeldBeads' : '{F44EE9AE-7D98-49C7-8634-700050114F38}',
	'IRxTranslatorAddInServer' : '{6ECCBC7B-A50D-11D4-8DE4-0010B541CAA8}',
	'CombineFeatures' : '{010971C0-0359-4820-A5EA-5EB9E6FFDA76}',
	'MiniToolbarButtonObject' : '{F6A7B996-5EB9-4DC4-99D9-3919C36FB802}',
	'ApprenticeServerDrawingDocument' : '{4F589652-207C-11D4-B7A5-0060B0F159EF}',
	'ThreadFeatures' : '{D0786DD9-AD8A-431B-B2A9-388211ABD7DD}',
	'IRxCurve2dEvaluator' : '{5DF8603D-6B16-11D3-B794-0060B0F159EF}',
	'DWGSplineProxy' : '{EF97259E-0689-42D1-AFAC-1FFD9F6A1980}',
	'TrimFeatureProxy' : '{7BCA4B05-379A-4960-BE68-236689EDAEF1}',
	'MoveDefinition' : '{61899B80-0F4D-49F5-A3FF-E727155139FD}',
	'DebugInstrumentationSink' : '{F6F3355B-6984-11D5-8DF3-0010B541CAA8}',
	'FoldFeatures' : '{2B564484-AF79-47BF-836B-15F288717791}',
	'ContourFlangeDefinition' : '{8D389B94-12D9-4150-BC67-B64B560E743F}',
	'HoleTables' : '{8C0B72C6-CFC6-4B2D-8A89-1DE890D9F65B}',
	'SketchEllipse' : '{8006A04A-ECC4-11D4-8DE9-0010B541CAA8}',
	'DirectEditRotateOperationProxy' : '{264513E0-16F5-4AE8-A80D-46EE06D2C99B}',
	'CommandControls' : '{DE07F599-C9C0-4843-8EFE-D5083EBEFB1D}',
	'AssemblyComponentDefinitions' : '{575F2831-2B6A-11D4-B7A8-0060B0F159EF}',
	'GeometricConstraint3D' : '{0DE9D15F-7E51-4861-BD72-050A86BA17AD}',
	'DerivedPartUniformScaleDef' : '{F41437F2-9B75-4C35-857C-98646F87B551}',
	'EnvironmentBase' : '{09E02BBB-8953-4E69-8686-B0AADCFF8D02}',
	'MidSurfaceThickness' : '{08389E18-6E84-499B-8F1F-09AC53003178}',
	'PartFeatures' : '{DA33F1A5-7C3F-11D3-B794-0060B0F159EF}',
	'StringAssetValue' : '{9ADC4649-06DC-449E-ABE8-5DCA6F4C7788}',
	'MidpointConstraint3D' : '{4FAB4F91-4998-4B1C-9717-8CDF1BD7377E}',
	'FactoryOptions' : '{1DC369B0-C6C9-42B7-BA0F-5A2AB9CA79AE}',
	'TranslatorAddInServer' : '{6ECCBC7F-A50D-11D4-8DE4-0010B541CAA8}',
	'ColorAssetValue' : '{9D7514D7-EA00-4F2D-8F66-0E395B21C284}',
	'LayoutConstraintProxy' : '{81807A32-C016-4239-8D61-28B44957393D}',
	'Matrix' : '{CB69F171-558E-11D3-B793-0060B0F159EF}',
	'DeleteFaceFeatureProxy' : '{FA1ACA84-839B-4F18-97FA-5AA81875B0EB}',
	'GraphicsNode' : '{58614F83-BD65-4B95-9C8B-92280B06D2F1}',
	'IEnumUnknown' : '{00000100-0000-0000-C000-000000000046}',
	'IntersectionCurves' : '{9F672C49-E28B-4239-8F7B-BF3FA7FD5071}',
	'IRxEnumApplicationAddIns' : '{E3571290-DB40-11D2-B783-0060B0F159EF}',
	'SweepGraphics' : '{1435773B-06FC-46E8-B965-5845697D2A6B}',
	'PointClouds' : '{715899F9-C5E6-4A31-96C7-151D74A852B8}',
	'DerivedAssemblyDefinition' : '{18DED264-417F-4B81-828C-B8806397C7C3}',
	'RadiusDimConstraint' : '{C173A081-012F-11D5-8DEA-0010B541CAA8}',
	'InventorVBAMembers' : '{E83434B4-B12D-4A6F-A2DC-BFA52D3C5FA7}',
	'CoilFeatureProxy' : '{ECD82FDD-5B8F-4515-B3CE-1ED92B94C11F}',
	'DefaultBorder' : '{A907AEE3-A78F-11D5-8DF8-0010B541CAA8}',
	'BrowserPanesEventsObject' : '{EF126FC8-7582-4E15-B5DC-194EEE2CEEDA}',
	'DWGPolyline2D' : '{AD47616F-A657-4363-AB07-360A1A38AD44}',
	'iFeatureWorkPlaneInput' : '{F21B5BBF-DBA8-480A-95A6-83D27D52343B}',
	'ThreePointAngleDimConstraintProxy' : '{C7A68CF9-14FA-11D6-8E01-0010B541CAA8}',
	'iAssemblyTableCell' : '{290EC1FE-2BB5-46E8-AB41-919D7455740D}',
	'UserCoordinateSystemProxy' : '{85577108-087D-4E36-994A-48CA4F1D2AB9}',
	'RectangularPatternFeatureProxy' : '{2A705B9C-82D0-4F14-9137-164642028E77}',
	'CoreCavityFeatures' : '{C44DF7B9-A598-407F-AE04-2594D11B9DC7}',
	'BIMConnectors' : '{7C1BEFD9-4296-4794-B3A2-8025809570D8}',
	'IRxLine' : '{CB69F163-558E-11D3-B793-0060B0F159EF}',
	'PartsListStylesEnumerator' : '{F829B171-412E-4642-8034-AEC013FCFDC5}',
	'InventorVBAArguments' : '{BAB06F80-7165-484C-88DF-7D8A0004A76D}',
	'UserCoordinateSystemDefinition' : '{598714D9-653D-4D2B-B7BB-139C3E9E38B1}',
	'DrawingPrintManager' : '{55C72DAA-3307-43D6-89F0-CBF7DD348E4D}',
	'RibDefinition' : '{5B078EF2-5839-4B6A-97D1-BB8F5D9CFD78}',
	'WorkPlanes' : '{46785C3B-7F4A-11D4-8DDB-0010B541CAA8}',
	'Curve2dEvaluator' : '{5DF860B1-6B16-11D3-B794-0060B0F159EF}',
	'PointAndPlaneDistanceDimConstraint3DProxy' : '{246ADF11-4A5F-43AF-ADDE-440B0532ED2F}',
	'SketchPoint' : '{8006A022-ECC4-11D4-8DE9-0010B541CAA8}',
	'PatternConstraint' : '{C173A073-012F-11D5-8DEA-0010B541CAA8}',
	'StyleEventsSink' : '{A52071CF-BF9F-45BA-A7D5-E5AAA2682B4D}',
	'PartsListStyle' : '{6C65399A-B4E9-42DB-8659-6E13E4B07050}',
	'TwoPointDistanceDimConstraint' : '{C173A079-012F-11D5-8DEA-0010B541CAA8}',
	'WebViews' : '{B894B815-AEF1-4FAA-938A-2131E2E5190F}',
	'FileDescriptor' : '{67CF708B-CA38-419D-8016-19CEAA5FBB7D}',
	'IRxComponentDefinitionReference' : '{5DF8600E-6B16-11D3-B794-0060B0F159EF}',
	'TransactionEventsSink' : '{BA8CE4E1-3FC3-414C-A73A-26BDB38ECE70}',
	'DocumentSubTypeHandlerObject' : '{CAEB520A-F52E-4F2B-AE02-CE0BF9944814}',
	'EllipseRadiusDimConstraintProxy' : '{C7A68CFF-14FA-11D6-8E01-0010B541CAA8}',
	'ObjectsEnumeratorByVariant' : '{9235396B-0350-11D3-B787-0060B0F159EF}',
	'IRxAlternateSurfaceBody' : '{5DF8606F-6B16-11D3-B794-0060B0F159EF}',
	'AngleConstraintProxy' : '{076FFE46-6694-42EE-9F7F-E61F71434845}',
	'VertexDefinitions' : '{F5BB5A51-A89B-425E-A747-23CD25D3C186}',
	'HoleTableRow' : '{E41AB38F-1708-4CAB-AA12-A29E5B3CE6FA}',
	'iAssemblyTableRow' : '{18517A46-ABB7-4285-94B4-35B3277880F1}',
	'_DocPerformanceMonitorObject' : '{AAF23B5F-E2FE-471C-85AA-E37FCE6DE651}',
	'ContentCenterEventsSink' : '{6C6BEFAC-FECC-47A9-8A4C-68210FE441C3}',
	'AttributesEnumerator' : '{1734EB04-2921-11D5-A4C1-00C04F6B9531}',
	'ExtrudeFeature' : '{2FD8A7F5-B548-4E12-9D65-FF47FD063F8C}',
	'RuledSurfaceFeatures' : '{721CC25E-D96C-4E25-BED5-04EF710574B4}',
	'GroundConstraint3D' : '{38876920-588A-4F80-A4B1-1F2E3562FB19}',
	'ParallelConstraint3D' : '{73919DC1-220E-4EC9-B716-072D6046A3AD}',
	'PlaneAndPointWorkPlaneDef' : '{46785C4B-7F4A-11D4-8DDB-0010B541CAA8}',
	'View' : '{70109AA3-63C1-11D2-B78B-0060B0EC020B}',
	'ObjectVisibility' : '{1B73EA84-1B63-4F24-B295-B50EA9215C26}',
	'IRxApplicationAddInSite' : '{6A2718FD-4CCB-46D8-857A-CB83113FD4B9}',
	'CircularOccurrencePatternProxy' : '{E6478D92-2EBD-4363-8C27-A6891E942DBB}',
	'SketchHolePlacementDefinition' : '{2BC16E62-07F5-4106-B5BD-58C7C660DA2C}',
	'FileUIEventsSink' : '{63AD687A-3898-44E2-B857-C9DAD84FC9EC}',
	'AssemblyEventsObject' : '{5F08DCB5-FE15-4511-9A2E-A3FB10968F2A}',
	'GeometryIntent' : '{56B990B9-D25A-436F-A652-1D21EC739C57}',
	'HemFeatureProxy' : '{0F6DEA5E-48E4-49BE-854E-164A89406DDC}',
	'ClientGraphics' : '{2B0F6166-711D-47E0-B9B1-54ED9E3F160B}',
	'Sheet' : '{206B59AE-22A6-11D4-B7A8-0060B0F159EF}',
	'ComponentDefinition' : '{5DF8601E-6B16-11D3-B794-0060B0F159EF}',
	'IRxPropertySet' : '{73F35CCD-ED6E-11D2-B785-0060B0F159EF}',
	'Centerlines' : '{3DC9DC2A-8A78-43BE-BDB5-E6F1162980BB}',
	'SketchOffsetSplineProxy' : '{BF18368A-A9B1-4295-9242-18D1AC91F8D3}',
	'LineAndPointWorkPlaneDef' : '{46785C43-7F4A-11D4-8DDB-0010B541CAA8}',
	'iPartTableCell' : '{901E43F5-403A-45C8-A93C-E9509386BB74}',
	'ContourFlangeFeatures' : '{A7AF22DD-A689-4BEA-84BF-AEE3496BB26E}',
	'TableFormat' : '{A2F174A9-9D82-4AF1-B80C-67FB45B59923}',
	'Views' : '{70109AA4-63C1-11D2-B78B-0060B0EC020B}',
	'ChainDimensionSets' : '{C9D63CDD-B82A-4CD9-82EB-CE937569197E}',
	'ContentQueryObject' : '{2BF92C40-9E07-4F12-B6A3-C5DAA12D3A61}',
	'TransientObjects' : '{6BA435D7-BBD6-11D4-8DE6-0010B541CAA8}',
	'KeyboardEventsSink' : '{AB510BBF-B893-47F7-ACC6-8F22836C5D8C}',
	'DerivedParameterTables' : '{321D3FD9-A57F-4CDE-AD39-FD1EEE22543C}',
	'PunchNote' : '{D23F0671-F983-4D09-8E5A-2BAB64BFB549}',
	'ClientFeatureDefinition' : '{0A1F6F03-BA19-49CD-8376-93A85FB08A2A}',
	'EdgeUseProxy' : '{46AEA72D-4302-11D4-B7AB-0060B0F159EF}',
	'ApplicationAddIn' : '{A0481EEB-2031-11D3-B78D-0060B0F159EF}',
	'DrawingStandardStyle' : '{55DBDB4E-BC61-4D53-84F6-86CF24267DD8}',
	'GraphicsDataSetsCollection' : '{8C2CC3CF-A455-40D6-8505-56A702F6FB77}',
	'DesignViewRepresentation' : '{4E1C27BA-D992-411F-9DE2-BD630285E4B3}',
	'TaperedThreadInfo' : '{D4D0315D-6874-4E69-9BBB-6E3D28B9122A}',
	'InsertiMateDefinitionProxy' : '{1DC001D8-CAAE-4132-A265-4E17E74A9410}',
	'EnvironmentBaseCollection' : '{BC985A7D-4B44-4089-870D-0AEE95D5E86A}',
	'iFeatureEntityInput' : '{84526202-5E30-403F-8700-397646B4BBD0}',
	'DraftAnalyses' : '{5C93A2CD-ECCA-4998-9DC4-D439BD9FE3DB}',
	'HoleTableStyle' : '{97B2D2E2-78EA-4838-B140-2BBAB4D8E7A9}',
	'DerivedPartEntities' : '{90A1D182-6B1E-49C2-9DAF-3A74B31BE6D4}',
	'AssemblyWorkPlaneDef' : '{62F1DC23-FB86-4D0C-81B3-05BF2CD775F4}',
	'ProfilePath3DProxy' : '{EA49DCCB-E7AE-4B7D-BEAC-80F835167854}',
	'EqualLengthConstraint' : '{8006A07E-ECC4-11D4-8DE9-0010B541CAA8}',
	'ModelDimension' : '{C66A1C65-43C3-4F1C-A22C-089F3F03349A}',
	'DWGLineProxy' : '{7EB60BBC-FF1C-428E-BB89-5F69BD727E83}',
	'iFeatureInput' : '{6A89E379-03FC-440E-A655-6111E86247A1}',
	'InventorVBAProject' : '{95C6C576-FC7A-4B16-B565-BFABEF69B013}',
	'TitleBlockDefinition' : '{A907AEB7-A78F-11D5-8DF8-0010B541CAA8}',
	'ProfileEntity3D' : '{142C71BE-1254-4947-9192-382BCC511F46}',
	'Arc2d' : '{C173A091-012F-11D5-8DEA-0010B541CAA8}',
	'SurfaceTextureGOSTDefinition' : '{0B1630B9-41C0-4DCA-BCBC-2E9D0BA096FE}',
	'EdgeDefinition' : '{F8B3014D-CA2D-40F4-B2A3-FA00E23105A1}',
	'UserInterfaceEventsObject' : '{4B01DD28-A1AF-4387-9F24-2B87442C1E94}',
	'ExtendFeatureProxy' : '{F057A860-3896-4C4A-87CB-E634F9BA681B}',
	'DSJoint' : '{055EC022-CD9B-4983-97E2-2EC073939046}',
	'CommandBarBase' : '{582865AB-F113-4939-8796-336EA266F8B2}',
	'DWGPolyline3D' : '{BC6242DB-ABCC-4605-8A0F-9A42F26F9D9C}',
	'LineAndTangentWorkPlaneDef' : '{2C167869-83FF-11D4-8DDB-0010B541CAA8}',
	'LeaderNode' : '{48F6DB32-6623-4944-BBF1-12A26E47107A}',
	'EllipticalArc' : '{C1066E40-4E2F-45C2-A5AB-E2B4D1B84A1E}',
	'EdgeUses' : '{5DF86094-6B16-11D3-B794-0060B0F159EF}',
	'BaselineDimensionSets' : '{F2930064-7C6A-4FF7-8B87-D98EAC520AA1}',
	'DocumentSubTypeHandlerEventsSink' : '{94F1E029-984C-4DDC-9B12-003982C02E06}',
	'BIMComponentProperty' : '{A145B58E-E928-4180-951B-D7E652298E2A}',
	'ReferenceParameter' : '{12959B9F-4EF1-4834-83C1-7950F2321878}',
	'KeyboardEventsObject' : '{BD32F579-5C70-453E-BD6F-41D11EF640FD}',
	'PointCloudProxy' : '{4EDC3AD5-669B-40A9-A3DC-3261C16F4642}',
	'ConcentricConstraint' : '{8006A078-ECC4-11D4-8DE9-0010B541CAA8}',
	'SelectEventsSink' : '{2E19A8EE-1E70-4AE4-8C1E-06DAE3BBABB2}',
	'LibraryFolders' : '{3E1A7894-35A3-41C3-9AF9-1E501AD1D747}',
	'AutoCADBlock' : '{C7A9F576-7180-4DEE-BCC7-8E9DEABECEC4}',
	'IRxSurfaceBody' : '{5DF86067-6B16-11D3-B794-0060B0F159EF}',
	'RadialMarkingMenu' : '{828DB6DB-AE56-4DB4-A765-216D9159A18C}',
	'ContentTableRow' : '{1C310044-05CF-4B79-9829-FE41BD1EB1A6}',
	'SectionDrawingView' : '{9CF770DE-2A15-4069-A057-AB247ACCFAFC}',
	'DiameterModelDimensionDefinition' : '{5FCEA8CE-F9AE-4216-8AAD-2530EC41B619}',
	'PartFeature' : '{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}',
	'RuleFilletFeatures' : '{9B108AAB-237A-460D-BC99-40FAF5EABD65}',
	'DrawingDimensions' : '{FD30DCC9-A6E8-44B1-85B0-D7D8AE1580E5}',
	'IRxEdgeLoop' : '{5DF8606A-6B16-11D3-B794-0060B0F159EF}',
	'FlangeFeatures' : '{F9B17D1C-6918-44FE-B072-7B4F00CD2BB3}',
	'Balloons' : '{3DFE3282-5B67-431A-A890-040098957C1C}',
	'OrdinateDimensionSets' : '{ACC86380-BE3B-48F1-A3D0-91E6ED2E2A82}',
	'ExtrudeDefinition' : '{3098A39F-CCD6-4163-8ADC-2E9504F3E00C}',
	'LeaderNote' : '{04AAEAB9-6EAD-412C-B69A-D8EE4D924798}',
	'SketchBlocksEnumerator' : '{2C9F06C7-9124-43FE-B6D9-703620D53DA7}',
	'SheetMetalComponentDefinition' : '{0562B816-F05F-4293-AF39-D2F640E42740}',
	'FaceFeatureDefinition' : '{67BD386A-CC79-48F0-BCFF-6C25FFBF59AA}',
	'ParametersEnumerator' : '{C52EE54D-B18E-4CB3-AEE3-7D0375F92948}',
	'MiniToolbarSliderObject' : '{6299A1B5-4F87-4209-B024-B002D3438E61}',
	'TwoLineAngleDimConstraintProxy' : '{C7A68CF7-14FA-11D6-8E01-0010B541CAA8}',
	'NonParametricBaseFeatureDefinition' : '{559C5073-6378-47FD-AA38-DE0BB46A9268}',
	'DWGPointsEnumerator' : '{19B7AC3A-9E5C-424E-AE7D-33B805717AF5}',
	'ProfileEntity3DProxy' : '{BD923BF8-C5DD-4AE4-B577-0988B48FA89D}',
	'TangentConstraint3D' : '{0456FF0D-196E-4C72-989D-D86E3DD32955}',
	'ImportedDWGComponent' : '{DF1920AB-6CC5-4C6A-AA29-F4D3B0A30BA6}',
	'_AssemblySolver' : '{92E914D0-9FEA-11D6-8E0B-0010B541CAA8}',
	'DrawingNote' : '{33A71A9E-0E21-4B70-A688-604C897D3A5A}',
	'MidPointWorkPointDef' : '{28DD48D3-8D70-11D4-8DDE-0010B541CAA8}',
	'Centerline' : '{05EC93C4-CC47-450C-A826-FEC6692AD526}',
	'Vertex' : '{5DF8608F-6B16-11D3-B794-0060B0F159EF}',
	'MiniToolbarCheckBoxSink' : '{7DDF539F-7AFE-44BD-BAF9-BBAE51A93721}',
	'IRxEllipseFull' : '{5DF86030-6B16-11D3-B794-0060B0F159EF}',
	'Assets' : '{7289A75E-C37E-468C-904F-B2BADC61F272}',
	'RuledSurfaceFeatureProxy' : '{1CEE32D6-4997-4E37-ADBB-9AE5873BF30D}',
	'OffsetWidthExtent' : '{2EF323DC-CEC7-4E75-9C92-E7571F6653C3}',
	'ProjectAssetLibraries' : '{EC5AD11E-A3AB-4C86-85BD-61DEBF623987}',
	'IRxBSplineSurface' : '{5DF8609C-6B16-11D3-B794-0060B0F159EF}',
	'PointInferenceEnumerator' : '{6886F155-F98E-4287-BF33-F63CB776B6B2}',
	'DWGBlockReferencesEnumerator' : '{E2012607-EC0A-4F31-A888-E389AF5667E7}',
	'AnalysisManager' : '{BB075EDC-49B3-4F03-8737-5E20737B1AEB}',
	'SketchFillRegion' : '{920C0497-59BF-4F6C-A45C-8C8AA72750CF}',
	'_AssemblySolverNodeObject' : '{92E91440-9FEA-11D6-8E0B-0010B541CAA8}',
	'RolledHemDefinition' : '{F899D5C4-5961-43ED-A66C-E44A186C1B67}',
	'KnitFeatures' : '{1426BDF8-DD91-4FF0-AD8D-BB0EC8797B24}',
	'DerivedParameter' : '{0BDE54D4-8527-46BE-B2DC-7E9A5AED8AB9}',
	'NonLinearEdgeWorkPointDef' : '{25188AF6-308D-4181-879A-1B1084288928}',
	'CompositeiMateDefinition' : '{BAC6577B-6985-4B55-BADC-8113EFF69A3C}',
	'Arc3d' : '{744FFECE-189A-4ACC-8BCF-8F959D5E4EAE}',
	'BIMComponent' : '{47005682-42D1-4831-A4BC-63AD38B98D6E}',
	'iFeatureTableColumn' : '{34295D6D-002B-40DC-B1E9-E0D658532EF0}',
	'PunchToolFeature' : '{0DC3C610-F23D-44AD-B688-A47CAB5B04CB}',
	'BoundaryPatchDefinition' : '{4FF4C556-DB2C-4FD7-A7E5-06C171C18D7B}',
	'KnitFeatureProxy' : '{091BB62A-D3D9-4DBE-B8DA-69D51538AC92}',
	'ASideDefinitions' : '{6047CD23-889D-458D-9AFF-3CD3EB248BAA}',
	'Tolerance' : '{77B88412-A66B-43BE-BEE2-06CFE38B0C70}',
	'SketchBlockDefinitions' : '{BC450138-0F96-4342-BC2C-239747CD4797}',
	'iMateDefinitionsEnumerator' : '{22D71B5C-2F5E-4A1B-9328-ABE89F78ABC6}',
	'CommandBarBaseCollection' : '{51BAA695-F419-4D00-B6C5-7C32F4114562}',
	'PresentationExplodedView' : '{1F917159-C90E-4746-A4E3-E543894ADFD3}',
	'PresentationDocument' : '{29F0D46C-C114-11D2-B77F-0060B0F159EF}',
	'AssemblyJointDefinition' : '{AB9D8E26-4BEC-4E22-84B0-B1ECDED332D8}',
	'CenteredWidthExtent' : '{FE15F632-2312-46D7-86C9-5EEAAC85F7B3}',
	'ProgressiveToolTip' : '{5189E676-CC1A-4901-98E7-EC85130FDB63}',
	'BendsEnumerator' : '{AA1A04EB-B571-4568-86E6-7732B8330E9C}',
	'DrawingBOMColumn' : '{A36A7AD1-DDBD-4858-B025-D3F6C2042BC8}',
	'iAssemblyTableColumn' : '{90821476-EE63-4328-BC9F-164D0BBF6F9C}',
	'DWGPolylines3DEnumerator' : '{7CC584DD-262F-45D6-A383-6705655F2435}',
	'DerivedAliasComponents' : '{12EC238A-7178-44C6-BF92-F95F87CD7592}',
	'MiniToolbarListItem' : '{F22EBF2F-9F55-45FD-96DB-AABFBD40C177}',
	'_VbaImplementationPartEvents' : '{4B98058A-A232-47FD-9186-1070297036FB}',
	'RuleFilletFeatureProxy' : '{3F51C434-F75E-487F-93A2-5D1438AD5D41}',
	'LoftedFlangeFeature' : '{A7EA6C3E-D3A4-48BB-B600-E8D1097B9A55}',
	'FilletFeatureProxy' : '{4F16A71E-1337-40DE-B13F-DB996F9A716E}',
	'BossFeatureProxy' : '{C7EAA071-3EFA-4D2F-87BD-C41ABA98C678}',
	'ImportedDWGComponentDefinition' : '{AEFCDC34-A275-44DF-8A40-DF4B0BFD215F}',
	'LeaderNotes' : '{08DCE0A8-28F0-4513-A655-010AD06BC874}',
	'SketchFixedSpline3DProxy' : '{DBABE302-0C4A-4F2D-B67B-768F87C54E32}',
	'SketchEquationCurve' : '{6D7C3BDC-9CE1-4F23-82CC-2F001A326F89}',
	'SketchFixedSpline3D' : '{7A5B2F53-5756-4261-B6F1-4B5C3CDE1226}',
	'ShellFeature' : '{E861980A-A56F-416A-BF52-876C8A06CE4E}',
	'CheckPointsEnumerator' : '{68E4EA6F-3BEA-4F89-9335-F46CDF1AB005}',
	'ToNextExtent' : '{4E5273FA-20B0-41E3-BB29-03BB6C09B0FE}',
	'SurfaceTextureGBDefinition' : '{53A282CD-46BF-4A34-BE2D-1CB7FF469B34}',
	'Leader' : '{77D4A0A3-255E-42A8-B0F5-41FE5007BCCE}',
	'HorizontalConstraintProxy' : '{C7A68CDF-14FA-11D6-8E01-0010B541CAA8}',
	'DimensionConstraints3D' : '{3C934EFD-E26A-4940-BA5A-66908C16AA92}',
	'ChamferDefinition' : '{8415AC9D-CA60-4AD8-8F79-CE03F00F573D}',
	'DeleteFaceFeatures' : '{91BDBCAB-AC12-4216-ACE4-4F561D7DD4BD}',
	'IRxEnumComponentDefinitionReferences' : '{5DF86013-6B16-11D3-B794-0060B0F159EF}',
	'LightingStyle' : '{9DACF05E-4734-4D7E-986A-EE320F8A85C7}',
	'DSDegreeOfFreedom' : '{055EC025-CD9B-4983-97E2-2EC073939046}',
	'BrowserFolder' : '{9D063FDB-B597-49B0-8DBC-7EB3D5F715B8}',
	'MiniToolbarControl' : '{F4D9FAC9-D5F7-4FB5-8324-16CA73F349FF}',
	'DiameterModelDimensions' : '{17BE1D0D-0A2B-4A92-9CB2-A9725D391143}',
	'ChamferFeature' : '{539ACB89-A1F6-43E4-BC0A-BDCE1B127584}',
	'Path' : '{86338055-4538-47A0-BD9B-06A8C4BD8D93}',
	'CosmeticBendFeatures' : '{B534FD24-88CA-435C-95D5-F0DB0FB0238D}',
	'FeatureDimensions' : '{44A143D3-13C8-4B0A-AE53-CCC6169C44DB}',
	'HardwareOptions' : '{9A19AF07-A6BF-43AA-ABF3-870CA1CF329F}',
	'GrillFeatureProxy' : '{E19AC563-EC57-4E4A-9FE3-35AEB2C6B59A}',
	'DSLoad' : '{7771DA54-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'CommandBars' : '{6364B6D5-2994-46A5-8F53-03F63958B056}',
	'DynamicSimulations' : '{7771DA51-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'HoleFeatureProxy' : '{AD86A222-E8A0-4754-A764-65A958389DF5}',
	'SketchCircles3D' : '{FA48B024-CC3B-458F-B0EB-6FE4CBEC35DD}',
	'CommandBar' : '{EF0F253F-6AF9-40A8-BD13-B136E00B6588}',
	'CornerChamferFeatureProxy' : '{DDD17D41-9A17-4ADD-BDB2-E2701A524903}',
	'RigidBodyJoint' : '{1C0E39F2-15F3-41EA-94C1-62AD59AD25D9}',
	'EmbossFeatures' : '{730B9714-80D2-4009-8904-1AEF4EAF3F23}',
	'ReferenceFeature' : '{298849A9-ECAB-4234-9675-6FAA66A95E4D}',
	'SketchLine3D' : '{87056D9A-B0B2-4BD0-A6EC-51E9D893A502}',
	'Profile' : '{8006A03A-ECC4-11D4-8DE9-0010B541CAA8}',
	'SimulationManager' : '{7771DA50-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'Edges' : '{5DF86095-6B16-11D3-B794-0060B0F159EF}',
	'Welds' : '{F3C8A2A2-E9DF-454D-8769-8544374BB882}',
	'Polyline2d' : '{2A1047EF-0B48-413B-92FD-6CA45A488DA6}',
	'ModelLeader' : '{F2E7C272-A777-41B1-B217-C31B8CFAEF77}',
	'AssemblyOptions' : '{C6345819-0FAA-45A0-BF96-3C946F130076}',
	'CoincidentConstraint3D' : '{843FEEB5-A0EF-4C5B-8939-4F9B574119D8}',
	'BIMPipeConnectorDefinition' : '{E52803C6-7F1E-4D7B-9C0E-D4FA6BFFA00D}',
	'UserCoordinateSystems' : '{D0BD7B89-04B5-4165-8E8D-1DB705A02E47}',
	'Machining' : '{CF3DEE6F-DBB2-4393-A409-5D0ADC6CB12C}',
	'InteractionGraphics' : '{691AF5CB-83DC-4AF2-B689-F70AFB0D5020}',
	'RevolveFeatures' : '{8EB2E33C-2CF3-41E6-9B08-C0C0D15DF5EE}',
	'GeneralDimension' : '{EE21CD75-39FD-4683-BE24-BFBB9CA66EB4}',
	'SurfaceGraphicsVertex' : '{7C9B84A9-127C-42B6-A0A7-6CDC39B98CDE}',
	'NonParametricBaseFeatures' : '{59E208A8-BB82-4322-92D6-DA364F8B9AB0}',
	'MoveFaceFeature' : '{837D8FB2-848D-4A3B-8F83-ECCFDCAC2766}',
	'SketchEquationCurve3D' : '{67863AC3-95B7-4386-8A51-449E44AC2FBC}',
	'ChangeDefinitionSink' : '{48DDBD08-5630-4D9A-A71F-8F623A3ABB47}',
	'LoftRails' : '{3E43E559-0053-402D-BE5F-4AC170C11A04}',
	'MoldDefinition' : '{E8D1DB25-5BBF-4635-B2A9-2ECC3A150373}',
	'IRxTransactionEvents' : '{AE277671-2FDC-11D3-B78F-0060B0F159EF}',
	'BOM' : '{8AF6DB71-B75D-4D21-A837-4A6699E972BC}',
	'FaceCollection' : '{24B7B991-46D9-45F8-82CD-05212ECFC6DD}',
	'TangentiMateDefinitionProxy' : '{4FD9CE51-8E4D-4E4B-865F-FC4F0D5A0D5C}',
	'BalloonValueSets' : '{B3721DAB-0BAD-4296-8C1E-6608FC0F6049}',
	'SmoothConstraintProxy' : '{22324A8F-65DF-48BC-84CD-8A3B457B6A6E}',
	'UnfoldMethods' : '{5D0AB9A7-FCDB-4815-837B-BDCADEE5CEB2}',
	'ObjectsEnumerator' : '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}',
	'LineGraphics' : '{6C312B38-95D8-47B3-A6A8-78942F77A1C7}',
	'DerivedAssemblyComponents' : '{A52D98FA-2E72-4170-ABB4-6D10C2BCB095}',
	'VerticalAlignConstraint' : '{8006A094-ECC4-11D4-8DE9-0010B541CAA8}',
	'NormalToSurfaceWorkAxisDef' : '{B25B8DC2-B557-4E6B-81D2-A7D0C2A992F4}',
	'IPictureDisp' : '{7BF80981-BF32-101A-8BBB-00AA00300CAB}',
	'BossSets' : '{85672B0C-EA86-4DF1-B223-51DD72F29566}',
	'LibraryManager' : '{C3E0CCFC-A6F5-4C54-83E4-3A2CBF11D5D7}',
	'EllipticalArc2d' : '{C173A095-012F-11D5-8DEA-0010B541CAA8}',
	'SketchSplines' : '{8006A034-ECC4-11D4-8DE9-0010B541CAA8}',
	'PunchNotes' : '{46D8F255-F1A2-4C52-8D4B-29C02C8198FF}',
	'LegacyDistanceHeightExtent' : '{31B7388A-3B81-4568-B697-9C1F0D09E7AC}',
	'ChamferFeatures' : '{2D38284B-DEAD-48C3-905D-02D1B7432699}',
	'SpiralCoilExtent' : '{8D41F569-6407-4C82-A25E-762F6F8AA4B9}',
	'HelicalConstraint3D' : '{33E293A8-9DD6-4B9A-8274-E436A3BB3876}',
	'LoftFeatureProxy' : '{D3CB21DB-DF14-45FC-ADD6-8E8EED0AECC3}',
	'MiniToolbarCheckBoxObject' : '{3D7599FE-1A8A-47D8-A353-5C48B819A55D}',
	'DisplaySettings' : '{F2780C41-65D5-43E1-A259-E05D08ED1659}',
	'ToHeightExtent' : '{2C292AFE-8044-4E68-AB51-56340FBF0231}',
	'DrawingViewEventsObject' : '{1DA08DFE-88EB-4ABE-8FA8-34FD098D65AA}',
	'ReferenceAssetValue' : '{186F6C0F-C3A2-4798-9685-C773181074C1}',
	'AssetsEnumerator' : '{505BB0CA-670E-4D54-AB26-F66A64DBB72C}',
	'RestFeature' : '{669AFAAA-7F38-44FB-B50A-161D5C713C69}',
	'HelpManager' : '{9C88D3AA-C3EB-11D3-B79E-0060B0F159EF}',
	'SketchOffsetSpline' : '{063D7617-E630-4D35-B809-64D6695F57C0}',
	'OGSRenderItemsEnumerator' : '{1915251D-AC20-4EFC-A0EE-43FBEF266925}',
	'RenderStyle' : '{D480B516-E785-4CEE-B43C-FD4E3B6055F4}',
	'DerivedParameterTable' : '{B9831DEF-A198-48C1-8023-F5F05E55B092}',
	'TableStylesEnumerator' : '{E0B90B3E-0907-49B2-8E51-438C950F3A4B}',
	'ProfileEntityProxy' : '{C7A68CCF-14FA-11D6-8E01-0010B541CAA8}',
	'IRxApprenticeServerOld' : '{0A5CE3AB-073D-11D4-B7A4-0060B0F159EF}',
	'LayoutConstraint' : '{EB7E9B67-F77A-4ACE-A3CB-1D5C93F7EE9D}',
	'CentermarkStylesEnumerator' : '{8E9F0865-0AE2-4AAC-8E67-0CED8434114C}',
	'EdgeProxy' : '{46AEA72F-4302-11D4-B7AB-0060B0F159EF}',
	'LineAndPointWorkAxisDef' : '{18A18CCA-283E-4E06-9358-1949A91CECF1}',
	'DirectionAndDistanceMoveDefinition' : '{080ECFB1-9C78-4A73-8FC9-7A438D08B3A6}',
	'FlangeDefinition' : '{3978BB7A-4A07-475B-BD57-13A05A343EDB}',
	'SketchEllipticalArc3DProxy' : '{DD3E1C70-8EDA-466B-B455-5CCE10BBA910}',
	'RigidBodyJoints' : '{1C4A4777-E52F-405F-BABA-7ED0931E81C0}',
	'OriginIndicator' : '{96E36D73-DFEC-4CF8-9DB3-F97F01A41A23}',
	'RipFeature' : '{38D353FC-D30E-4B08-B73A-785787D4D7AD}',
	'ComponentDefinitionsEnumerator' : '{C5AC2A12-6439-4CB5-BA1E-45765296285E}',
	'FlatPatternPlates' : '{BF8CF130-DAD5-444E-9DED-16AD1178DE2F}',
	'AnnotationPlaneDefinitionsEnumerator' : '{FA169DD0-A365-49D9-9572-F0F23F2B634E}',
	'UserCoordinateSystem' : '{F0854465-652D-4375-98A4-7C875BFE7A9C}',
	'TextBoxDefinitionHandler' : '{92A50081-D0B7-428F-BFF0-B0D277C3AEB0}',
	'IPersistFile' : '{0000010B-0000-0000-C000-000000000046}',
	'iAssemblyMember' : '{29049E48-996E-4799-8DA6-778A0B82AB54}',
	'DrawingBOMRow' : '{3538A9B3-0A9F-4B3E-9FC9-3272AB0D7C2B}',
	'FaceFeatureProxy' : '{6DEF95B4-C5EF-4FBA-AEE9-B9486F648CAB}',
	'UnfoldMethod' : '{F69435CA-41FA-4FDC-8E07-2D677A30AB2C}',
	'CommandBarPopUp' : '{32429DA6-B712-4638-8C53-B1EEE7C1D18B}',
	'EmbossFeature' : '{6A0A9BAD-53F2-4254-A34E-9262F980B5CE}',
	'FaceShell' : '{5DF8608A-6B16-11D3-B794-0060B0F159EF}',
	'BIMCableTrayConnectorDefinition' : '{2D6BA5C4-3929-44A3-8D59-5A173034BBF1}',
	'DrawingDimension' : '{63E2B412-8EDA-496C-BAF6-A28928F74091}',
	'ContentTreeViewNodesEnumerator' : '{2CB6EA8B-44E3-4C93-BB2A-531D62EBD934}',
	'FoldDefinition' : '{0AE09AED-1DFB-41D3-B640-E0E9A24FA8C0}',
	'InsertiMateDefinition' : '{4FE10280-6679-4500-B7CE-411995D157E7}',
	'BOMQuantity' : '{07F8CD55-9194-4CDB-8403-6BFC4F99D1EE}',
	'MoveFaceFeatures' : '{04370FAD-4F3A-4589-A7F8-6DFA839522D3}',
	'TwoPointDistanceDimConstraint3DProxy' : '{5B29EB3A-F2F2-4998-B713-03042554E46C}',
	'SketchEllipse3DProxy' : '{A50E48BD-8D0E-4C9A-B3C7-D6EC114ACB3D}',
	'Profile3D' : '{2A8678EA-A024-469A-80DC-D1EAD67847A3}',
	'FaceProxy' : '{46AEA72B-4302-11D4-B7AB-0060B0F159EF}',
	'SketchBlockProxy' : '{36B9F8B4-FD23-4AC9-A41F-4778F124C0B7}',
	'iMateDefinition' : '{928894AE-2111-43EB-B77C-4E1A7388CD75}',
	'ContentTableColumns' : '{E06998C3-E510-47D3-BE8D-2CD348F24456}',
	'SketchControlPointSpline3DProxy' : '{7D3BDDB1-82EF-4AF6-80C2-96BED3462559}',
	'AssemblyConstraints' : '{AA044AA3-D685-11D3-B7A0-0060B0F159EF}',
	'TableParameters' : '{0E4C2356-1844-43F1-BAFA-45AA948EDAD8}',
	'ApprenticeServer' : '{C343ED82-A129-11D3-B799-0060B0F159EF}',
	'MeasureTools' : '{78B3596A-176A-43F5-A65C-4BDFFC042236}',
	'ModelAnnotationText' : '{B513304D-05B5-4DD7-AA23-E4BF2F120406}',
	'iPartTableRow' : '{A8DB137E-896E-4B61-8813-E49040BBE99E}',
	'EndOfFeatures' : '{A89E388A-13C9-4FFA-B777-9C0E1C81F136}',
	'SheetMetalStyle' : '{46A4AA12-70D3-4BEC-B059-D285F084B979}',
	'DWGPolyline' : '{249D0F99-CAD8-4B05-9A8C-AAF415CEA2DC}',
	'ImportedGenericComponent' : '{D2653F5F-C73A-4FAE-9172-EA1B60098B07}',
	'ComponentDefinitions' : '{5DF86022-6B16-11D3-B794-0060B0F159EF}',
	'MessageSection' : '{C7CECA91-B8BD-4C0E-A998-FBFD9BE85416}',
	'ModelLeaderNoteDefinition' : '{3614BB38-60E8-42E0-84E1-A0045BFB25D4}',
	'BIMComponentPropertySet' : '{5F89369C-998C-4AD6-B59D-FBA9AFDCFB65}',
	'TriangleStripGraphics' : '{907F6639-A091-4B19-B1B4-E677D960934C}',
	'iFeatureVectorInput' : '{F302D8D2-7DF4-4AD2-9933-9037EB507A90}',
	'IRxComponentDefinition' : '{5DF8600D-6B16-11D3-B794-0060B0F159EF}',
	'Torus' : '{5DF860A4-6B16-11D3-B794-0060B0F159EF}',
	'TrailSegment' : '{8D039683-92D8-4F9E-995C-1FDF01AA16D0}',
	'HelicalConstraint3DProxy' : '{5DE610F3-F512-4973-B78A-F50669560B4B}',
	'DocumentInterests' : '{B1DA2E33-F616-41D4-917A-CEB1138058D0}',
	'RestFeatures' : '{0E000A5B-67FD-4B23-A312-E6E5F444C045}',
	'CoincidentConstraintProxy' : '{C7A68C71-14FA-11D6-8E01-0010B541CAA8}',
	'SurfaceTextureSymbols' : '{F828B7C4-4B02-4B69-8D22-8BC7BA9D6243}',
	'EdgeUseDefinition' : '{6307798C-50E3-4E9E-B502-038DA82B7C74}',
	'TangentDistanceDimConstraint' : '{C173A085-012F-11D5-8DEA-0010B541CAA8}',
	'ColorSchemes' : '{817C825E-2D55-4E09-A69E-789E9753959D}',
	'MateiMateDefinitionProxy' : '{619B5213-A92D-4D4B-BE3F-6CA4B1715A78}',
	'ModelLeaderNode' : '{7430CE13-37A3-4A67-A645-2AAD0BB71038}',
	'UnitVector' : '{CB69F176-558E-11D3-B793-0060B0F159EF}',
	'TriadEventsSink' : '{5401A856-D03A-4418-AAA2-F1B677FA410D}',
	'ModelAnnotations' : '{9789E1AC-1767-4225-96DD-FD06F614AD59}',
	'ExtendFeatures' : '{4A355C86-508E-4A45-80C3-001139E9FD81}',
	'GrillFeature' : '{5EC2AE01-F47C-4E11-B8CD-67A017E07132}',
	'ClientFeatureProxy' : '{EF375552-9B4F-4384-9775-4D4EE910DA33}',
	'WebBrowserDockableWindow' : '{1A88CE14-0590-4C13-B58A-C9B7FA1458C5}',
	'CombineFeature' : '{2D0B10A8-711C-4352-AEE1-C8465CBDC36B}',
	'DataMedium' : '{6BA435DB-BBD6-11D4-8DE6-0010B541CAA8}',
	'ReferenceKeyEventsObject' : '{B4A5B240-ED5B-4F0F-B5C7-A1D21FB85939}',
	'IRxFileSaveAs' : '{42C7E0BE-FDCF-11D2-B785-0060B0F159EF}',
	'RipDefinition' : '{453A1005-42C9-469C-847E-CEA7D550751B}',
	'LineWorkAxisDef' : '{28DD48B9-8D70-11D4-8DDE-0010B541CAA8}',
	'AssemblyEventsSink' : '{BABF5BBF-9878-11D4-8DE2-0010B541CAA8}',
	'ModelHoleThreadNoteDefinition' : '{90ED1343-7C9E-4042-9664-93D821AF88CC}',
	'ProjectOptionsButtonSink' : '{0C946530-B275-481A-9573-6CA7D4F93611}',
	'PartEventsSink' : '{BABF5BAF-9878-11D4-8DE2-0010B541CAA8}',
	'EdgeDefinitions' : '{7F842490-A580-4A3A-AF94-DF8E5D292A42}',
	'CircularOccurrencePattern' : '{6F9AAB22-31DC-4F5A-98ED-8A8693D5BD1C}',
	'DockableWindowsEventsObject' : '{32958A3F-CEA1-4390-946D-3D2F2E92675B}',
	'GenericObject' : '{32E4A31B-C5E8-11D2-B77F-0060B0F159EF}',
	'WireEdgeDefinitions' : '{4B427038-81A6-4E75-A633-CF7CCBDD8160}',
	'Sketches3DEnumerator' : '{EC6AB9BC-0F8E-49E6-B809-09E5962BA707}',
	'GroundConstraint' : '{8006A082-ECC4-11D4-8DE9-0010B541CAA8}',
	'TeardropHemDefinition' : '{4F1B00F2-FA18-46EA-9C2F-97574189230D}',
	'ConcentricConstraintProxy' : '{C7A68CD3-14FA-11D6-8E01-0010B541CAA8}',
	'BalloonStyle' : '{04B1FC27-4477-491B-A640-3C313E9AC402}',
	'TangentConstraint3DProxy' : '{F2BCCD2A-83E0-4528-A039-318A93C7ABBA}',
	'DocumentsEnumerator' : '{ACE59077-7778-11D4-8DD8-0010B541CAA8}',
	'RefoldFeatures' : '{AD87B241-B3FD-475C-B369-AD3C5D3E3E0D}',
	'FileSaveAs' : '{9CAF98A3-33EA-11D3-B78F-0060B0F159EF}',
	'AssemblyConstraint' : '{AA044AA2-D685-11D3-B7A0-0060B0F159EF}',
	'Polyline3d' : '{C9EBE756-798A-4E78-8CC4-DA91D7737321}',
	'AssemblyJointProxy' : '{4E19FF37-38A9-494F-AC1E-557D5D01CDB4}',
	'PlanarSketch' : '{2C16787F-83FF-11D4-8DDB-0010B541CAA8}',
	'ModelFeatureControlFrames' : '{01711A84-0018-4452-A736-D9292E754D38}',
	'DirectEditScaleOperationProxy' : '{BC329A16-2294-4C2D-AEAC-AE61F5433C7B}',
	'TextGraphics' : '{F3D4C961-7227-4E32-90A3-C60A9EEFA90D}',
	'TranslateTranslateConstraintProxy' : '{FBC6B272-3033-4F57-8279-7D70F3FFD508}',
	'ComponentOccurrencesEnumerator' : '{EF562DD1-92FA-11D4-8DE0-0010B541CAA8}',
	'EnvironmentBaseHandlerObject' : '{EBB974BD-2A69-4125-899A-5752878B7E55}',
	'MidSurfaceThicknesses' : '{6E9FA739-9CD7-49D3-85B9-72F260BFBF52}',
	'TriangleGraphics' : '{B5E1C129-EE0E-4C45-9AC3-FE79794F1EB0}',
	'MiniToolbarObject' : '{DBC99CB5-8EB0-4D45-BAC7-DE9D532FDD04}',
	'DWGEntitiesEnumerator' : '{5F9B0BEB-E30C-4750-A733-1FCFE4218750}',
	'Circle' : '{49CB4BB5-872A-11D3-8524-0060B0F0B5B7}',
	'AssemblySymmetryConstraint' : '{BA9EC28C-765B-4481-8A8C-20489290B35E}',
	'GeneralPreferences' : '{9C88D3A8-C3EB-11D3-B79E-0060B0F159EF}',
	'UserCoordinateSystemSettings' : '{42E1EF4D-7D8F-49EA-95A4-B4661D4983AA}',
	'GraphicsDataSets' : '{400A64D5-7150-42F6-943E-F190518265CA}',
	'ShellDefinition' : '{C80E7C12-B126-45F2-A228-704248D58530}',
	'ContourRollFeature' : '{1492BD29-4122-41C8-AA02-B871BC06CCA1}',
	'RuledSurfaceFeature' : '{E58169E1-CCA4-432A-9626-A37ABF5F287E}',
	'ModelParameters' : '{652F6A52-8B8A-4CEF-B1DC-C78751914993}',
	'ContentFamiliesEnumerator' : '{239A8027-E757-4A2E-B8DC-9203A644401F}',
	'IRxEnumFaceShells' : '{5DF86071-6B16-11D3-B794-0060B0F159EF}',
	'LoftedFlangeFeatureProxy' : '{87DB004A-F974-4BFE-A8BD-65BA290F2D43}',
	'ProgressBarSink' : '{6322C608-F92C-4CBB-9C17-B1661DA641AB}',
	'RadiusModelDimension' : '{672C4DAF-1B67-4131-8F53-9274F42E44E9}',
	'SketchFixedSplineProxy' : '{C5195DC5-0D96-45C2-8E51-BE1A305AC086}',
	'BrowserPanesSink' : '{B159D948-7FC9-4D48-B482-FC7FD152AFCA}',
	'PartOptions' : '{986FCF92-8A47-4DEC-9007-DD852292DE71}',
	'BOMRowsEnumerator' : '{BCDD5058-E7D5-4E88-8EF8-8D6370E0CBA3}',
	'DerivedParameters' : '{D4C98D93-FA6C-4602-8EB8-2709938BFE74}',
	'EllipticalCone' : '{FA34A402-F063-11D3-B7A2-0060B0F159EF}',
	'Cone' : '{5DF860A3-6B16-11D3-B794-0060B0F159EF}',
	'Border' : '{A907AEAF-A78F-11D5-8DF8-0010B541CAA8}',
	'MoveFaceDefinition' : '{B0A76319-7649-4B77-9159-0975E700253B}',
	'TextStylesEnumerator' : '{D4AAD36D-D0D1-4BFC-9C3A-C4718D3D9209}',
	'PerpendicularConstraint3D' : '{2035E584-09E7-4B18-9698-014DEF44B10E}',
	'Style' : '{A5AFB9DC-4066-4800-A459-E4A7E4E433B6}',
	'FaceFeatures' : '{C0D71AC3-E085-4A0E-85FF-549C000BA1E7}',
	'iMateDefinitions' : '{AE309209-288A-4083-BEAB-7DFB7EC9947D}',
	'BendConstraint' : '{AE27E3D2-63C8-4D39-B2CA-A6387AE5D7B3}',
	'DerivedPartComponents' : '{CF891949-B3AD-4A38-9254-7CAFE0F3B7F6}',
	'MacroControlDefinition' : '{2F800161-0E4D-4953-A0B7-E55EE05E039B}',
	'DerivedAssemblyComponent' : '{A1D2EAAD-28A1-4692-BC13-883879C68894}',
	'SphereCenterPointWorkPointDef' : '{609506AD-969B-4FEA-9DA5-D2FC535472FA}',
	'FaceDefinition' : '{F3ACEE71-EC98-43F5-AC33-D0BDE47609EE}',
	'BIMConduitConnectorDefinition' : '{744F35C4-CD6F-46C3-87B8-80425AB4AFA2}',
	'ProfilePath3D' : '{D7347916-69D8-4972-AEBE-95BE5672BED2}',
	'IRxGeometryProxy' : '{5DF86010-6B16-11D3-B794-0060B0F159EF}',
	'IRxPoint2d' : '{CB69F15E-558E-11D3-B793-0060B0F159EF}',
	'TestInputOutput' : '{2190DB7B-9EAB-45D5-B9E0-B7FE50E1F50B}',
	'DerivedAliasComponentProxy' : '{51182028-01DC-4629-AD22-8BFF0D74FA1A}',
	'MiniToolbarSliderSink' : '{2F9E3271-4E14-4B76-9581-602AED994066}',
	'RectangularOccurrencePatternProxy' : '{17FD3E5D-FF18-4E1C-AE86-C9A5A295B2BE}',
	'FixedWorkPointDef' : '{28DD48D5-8D70-11D4-8DDE-0010B541CAA8}',
	'SketchImageProxy' : '{0FCBB605-3830-4C3F-95F6-76A4CB15F659}',
	'ControlDefinitionEventsObject' : '{4CF7D720-1E41-4049-8C1A-70C980D11667}',
	'TestProgram' : '{52D6C08A-B387-4F4C-A2E3-4F3CFFF276CE}',
	'DrawingBOMRows' : '{6ADEEB5C-21C6-4995-91AA-7FD0CE1D0073}',
	'EqualRadiusConstraintProxy' : '{C7A68CDB-14FA-11D6-8E01-0010B541CAA8}',
	'CurveEvaluator' : '{5DF860B0-6B16-11D3-B794-0060B0F159EF}',
	'EnvironmentList' : '{A1C8AD17-F4C3-4424-982C-9D628A5A4ECA}',
	'DirectEditSizeOperation' : '{047BD59F-24A4-40D2-A47E-6FED9726BA88}',
	'ArcLengthDimConstraint' : '{FD350F5E-E3C9-4268-BCF4-0DEA91B6F8EF}',
	'PointCloudPlane' : '{6B3ECB2F-78BA-492E-9235-E68EA88F66E9}',
	'ExtendFeature' : '{2DADCD08-8ED5-4F71-88BF-481E8B0E9847}',
	'_DocPerformanceMonitorSink' : '{C2083475-A259-414A-BED9-FC43291F4455}',
	'DWGEllipticalArc' : '{E9455662-85DE-499A-9965-81270D314D70}',
	'BendDefinition' : '{54E4411A-7349-4591-991E-9F930A01EB83}',
	'IRxEllipseFull2d' : '{5DF86031-6B16-11D3-B794-0060B0F159EF}',
	'PathAndGuideSurfaceSweepDef' : '{7D7EAE29-869F-48FB-AD5E-797AB5B87F65}',
	'IRxEllipticalCone' : '{97ED8AED-EF9D-11D3-B7A2-0060B0F159EF}',
	'SketchEventsObject' : '{0CB0F042-1627-49BF-B430-619A3AD6FADC}',
	'ComponentGraphics' : '{C958801B-73D0-4031-B9F6-5CDBCE975ABC}',
	'RevisionTableCell' : '{63C5D5FD-8348-4246-BE53-619E8C48EC6F}',
	'EqualRadiusConstraint' : '{8006A080-ECC4-11D4-8DE9-0010B541CAA8}',
	'IRxEnumEdges' : '{5DF86075-6B16-11D3-B794-0060B0F159EF}',
	'ShadedDisplayOptions' : '{DA7E3A1C-5473-4CC3-8E19-25F8DE00C0A6}',
	'PointInference' : '{6886F154-F98E-4287-BF33-F63CB776B6B2}',
	'LinearModelDimensionDefinition' : '{84385A0E-4B73-48FE-B948-CB83894F2E61}',
	'DWGEllipticalArcProxy' : '{5EE74326-54FB-4C26-97AD-B78830B6E0C0}',
	'UnfoldFeatureProxy' : '{550A5700-23FB-4E1F-98D6-5BD7D9701ACD}',
	'IRxBox2d' : '{5DF8602B-6B16-11D3-B794-0060B0F159EF}',
	'SurfaceTextureStyle' : '{F329734C-AAC4-40B9-A1A0-A051679C1EC7}',
	'IRxApplicationAddIn' : '{E3571291-DB40-11D2-B783-0060B0F159EF}',
	'MirrorFeature' : '{12BF1F8A-5679-468F-A820-DA5532624CEA}',
	'VerticalConstraint' : '{8006A092-ECC4-11D4-8DE9-0010B541CAA8}',
	'AssemblyConstraintsEnumerator' : '{56C3574C-13A4-46AB-B981-4B45784B2156}',
	'SheetMetalFeatures' : '{41ADE507-16D9-4103-BD0C-FA1C196B9DAA}',
	'AngleExtent' : '{312EFE2A-648A-4715-85F4-B7A1EF02CCB9}',
	'FilletDefinition' : '{448C7AED-838C-44DB-87FC-2D18E74AA05A}',
	'RevisionTableColumns' : '{CBC02A91-4346-4459-8A47-C845B0A4051F}',
	'CornerChamferFeature' : '{8B72B033-1F46-4D07-8B26-6E9A718A1533}',
	'File' : '{6E5CDAB2-6BA5-4EAD-B357-78646BE0A813}',
	'CustomTable' : '{88F528C1-AE9A-457B-8A19-A6224F473A62}',
	'ProjectedCuts' : '{3C83A20C-1648-40C3-9A28-FFDE72124D2C}',
	'AttributeSet' : '{EFA08B24-F116-4751-90FA-46ADE09BF0B3}',
	'SmoothConstraint3DProxy' : '{748041B9-77F8-481D-BADA-8F03152C3AF1}',
	'SymmetryConstraint' : '{8006A08E-ECC4-11D4-8DE9-0010B541CAA8}',
	'AutoCADBlockDefinitionsEnumerator' : '{892AF496-C31A-431A-9B15-39FA10940A86}',
	'TransactionManager' : '{AE277672-2FDC-11D3-B78F-0060B0F159EF}',
	'HoleFeature' : '{ABA7FFC5-E604-498E-B1B1-B829D4E059EC}',
	'CollinearConstraint3D' : '{E8BE2118-716C-40FD-8BC0-2517B253E4F9}',
	'ControlDefinitions' : '{B9D982C4-3FFF-4796-AD6D-C6D1F16D7BA9}',
	'Plane' : '{CB69F17A-558E-11D3-B793-0060B0F159EF}',
	'iPartFactory' : '{B9F30FBA-DABE-4327-AAB3-65E2160135C1}',
	'WorkSurfaceProxy' : '{9A104FEF-2749-4112-AA6D-937CB4F44420}',
	'GeneralDimensionsEnumerator' : '{294E366C-86B9-4CF7-9CF9-10D83787D2A6}',
	'CutDefinition' : '{3B809336-2821-4E36-B2A1-31B987537E57}',
	'SketchedSymbolDefinition' : '{A907AED3-A78F-11D5-8DF8-0010B541CAA8}',
	'ImportedModelEntity' : '{3F35DB6C-C158-4203-B420-AE4ABCC4B908}',
	'ContourRollFeatureProxy' : '{206F590B-1854-41A8-9ACE-CB18BCF1154B}',
	'FilletVariableRadiusEdgeSet' : '{A335F5F6-7194-409E-94A7-45B617264920}',
	'TransactionEventsObject' : '{ABD216FA-7559-4883-93D7-C0A9ECFF19C4}',
	'ModelParameter' : '{916D7FDB-CFE6-4FB1-8921-694DC9CD2793}',
	'ReferenceComponent' : '{DD8AB7FC-77D4-4EA8-83A9-A0C868DABFC0}',
	'SketchFixedSplines3D' : '{80DBF4D7-FEC3-454C-BF1C-65BCDB27188C}',
	'FixedWorkAxisDef' : '{28DD48C5-8D70-11D4-8DDE-0010B541CAA8}',
	'Environments' : '{D23D422B-C248-4EA4-98AF-9E6390C99964}',
	'RadiusModelDimensions' : '{7C6BCC40-95D1-4B47-AE7F-A5EBFEF95851}',
	'TextBoxes' : '{A907AE97-A78F-11D5-8DF8-0010B541CAA8}',
	'DisplayOptions' : '{48694BB1-0E75-4A39-94E0-C7C133C23305}',
	'HoleThreadNotes' : '{DDB3F084-C3BC-4A46-8B6A-A169466514BF}',
	'SketchArcProxy' : '{C7A68CC1-14FA-11D6-8E01-0010B541CAA8}',
	'ReferenceComponents' : '{45D64D2D-8D31-4ABD-BB94-E55F0879A90C}',
	'InventorVBAComponents' : '{24FAC734-1A3D-404E-A28B-7CC1AD47DCA1}',
	'WorkPoint' : '{28DD48C9-8D70-11D4-8DDE-0010B541CAA8}',
	'LineSegment2d' : '{C173A08D-012F-11D5-8DEA-0010B541CAA8}',
	'Wires' : '{31B11F76-0E31-45DF-8BE6-409EE5416DC5}',
	'SplineFitPointConstraint' : '{8006A07A-ECC4-11D4-8DE9-0010B541CAA8}',
	'LinearModelDimensions' : '{D60D7065-70F2-4E41-AE17-17E36EE573DF}',
	'FlatPatternPlate' : '{938A5052-5007-48B1-9629-D00898FD6855}',
	'DrawingDocument' : '{29F0D467-C114-11D2-B77F-0060B0F159EF}',
	'GeneralOptions' : '{DBB345F5-06CB-4B20-96B8-C47EF589ECBE}',
	'BSplineCurve2dDefinition' : '{E3B2EB5A-FE46-4DA6-8DDD-6135E2120CB2}',
	'IRxFacets' : '{2894395B-1E28-4516-8308-6AD0911B83D5}',
	'PointCloudRegion' : '{E34C07F3-B8FF-4181-ADC4-DEE3D6550961}',
	'DisabledCommandList' : '{81710E0C-B8F1-4D04-BDDF-AC92C274CC81}',
	'PointCloudCrop' : '{2D5EB497-6E4D-4B66-B185-EB6C7C188F2F}',
	'LoftFeature' : '{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}',
	'VertexDefinition' : '{40E01FF0-E437-4C55-83A4-8E3FA8B19225}',
	'IRxEllipticalCylinder' : '{FA34A3FE-F063-11D3-B7A2-0060B0F159EF}',
	'MidpointConstraint3DProxy' : '{2B2BEA0C-F141-4B3E-B061-1B2C8C6B5D9F}',
	'MoveOperation' : '{BC1B0D6F-086B-43CC-91CC-6BEF7D7E35C1}',
	'ISequentialStream' : '{0C733A30-2A1C-11CE-ADE5-00AA0044773D}',
	'TextBox' : '{A907AE99-A78F-11D5-8DF8-0010B541CAA8}',
	'MateConstraint' : '{CEFDC141-B989-4BF3-BDD7-8308D8089FFE}',
	'BrowserNodesEnumerator' : '{76B0EC66-F962-4D22-9E96-3D02F49AD363}',
	'SmoothConstraint' : '{8FFF6DFE-F659-4C77-81E5-DD9B70A37D90}',
	'BIMConnector' : '{12DA4D02-DCE6-4F08-ADEB-9EE13C559C52}',
	'IRxFileAccessEvents' : '{32E4A318-C5E8-11D2-B77F-0060B0F159EF}',
	'Line2d' : '{CB69F179-558E-11D3-B793-0060B0F159EF}',
	'_VbaImplementationDrawingEvents' : '{296442E1-7AB3-46B9-8494-7FBB585F6B50}',
	'DSResults' : '{055EC026-CD9B-4983-97E2-2EC073939046}',
	'BrowserNode' : '{5D21C290-CB28-4861-9367-C3F1B9F0BCCB}',
	'FileDialog' : '{BA80AE34-5BB2-4C90-BFDE-64DA56286813}',
	'CameraEventsObject' : '{F2BD70CA-061C-45C4-B057-88526074C390}',
	'ModelAnnotation' : '{089C1D07-A3A6-4649-B1C4-CE9DAB1D8BBE}',
	'iFeatureParameterInput' : '{95B2DD02-374C-41C5-998C-7FCF8BDCA452}',
	'ExtrudeFeatures' : '{F05DFBBD-F824-48A1-8272-A62F1A524F42}',
	'ApprenticePrintManager' : '{8530B3FF-DBD2-4C75-A6EC-0755B8229AE7}',
	'IRxDocumentEvents' : '{70109AA7-63C1-11D2-B78B-0060B0EC020B}',
	'DWGPolylinesEnumerator' : '{E25D1002-8B00-4E7A-A6F3-DF7BDCC7A63A}',
	'iFeatureTableRows' : '{4A66B607-4991-4FA2-A361-CD8424A99A70}',
	'ProfileProxy' : '{C7A68CCB-14FA-11D6-8E01-0010B541CAA8}',
	'BrowserNodeDefinitionSink' : '{11D880AF-2B60-4816-A74A-73526CFE6FDD}',
	'RepresentationEventsObject' : '{FB4D47B9-777E-49C5-99CB-9CE5C345D66E}',
	'ComponentDefinitionReference' : '{5DF8601F-6B16-11D3-B794-0060B0F159EF}',
	'HorizontalAlignConstraintProxy' : '{C7A68CE1-14FA-11D6-8E01-0010B541CAA8}',
	'InsertConstraint' : '{0AEBFB16-385B-4663-B17C-D07F576F2C70}',
	'SketchPoints3D' : '{3BCDEC54-2F73-4114-A7CB-ACF5E823B67D}',
	'RotateRotateConstraint' : '{F8F30CD3-A44B-4C8A-B9D2-287361B0BD26}',
	'UserInputEventsObject' : '{2772058F-17D8-4969-8D46-51860F09AC9B}',
	'HoleTable' : '{13A31354-BFF7-45CC-B749-2CE174780E77}',
	'EllipseRadiusDimConstraint' : '{6ABB821F-4962-11D5-8DEE-0010B541CAA8}',
	'AssemblyComponentDefinition' : '{AA044AA1-D685-11D3-B7A0-0060B0F159EF}',
	'IRxBox' : '{5DF8602A-6B16-11D3-B794-0060B0F159EF}',
	'FilletSetbackVertex' : '{C6C1652F-6D5B-495D-B7E5-F4DEB205BA25}',
	'iPartTableRows' : '{B01CC9E0-93E8-4482-9321-D8F52A7AB213}',
	'SketchCircle' : '{8006A04C-ECC4-11D4-8DE9-0010B541CAA8}',
	'DeleteFaceFeature' : '{4CDC6B45-25DB-442E-BF8B-12C87365788E}',
	'iMateResultProxy' : '{5EA2744B-95DB-4104-B06A-E9BB6712D59E}',
	'DrawingViewEventsSink' : '{F777456B-314C-4F8E-87E0-196CB7FC8D32}',
	'SketchSplines3D' : '{611271CA-48EE-4EBF-9ACD-CCD081142400}',
	'LineLengthDimConstraint3D' : '{04A196FD-3FBB-43EF-9A79-2735B3B99214}',
	'RevisionTableRows' : '{C5EDE080-C83A-4D7F-9560-B867FD29DFD6}',
	'HoleTableColumn' : '{A2E47B01-25D6-4047-BC17-FA7F71B18599}',
	'ChainDimensionSet' : '{5BC0F92E-9C6A-4887-9B29-E1831F845DB2}',
	'WorkPointProxy' : '{3CBE8AA7-3D92-11D5-8DEE-0010B541CAA8}',
	'SurfaceEvaluator' : '{5DF860B2-6B16-11D3-B794-0060B0F159EF}',
	'BrowserPanes' : '{1EBEC999-3A4D-4A4C-A35A-3F2E773DD56D}',
	'PointCloud' : '{6E45ED1A-92ED-469A-9CE0-79C26C9CB5E5}',
	'DirectEditFeature' : '{602389D5-6C6A-4368-A6F2-47D54FA1FBA4}',
	'DiameterGeneralDimension' : '{98D51E77-8775-4472-8AB0-50BCA8F56023}',
	'ModelLeaderNote' : '{5194100D-435F-4C85-A922-6BD3E4CC9C36}',
	'MaterialsEnumerator' : '{DDD3ADB9-30D8-4E01-8E88-42ABF8645AD4}',
	'MiniToolbarDropdownSink' : '{8AAC5924-81F8-4760-9BA0-3BD408FA7BA5}',
	'CommandBarControl' : '{4BF433DE-1B2F-4ADE-B71C-0C826CF2CC88}',
	'BendNote' : '{F5DA8C39-2BD7-4E77-BE94-81743E81ACC9}',
	'SilhouetteCurves' : '{B4F71C8B-BC8D-47F1-A327-9275F5FB443D}',
	'TextBoxConstraintProxy' : '{2F77E2FF-BAD3-43A4-9874-8A99E824E060}',
	'GeneralDimensions' : '{A0F72CD2-B7A3-4EBA-9CDB-47F42BC74777}',
	'SketchEntitiesEnumerator' : '{B546124B-09AA-11D5-8DEC-0010B541CAA8}',
	'TransactionsEnumerator' : '{AE277673-2FDC-11D3-B78F-0060B0F159EF}',
	'RectangularOccurrencePattern' : '{A8E2C150-78E9-4E97-A4A0-BF43936B2A45}',
	'MoveFeatures' : '{972006AB-5037-4850-AF98-8D3B5A55C1F4}',
	'ObjectCollection' : '{6939FFDD-BA10-11D2-B779-0060B0F159EF}',
	'DocumentInterest' : '{36DB2A89-F970-4C03-AA8A-7864122D553B}',
	'WeldsComponentDefinition' : '{268D663B-4B37-11D6-8E06-0010B541CAA8}',
	'DrawingStylesManager' : '{1A58DFEF-0B8C-44DF-97AF-4DAC85734B04}',
	'HighlightSets' : '{DD60CA37-AB7B-491F-AD9E-C9DF3B4B5BBB}',
	'ToExtent' : '{C73A295D-CB57-4B32-AA53-652422FACF65}',
	'PointCloudRegions' : '{10DE860A-67D1-47ED-A23A-291BD48E25E9}',
	'Point2d' : '{CB69F173-558E-11D3-B793-0060B0F159EF}',
	'PointHolePlacementDefinition' : '{1993ABC5-7080-4CB1-9CE3-406B4B70B951}',
	'WireframeDisplayOptions' : '{75091477-A808-4B93-AF11-14C0CD466611}',
	'IRxVector' : '{CB69F15F-558E-11D3-B793-0060B0F159EF}',
	'OGSSceneNodesEnumerator' : '{E8DC5B4C-F562-4911-AFBC-41961F55C140}',
	'_AssemblySolverNodeSink' : '{92E914A0-9FEA-11D6-8E0B-0010B541CAA8}',
	'RevolveFeature' : '{87F4CA2E-5700-4FC7-A283-8E2D90FE5F61}',
	'CornerRoundFeatureProxy' : '{F8B2175E-285B-4787-B12A-6E485CA1885B}',
	'ModelingEventsSink' : '{124B76C3-CB79-4414-9CB9-DDA2F8C5C90A}',
	'SurfaceTextureISODefinition' : '{587A7801-DF86-4DC8-BD20-ADA5FB1193C2}',
	'SketchLine3DProxy' : '{BD020927-670F-4F30-943B-75A2EC87E052}',
	'MiniToolbarValueEditorObject' : '{4E97BC3C-1235-44DE-8B31-571FA40955B5}',
	'Sketch3DOptions' : '{D39AB98F-45E0-4CAE-A0F2-4490804F2AD3}',
	'IRxApplicationAddInServer' : '{E3571292-DB40-11D2-B783-0060B0F159EF}',
	'AutoCADBlocks' : '{50DE4356-9814-490A-8932-18E72420930E}',
	'RibFeatureProxy' : '{1F878EE1-06B7-4C7F-9339-920BEFCFE63D}',
	'AutoCADBlockDefinition' : '{C7131135-82E7-45EA-BB86-15DA083F6A04}',
	'CommandCategories' : '{AE2CB260-129A-494C-9F8C-AD8140271E8A}',
	'IRxFileUIEvents' : '{70109AA6-63C1-11D2-B78B-0060B0EC020B}',
	'CurveGraphics' : '{9AB0A7C1-DDEE-400D-B526-287FB2EB6DDD}',
	'BSplineCurveDefinition' : '{30630D32-6807-4D69-8E77-224FD90A21BF}',
	'MiniToolbarTextEditorObject' : '{AAC6E2B5-64B0-440C-A5A2-2AED0D4D7191}',
	'InventorServerObject' : '{EF42229B-CAC3-488D-BCC4-C992FC7795AE}',
	'TranslationContext' : '{6BA435D9-BBD6-11D4-8DE6-0010B541CAA8}',
	'FeatureControlFrames' : '{682CEB3B-365E-4863-B103-BCC368FBA896}',
	'LibrarySketchedSymbolDefinitions' : '{98E6F703-DF38-4C29-85A2-A8266869668E}',
	'SketchedSymbolDefinitionLibraries' : '{A86A47DC-AAFE-4565-9E26-CBEEB2C1C8E5}',
	'FeatureControlFrameRows' : '{4A558EB0-274A-4EF6-90A0-222A720A778E}',
	'FromToExtent' : '{95852FC2-F171-47D3-9435-A478AFF2353E}',
	'MapPointCurves' : '{E405BACE-0EE8-4427-B6BE-82CC11F9CC35}',
	'MapPointCurve' : '{52909F65-AE2E-4997-B3F5-527FE09BF5BE}',
	'ContentTreeViewNode' : '{3DD6B742-71A1-438D-BB71-5CACFA2AACBE}',
	'ContentCenterConfiguration' : '{0B13DE4E-2371-408F-AF1A-F884A9061ED9}',
	'DocumentDescriptorsEnumerator' : '{DBD3CBEE-DBBC-4A71-B122-33A8D1786D20}',
	'ModelDatumIdentifier' : '{EB143431-FB4F-4B4B-BDDA-C21026571456}',
	'SheetFormat' : '{1DF75C0E-591B-45B3-8233-37924B5019DB}',
	'CustomParameterGroup' : '{81342C4A-E898-4566-AA9B-735E88874E56}',
	'IRxEnumComponentDefinitions' : '{5DF86011-6B16-11D3-B794-0060B0F159EF}',
	'RectangularPatternFeature' : '{58B0C13D-27CC-4F06-93FD-0524B69E6578}',
	'CollinearConstraint' : '{8006A076-ECC4-11D4-8DE9-0010B541CAA8}',
	'ThickenFeatureProxy' : '{D07B4A7B-08EE-4CEA-BC85-525E882714BC}',
	'IRxFileAndReferencesOld2' : '{C0E7110B-2136-11D4-8DD0-0010B541CAA8}',
	'DebugInstrumentationObject' : '{F6F33557-6984-11D5-8DF3-0010B541CAA8}',
	'WireDefinitions' : '{29440031-7A2B-4713-907C-DCCE79375669}',
	'MiniToolbarComboBoxSink' : '{5A213EAD-8C62-4EE8-B99A-61A09F2F56E3}',
	'Lights' : '{9F512CF6-D755-4539-A0A5-E346F4B89AE1}',
	'iFeatures' : '{D50258F5-140B-4AE1-BCC7-3CB2438B04E1}',
	'FlatPatternOrientation' : '{830E9463-F267-4A8E-8CE5-8D417295459D}',
	'ComponentOccurrences' : '{5DF86024-6B16-11D3-B794-0060B0F159EF}',
	'PointCloudScans' : '{F20B72F3-D856-45E8-A71A-0753F12D7A10}',
	'VbaApplication' : '{71A0E8AF-8F3E-485D-BB40-7C98163F9C14}',
	'IRxEnumReferencedFileDescriptors' : '{00C8476F-E79F-11D2-B785-0060B0F159EF}',
	'ReferenceKeyEventsSink' : '{4DA70A52-6AE0-4674-95A6-6D7E563CD589}',
	'Trail' : '{0AD2B1BB-3410-4A43-9926-C3849F69FD2F}',
	'RevisionTableStyle' : '{4758367B-5DAF-4CE3-BDF1-189FAD8D6BD2}',
	'ChoiceAssetValue' : '{CC1FB682-EF98-4FE5-9934-143CFB8C65B1}',
	'DesignProjects' : '{131DB1C8-39A0-41F6-B881-9B49050D08DC}',
	'SurfaceGraphicsEdgeList' : '{977D767F-C958-44E8-AB59-8F7267DEBBA1}',
	'CustomConstraint' : '{929723D9-517D-4405-A5B5-263E3B02C6C4}',
	'UnitsOfMeasure' : '{D007B6F9-71BB-48FF-B14C-EE5D633CB0C3}',
	'LeaderNodesEnumerator' : '{26C1C5B1-44AE-4180-8118-EDF2B8CB220B}',
	'ApprenticeDrawingPrintManager' : '{F90311E1-7249-40AF-A597-8AFF681BFA93}',
	'QueryManager' : '{FC6C5BEB-A2CE-4249-8C31-6B0E1E8030A9}',
	'PerpendicularConstraint3DProxy' : '{E2CF70B0-55E2-49E6-81AC-41FD6A6C3DB2}',
	'FileAccessEventsObject' : '{3D67DF18-9BC6-4470-A9E3-C820CB4E821C}',
	'CornerRoundDefinition' : '{21BBAED3-F2FD-4A60-9AE4-7A10A8E2BC2D}',
	'CommandCategory' : '{6B821DA7-B56B-44FC-859F-4DABA658C6E2}',
	'SilhouetteCurveProxy' : '{49F63CD1-212B-4BCB-B43C-5CAF969A2EAC}',
	'SurfaceBodies' : '{5DF860AE-6B16-11D3-B794-0060B0F159EF}',
	'SketchedSymbolDefinitions' : '{A907AED1-A78F-11D5-8DF8-0010B541CAA8}',
	'CosmeticBendFeatureProxy' : '{7958ED54-7E29-490B-9963-BF61E39E98E0}',
	'MidpointConstraint' : '{8006A088-ECC4-11D4-8DE9-0010B541CAA8}',
	'Ribbons' : '{4AA83B95-08F8-4415-9397-4BB5E8103290}',
	'InteractionEventsSink' : '{F1C0EFF2-5035-4DDD-8086-060590676024}',
	'iFeatureTable' : '{5F15A208-8871-42B9-8421-D0555100A7D9}',
	'FilletFullRoundSet' : '{FDBEDE20-57AB-44CC-9A84-31E4D730E85D}',
	'SketchSplineHandle' : '{1236D237-9BAC-4399-8CFB-66CB6B7FD5CA}',
	'FlushConstraintProxy' : '{F36456A4-780C-4CA6-B420-5DBEFFBBCA7D}',
	'PointWorkPointDef' : '{28DD48D1-8D70-11D4-8DDE-0010B541CAA8}',
	'DWGPolyline2DProxy' : '{C5A7AC9D-A15D-46B9-8582-31BD4E8D05CD}',
	'ChangeProcessorSink' : '{5BAB1E1A-F66B-4021-A008-A16E939CA863}',
	'TangentDistanceDimConstraintProxy' : '{C7A68D01-14FA-11D6-8E01-0010B541CAA8}',
	'WireDefinition' : '{9F5047CD-939F-4F15-930C-5C77CEB50BAA}',
	'TwoPlanesWorkAxisDef' : '{28DD48BB-8D70-11D4-8DDE-0010B541CAA8}',
	'HoleTapInfo' : '{F5BFBDBA-35EE-424D-A3AD-8D87B22484CF}',
	'FaceOffsetPreview' : '{FD93BF70-B8C9-4CEE-8AEB-AAC34B534803}',
	'SketchArcs3D' : '{4AF3870E-AB8B-4567-94B5-C1850D292111}',
	'FilletIntermediateRadius' : '{3C16D9FD-5F89-4669-B637-B356887583D1}',
	'GraphicsNormalSet' : '{D8297E9E-DD8B-4C8D-9271-186CAE8E00C1}',
	'Box2d' : '{5DF86063-6B16-11D3-B794-0060B0F159EF}',
	'SoftwareVersion' : '{076C16D1-4994-11D4-9E0F-0010A4C72F07}',
	'RotateAboutLineMoveOperation' : '{1E4085FD-7428-4EA1-B3EF-B2ADDD7F8F5C}',
	'GeneralNote' : '{5C204B1E-BE7E-489A-A842-7A800A7CE348}',
	'ASideDefinition' : '{D092DF11-377A-47AA-92DA-664BE32DDDD4}',
	'BorderDefinition' : '{A907AEB3-A78F-11D5-8DF8-0010B541CAA8}',
	'DSResult' : '{055EC027-CD9B-4983-97E2-2EC073939046}',
	'EllipticalCylinder' : '{FA34A401-F063-11D3-B7A2-0060B0F159EF}',
	'SketchCircles' : '{8006A038-ECC4-11D4-8DE9-0010B541CAA8}',
	'TangentConstraint' : '{0A73D068-AC6B-4B51-8B6D-913B90A77741}',
	'UnfoldFeature' : '{B03877E4-31F6-4B1E-8F38-FCCFD0B0DCAA}',
	'ShellFeatureProxy' : '{EE0E6545-A868-4A60-A152-2AF4C5FB44DC}',
	'DrawingSketches' : '{1644E1D7-9BD5-11D5-8DF7-0010B541CAA8}',
	'ThreePointAngleDimConstraint' : '{C173A07D-012F-11D5-8DEA-0010B541CAA8}',
	'CommandBarList' : '{16EF0082-3213-4E37-AF75-5CB2BF738741}',
	'LightingStyles' : '{A5B827BD-83C7-4CCA-8DCA-06CD10C2237E}',
	'_VbaImplementationAssemblyEvents' : '{E12CF633-9F24-427A-A6F9-D5A7D7BCB314}',
	'SketchArc3D' : '{6129AB00-E4D1-45AD-B3AE-A873BDF452BF}',
	'SplineFitPointConstraintProxy' : '{C7A68CD5-14FA-11D6-8E01-0010B541CAA8}',
	'MiniToolbarValueEditorSink' : '{334FE9E9-7C63-4924-8ADC-42DB57B7B688}',
	'CommandControl' : '{E0519C23-A426-4FA3-BB30-AC5FBEAD137E}',
	'NormalToCurveWorkPlaneDef' : '{EEEC1AAC-5A0C-4405-B0A7-63EBCF82A3A3}',
	'TranslateTranslateConstraint' : '{6D92FD04-C569-4F19-8A54-A83B1CBA7080}',
	'AttributeSets' : '{790B4EB3-7947-4D08-9510-372E93A24CF1}',
	'DockableWindows' : '{FE97EF73-E784-47FB-AA0B-D1891A8F1DF4}',
	'InventorVBAComponent' : '{611EDF7B-009C-4871-B3F9-69E1B4A61C1E}',
	'DrawingBOM' : '{1290504E-696F-4480-8126-04A65C7DA45E}',
	'IRxEnumComponentDocuments' : '{59D3FA3B-ACE0-11D3-B79A-0060B0F159EF}',
	'iFeatureProxy' : '{736ED1B9-7434-4044-B439-EEC1AA84CAAE}',
	'RotateRotateiMateDefinitionProxy' : '{D9E903E5-29EE-4164-8701-2CB853CFEE99}',
	'LoftSectionDimension' : '{3138A370-A692-42B1-8C91-7981A9A0F12C}',
	'IRxComponentDocument' : '{5DF8600C-6B16-11D3-B794-0060B0F159EF}',
	'SurfaceTextureSymbol' : '{7FF4B4DA-DF87-4E58-8727-ADEBA3B6452B}',
	'LumpDefinitions' : '{41473886-B1F1-4E65-9BEB-36F729B6A9F1}',
	'Preparations' : '{1691F301-F2AF-48F4-946F-185CEF9A7EEE}',
	'OffsetDimConstraintProxy' : '{C7A68CF3-14FA-11D6-8E01-0010B541CAA8}',
	'SculptFeatures' : '{EAADC3AE-D599-495E-A56C-FA79AE3E8848}',
	'MidSurfaceFeatureProxy' : '{3F96EC38-31B5-46BD-B45D-CA049B450786}',
	'RefoldFeature' : '{6FF869B7-4D60-4A01-9CCA-9F5F71433014}',
	'IRxCone' : '{5DF86099-6B16-11D3-B794-0060B0F159EF}',
	'BendPartFeatures' : '{3E39E3B3-FA8E-463D-A191-6D7A7CB8E7AE}',
	'EnvironmentBaseHandlerEventsSink' : '{165776AC-95DC-4BD0-8288-BE844390282F}',
	'AssemblySymmetryConstraintProxy' : '{E4FA0888-2179-4CB4-9277-B103A9C40812}',
	'SketchConstraints3DEnumerator' : '{85C83167-947D-46E2-A802-92D529B48E37}',
	'TriadEventsObject' : '{0466D05C-72BF-45E4-A1C6-3FA76AF8812C}',
	'RectangularPatternFeatures' : '{ADA699FB-D9E7-4879-A1A3-86D9F2C6F57F}',
	'FloatAssetValue' : '{5F0359BB-A074-4CD1-98EF-F66DAE4649E9}',
	'RefoldFeatureProxy' : '{325DB945-8B2D-4574-A023-A2864A85896A}',
	'Command' : '{C343ED7B-A129-11D3-B799-0060B0F159EF}',
	'DWGLine' : '{18F5F2F4-26CB-49E9-A105-F83638FEFB3E}',
	'HoleTableRows' : '{73886374-D415-4797-8E3A-A2CA9115D924}',
	'RotateTranslateConstraint' : '{31737D0F-56F3-40B8-8649-C8A5AB945D80}',
	'SketchLineProxy' : '{C7A68CBD-14FA-11D6-8E01-0010B541CAA8}',
	'DimensionStyle' : '{3697D2E9-C4C2-4FF5-A60D-F5EC68EACD27}',
	'DoubleHemDefinition' : '{C534F040-9826-411E-8C6F-4A73C3A998FC}',
	'PartsListRows' : '{A907AE8D-A78F-11D5-8DF8-0010B541CAA8}',
	'DrawingView' : '{206B59B1-22A6-11D4-B7A8-0060B0F159EF}',
	'OffsetSplineDimConstraint' : '{BBCEA345-055B-4625-ABCA-582C6BF7E440}',
	'FaceDefinitions' : '{34EE0736-EB0C-47F4-A4DA-D28AE8D91BFF}',
	'PresentationOptions' : '{6E68C1F1-A6AF-4235-8E86-AB031F7813E3}',
	'SketchOptions' : '{8B657FE9-BF0A-4AED-B1FB-166229D406B3}',
	'PresentationExplodedViews' : '{941D7D22-4C65-4E96-B446-086CD1B94572}',
	'Row' : '{8AF87EC1-B613-43DB-9FF6-E0D489B68DAE}',
	'DerivedPartEntity' : '{FB78F43A-8F10-40F3-8C04-62EEA948C716}',
	'CommandControlsEnumerator' : '{B32BC09F-4DC6-4655-A457-8B7E8934CAAA}',
	'FaceDraftDefinition' : '{8A551127-A520-46FD-A9C4-5ECD271576FC}',
	'ModelingEventsObject' : '{A50B89A5-B9C9-449C-AD62-813F12D80A5D}',
	'AssemblyJoints' : '{EF706A55-28C3-41A6-8D99-EE900BDBCD9D}',
	'LipFeatures' : '{2AD0B878-13E1-4BB0-BDFF-BBAA7DA553DD}',
	'CustomConstraint3D' : '{8E02BFEC-2C95-4685-83B8-E215F98BA844}',
	'LineAndFaceWorkPointDef' : '{28DD48CF-8D70-11D4-8DDE-0010B541CAA8}',
	'SketchEllipticalArc3D' : '{C3CB1896-B26C-4862-8652-5208013D95A7}',
	'TwoPointsWorkAxisDef' : '{28DD48BD-8D70-11D4-8DDE-0010B541CAA8}',
	'OGSRenderItem' : '{429D036C-4F9D-4F72-9F77-AB5789FCC6E9}',
	'DWGSplinesEnumerator' : '{0FEC3515-6F9A-4BFB-BD87-7070E60B0010}',
	'AliasFreeformFeature' : '{49A9C1BC-D718-4DCB-AAD8-8FB4285EFA45}',
	'LinearGeneralDimension' : '{B0E8CB6F-9451-4AFC-B8D3-A157ACDCBB0F}',
	'FilesEnumerator' : '{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}',
	'ClientBrowserNodeDefinitionSink' : '{B142CBF7-AE52-4AC4-ADAB-7A36A2A9A834}',
	'SketchSplineHandle3DProxy' : '{7C693E2E-D4D3-433A-A90F-112E3C52E543}',
	'ClientFeatures' : '{68AF2955-0901-433D-B7C3-D91D637DD21C}',
	'SketchEllipses3D' : '{7A7BD889-E944-41FC-A34F-474465F0894E}',
	'Attribute' : '{BC3487BB-F349-4A6C-9F72-D8C62CBADE6B}',
	'PrintManager' : '{69190E26-316F-47BD-AE75-8B64641C18C8}',
	'RibFeatures' : '{436A627D-919B-4B92-B242-268F7266D8A1}',
	'RadiusDimConstraint3DProxy' : '{8DD13222-E35F-4EEA-93BA-87F73A069481}',
	'ProfileEntity' : '{B5461255-09AA-11D5-8DEC-0010B541CAA8}',
	'GeometricConstraints3D' : '{85A24FF2-F0E9-4BC4-9A69-34F8C683B41A}',
	'FoldFeature' : '{4594DFB7-06DB-4707-9F10-B42F740EE37D}',
	'BoundaryPatchFeatures' : '{97D6B280-1D62-48E6-B4B9-007F25F7A3A5}',
	'ClientFeatureElement' : '{BA8A81FD-71F7-4BE4-A009-1CC6731723FD}',
	'TorusCenterPointWorkPointDef' : '{E205D028-CE6C-4BE5-AE33-AB6F9770D869}',
	'FaceFeature' : '{600E3CEE-1600-4999-ACE4-7CED6483BECE}',
	'MidSurfaceFeature' : '{247E2AC0-3948-4DD9-88A1-0AC87A794BC7}',
	'IRxEnumEdgeLoops' : '{5DF86073-6B16-11D3-B794-0060B0F159EF}',
	'ImportedModelEntities' : '{FC6CACA3-208B-40AD-8B3A-0949B6CBBD3A}',
	'CutAcrossBendsExtent' : '{061C46D9-4A71-40EB-9DDC-4D425A6ABE3E}',
	'SketchEllipses' : '{8006A036-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchFixedSpline' : '{DCEF44A1-7A80-4A0A-937C-A349AF8A9233}',
	'FaceShellDefinition' : '{BB41DDFD-351A-4AC7-9294-0FF1D2710C07}',
	'FileManagerEventsSink' : '{CA8E18AF-5EA2-4A45-BA43-FF3914C5C200}',
	'BIMElectricalConnectorDefinition' : '{1F222D21-CBB5-4FC4-A6CF-0387224A7F2C}',
	'iFeatureDefinition' : '{358B0B8E-D2C7-4D76-AAC6-33009864424E}',
	'ApplicationUtilities' : '{DB93184E-4A45-4C38-96B4-42051502413D}',
	'FlatPattern' : '{A7E07EA5-369D-11D6-8E02-0010B541CAA8}',
	'ModelDatumIdentifierDefinition' : '{0B87CDBE-3271-46A7-9C95-259667C9FFCF}',
	'PointCloudScan' : '{A962939B-0A11-490F-AC66-DC0FDAA3DD75}',
	'CurveAndEntityWorkPointDef' : '{FFFA6714-4FA1-4191-B746-8F0493DF7C06}',
	'InventorVBAProjects' : '{EEB0116A-7B74-4A9C-B2FF-96BC31812249}',
	'ButtonDefinitionSink' : '{9B5D2EC6-A4BD-4B3A-8A34-069EE52B009D}',
	'IRxUnitVector' : '{CB69F161-558E-11D3-B793-0060B0F159EF}',
	'DWGPolylines2DEnumerator' : '{8C2B0FE6-3B3F-4897-BD44-806DA59E436A}',
	'SinglePointRipTypeDef' : '{E8320E6D-E219-4F7C-954C-484A94137FD1}',
	'AssetLibraries' : '{DF8C6267-186F-4A45-8BD4-2545484B102E}',
	'DirectEditOperation' : '{86EF3B55-8CEB-45E8-9C9C-5F4430679B7C}',
	'BrowserFoldersEnumerator' : '{A9427B73-D39C-4DA3-9330-3CEB71ECA2B9}',
	'BoundaryPatchFeatureProxy' : '{6F18AA5B-56B7-4880-90A5-190322278B8D}',
	'Ribbon' : '{3AB23287-16A5-4B3B-964B-00C27869CD23}',
	'ConstraintLimits' : '{8112A2AA-0017-4029-81A5-9C18F5E37E92}',
	'IRxFacetsOld' : '{CB69F159-558E-11D3-B793-0060B0F159EF}',
	'MiniToolbarComboBoxObject' : '{F7844415-30E0-4507-8BC0-F8AF990B3B38}',
	'DerivedAssemblyOccurrences' : '{DEB206F5-3467-4860-869E-97479BA38D36}',
	'DerivedPartTransformDef' : '{11C8C1C5-74AB-415F-AE6B-F358CE0FDA4C}',
	'AliasFreeformFeatureProxy' : '{8DE224FA-1DA2-4B05-BE2B-3E7FB6361FC2}',
	'Asset' : '{766A9447-A604-43C8-9393-2D2709837D1E}',
	'LoftRail' : '{02466B5A-9C4B-48C4-BFA0-5590DB014745}',
	'ExpressionLimits' : '{F8CA1F67-2904-4C91-88F3-F79683227118}',
	'ComponentOccurrenceProxy' : '{46AEA719-4302-11D4-B7AB-0060B0F159EF}',
	'UserParameters' : '{2FF370FA-BB1C-4C92-BB10-06D94CC8F8F3}',
	'IRxLine2d' : '{CB69F164-558E-11D3-B793-0060B0F159EF}',
	'SketchConstraintsEnumerator' : '{8006A026-ECC4-11D4-8DE9-0010B541CAA8}',
	'FaceDraftFeatures' : '{C77D9639-C58A-4E5A-BAE0-14966E37DDEE}',
	'ReferenceFeatures' : '{347FB32C-79ED-4A5B-89B1-7B14FF6A9CA8}',
	'CombineFeatureProxy' : '{665564D4-83B4-4B86-A365-CAA6B0EBA6C2}',
	'DocumentSubType' : '{D3EDB5BC-7B47-42B9-9D77-F3A2676EC15B}',
	'UserInterfaceManager' : '{3AF77BAF-EECD-4301-823D-9B604FE5C176}',
	'ModelDatumIdentifiers' : '{498E2A5A-76DD-4059-BB54-300D026EC79D}',
	'RibbonTab' : '{734FDACC-45FD-487A-AC60-02CE0522FF00}',
	'DSServer' : '{457D2D49-6354-461E-AE0F-2C42B371D313}',
	'SketchImage' : '{C00FE3F4-2D75-4409-93FB-9B72913C073C}',
	'CollinearConstraint3DProxy' : '{4FDD2BD0-33C6-4EB0-90CE-4EEA2B181738}',
	'SketchConstraintSettings' : '{541E7231-CD23-4986-B26D-4C2B4F1E2DBE}',
	'Circle2d' : '{49CB4BB6-872A-11D3-8524-0060B0F0B5B7}',
	'DerivedAssemblyComponentProxy' : '{D2E7C9A2-CB9A-4619-B0AA-B7BA2870CDEE}',
	'OffsetSplineDimConstraintProxy' : '{B8E1A8FF-EE38-49CD-BC33-FBA4E8E6073C}',
	'AngleiMateDefinition' : '{F5C82F4B-9B32-488E-920A-31F065B1AD77}',
	'RotateRotateiMateDefinition' : '{6025C779-5DFB-4B1D-B2C9-E7CDD5D18B5F}',
	'LineLengthDimConstraint3DProxy' : '{2F041963-4B68-415F-BE07-F1FB6C6342A3}',
	'_SweepDefinition' : '{3D70E84F-AC86-4734-8A36-1672FE750893}',
	'RipFeatures' : '{8A0202C7-6ADF-454C-AF47-09E3027E8E7C}',
	'RevisionTableStylesEnumerator' : '{50C3C4B3-5029-44E8-BF12-C1D09530CCF5}',
	'SketchedSymbols' : '{A907AED9-A78F-11D5-8DF8-0010B541CAA8}',
	'DrawingSketch' : '{1644E1D5-9BD5-11D5-8DF7-0010B541CAA8}',
	'ContentCenterOptions' : '{650A171B-40E1-4C3B-B55E-DFB3D31C2CB8}',
	'ErrorManager' : '{7B550B22-4519-43D2-9A9E-5EC0D9FFCCD6}',
	'ThreadFeatureProxy' : '{DA05EA7F-D509-4D65-AA86-AB596110425C}',
	'CustomPropertyFormat' : '{B2EC7987-2BDE-47F6-8EE7-534C7B854B2B}',
	'Camera' : '{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}',
	'VerticalAlignConstraintProxy' : '{C7A68CEF-14FA-11D6-8E01-0010B541CAA8}',
	'SketchControlPointSplines3D' : '{745A04C4-8445-412A-AFA7-33E778DA3059}',
	'RestFeatureProxy' : '{1B63BB78-7EC2-4D21-A312-A867DCF54110}',
	'EdgeWidthExtent' : '{E59EEDF7-48F4-4328-AF62-EBBE19BD09C1}',
	'DerivedAliasComponent' : '{61B9A367-8CCB-4868-A573-CCE62C5C35B6}',
	'WidthOffsetWidthExtent' : '{91578449-A1E5-4865-BF53-D297549308B0}',
	'Line' : '{CB69F178-558E-11D3-B793-0060B0F159EF}',
	'PlaneAndOffsetWorkPlaneDef' : '{2C167867-83FF-11D4-8DDB-0010B541CAA8}',
	'Light' : '{755B3C6B-3A92-4702-96AC-686382A91278}',
	'SurfaceTextureJISDefinition' : '{78B82408-F848-4E5B-A657-67059CC86235}',
	'DriveSettingsObject' : '{F8FEB6D6-1D1A-4472-9429-1FF06A76DB9E}',
	'ChangeDefinitionObject' : '{4F8D5D47-63F7-4690-A06D-54D7311A2566}',
	'DimensionConstraint' : '{B5461259-09AA-11D5-8DEC-0010B541CAA8}',
	'PartComponentDefinition' : '{DA33F1A3-7C3F-11D3-B794-0060B0F159EF}',
	'TextureCoordinateSet' : '{D96060F8-0E08-4E73-8D5E-37F506A1A738}',
	'IRxProperty' : '{73F35CCF-ED6E-11D2-B785-0060B0F159EF}',
	'AnnotationPlaneDefinition' : '{740E1B50-7EC5-4C4E-B94B-CCEB4FB5C489}',
	'EdgeCollection' : '{8DC730F1-A15F-4547-A279-69B7A9FAE657}',
	'DiameterDimConstraintProxy' : '{C7A68CFB-14FA-11D6-8E01-0010B541CAA8}',
	'DocumentDescriptor' : '{D755CFCA-9E02-4A08-AFE8-7178E818C763}',
	'DWGSpline' : '{A19EC228-CE1D-4B2D-BE30-584AF42A18AA}',
	'CornerFeature' : '{7DBA9100-AFA9-407A-A91C-A9CC7A079565}',
	'SaveOptions' : '{A6EC8B79-931A-409E-90CE-3EE28CB9F9F4}',
	'DWGEllipticalArcsEnumerator' : '{E825D13E-DAE3-4CA1-A275-5C0A62A67E6B}',
	'MouseEventsObject' : '{70B77812-4E3A-4499-8F8D-6AB6C6BDC5A5}',
	'IRxEnumSurfaceBodies' : '{5DF86070-6B16-11D3-B794-0060B0F159EF}',
	'PartsLists' : '{A907AE85-A78F-11D5-8DF8-0010B541CAA8}',
	'DWGPolyline3DProxy' : '{078D1300-9A94-4644-BB80-BFD3B4600F3A}',
	'SketchControlPointSplineProxy' : '{E3757DA9-1C29-477B-838A-B84E896410B2}',
	'FaceOffsetFeatureProxy' : '{E139EE45-18F4-404E-972E-08C6008BD225}',
	'SweepFeatureProxy' : '{2A5668A8-5EA5-45AE-B3DB-A4C7BD2F7E9D}',
	'MassProperties' : '{2FA1D3CF-EAFF-4D47-9E13-E5B074C1565C}',
	'HemFeature' : '{D9AB7AE5-6A67-4165-9E0B-0F008C9135B0}',
	'NonParametricBaseFeature' : '{1D09051E-D674-4ABE-BEC9-5A58016455B1}',
	'CoilFeatures' : '{2C30965F-FD0D-4D6E-AC98-797F2F0E2DEB}',
	'ClientGraphicsCollection' : '{66829BB6-656B-431C-BF5C-0BF53DBA225D}',
	'InventorVBAMember' : '{FBC2D851-EC7F-4D70-B13C-98B57B785E97}',
	'ReplaceFaceFeatureProxy' : '{63FB8F95-6B59-4039-B9E1-F6D74E1B3716}',
	'BalloonTipObject' : '{BDAFC08A-5CAC-4E5A-B715-F2BCAFFD5282}',
	'DesignProjectManager' : '{4A60CB5E-1EE8-4180-A801-194704F3021E}',
	'SketchLine' : '{8006A016-ECC4-11D4-8DE9-0010B541CAA8}',
	'DrawingEventsObject' : '{27716230-E826-46E8-90FB-923D38D6F6F8}',
	'LevelOfDetailRepresentations' : '{B7B652AD-7411-429D-92AC-663F9183F7F6}',
	'ReferencedFileDescriptor' : '{9E0BA9CA-E916-11D2-B785-0060B0F159EF}',
	'iAssemblyFactory' : '{B76D6529-D84D-4A66-8215-58B6A32D56A9}',
	'GraphicsImageSet' : '{FC23373B-FA59-43C7-BD1B-2618DFA1C8C0}',
	'TextureAssetValue' : '{AD623DC3-5354-483D-99A1-C7ADDB0C06CF}',
	'IRxSurfaceEvaluator' : '{5DF8606E-6B16-11D3-B794-0060B0F159EF}',
	'FeaturePatternElements' : '{82B32371-11B8-467E-B57E-0112DDD4BB65}',
	'SketchEllipticalArcs3D' : '{08C74C78-5F8D-40B3-9D57-4507D5CEA79C}',
	'SketchEllipticalArcs' : '{C173A089-012F-11D5-8DEA-0010B541CAA8}',
	'DataIO' : '{FBCADB33-9CBE-11D3-B799-0060B0F159EF}',
	'ClientFeature' : '{BB91C845-BD7E-4470-948F-C5A069B21BBC}',
	'Profiles3D' : '{B1340A33-EB0D-4609-BA1E-B98A3D173794}',
	'HoleTableCell' : '{E232F1FF-D6C3-421F-B650-AFAC768279D5}',
	'DWGPolylineProxy' : '{6755F53A-DF74-4D7A-AB08-340C5AAD6F5C}',
	'HoleTableColumns' : '{A80294E5-6638-47F4-948A-A31A9F9CBC36}',
	'PointAndPlaneDistanceDimConstraint3D' : '{39930637-A840-4819-AB86-EFE9CCB21BD1}',
	'DerivedPartComponentProxy' : '{1B986C9A-B329-45B0-B682-95F04FF16E87}',
	'LoftSectionDimensions' : '{F8FBACE4-75A7-4493-B2D8-492AC937F3E5}',
	'CornerDefinition' : '{F69024F9-970E-4223-82DD-6B4F0E3AF57F}',
	'IRxVector2d' : '{CB69F160-558E-11D3-B793-0060B0F159EF}',
	'DerivedAssemblyOccurrence' : '{4DEAC0A5-E998-4958-8344-D866385CECF2}',
	'CentroidWorkPointDef' : '{4286D377-DC30-4195-9A04-E2C5A29AA72A}',
	'TextStyles' : '{A907AEBF-A78F-11D5-8DF8-0010B541CAA8}',
	'IRxFileAndReferences' : '{D4606260-75D8-48EA-A3C3-A971E2384118}',
	'SymmetryConstraintProxy' : '{C7A68CE9-14FA-11D6-8E01-0010B541CAA8}',
	'GraphicsPreferences' : '{92353969-0350-11D3-B787-0060B0F159EF}',
	'GraphicsIndexSet' : '{9D2A8D7D-D599-4D54-BDE0-586E5E18880D}',
	'LanguageTools' : '{0420658E-CCD1-4100-BFA1-AD78AA655551}',
	'DrawingOptions' : '{221277C1-7963-4539-B2E5-E7E16D3C75AA}',
	'FeatureGraphics' : '{6757C085-699B-474B-9566-61221A64A09F}',
	'HelpEventsSink' : '{39E63B3F-3A40-4735-9C8F-012AFB75F087}',
	'SculptFeatureProxy' : '{78F10980-2892-46CD-8F0E-B709A4835B9B}',
	'SketchedSymbol' : '{A907AED5-A78F-11D5-8DF8-0010B541CAA8}',
	'HoleTag' : '{CA779A92-76AD-4CD4-ACDB-7F06D73A089E}',
	'BOMRow' : '{148682B7-6B44-4FF0-8C10-AB21D276602E}',
	'ButtonDefinitionHandlerObject' : '{93224595-EAF4-4AE2-9604-16A2854AFF4B}',
	'RibbonTabs' : '{1CE97D79-6535-4D0F-9A51-57734766BEDC}',
	'AssetValue' : '{C6E1E6AB-897D-4CDD-A486-4ABAA04FC9B9}',
	'IRxComponentOccurrenceOld' : '{5DF8600F-6B16-11D3-B794-0060B0F159EF}',
	'SketchControlPointSpline' : '{D5F8CF99-AF1F-4089-A638-F6889762C1D6}',
	'iPartMember' : '{2DB692B1-9CA2-40CA-AD6B-D1250C063724}',
	'MiniToolbarDropdownObject' : '{7DF3C716-A1C7-4D3F-83C0-5D06A3D7F05C}',
	'OccurrencePattern' : '{09A5CE88-D529-499E-82EF-246D8DC4F5B3}',
	'DirectEditRotateOperation' : '{3913A482-D11A-4B13-A6B1-C1310F935B09}',
	'SketchFixedSplines' : '{6359FE67-0814-4847-9F33-72E0BB9EB688}',
	'SculptSurface' : '{65A5B1BC-9F61-4F5D-A113-66EDC3DAAAC0}',
	'ContentCenterDialogEventsObject' : '{F55C4A2E-FEBB-4EEA-872D-C54B481B0948}',
	'OrientedBox' : '{556DCFA3-BD63-4B13-9C12-D99113AEAEFB}',
	'Layer' : '{9FEBA8BF-6BB5-421E-82DE-F1C4A1639C70}',
	'iFeatureSketchPlaneInput' : '{77244784-A1C1-429E-A61F-E6E480B8DFEF}',
	'BendNotes' : '{206AFE1A-FAFA-4DAF-A569-1AF60672D63B}',
	'LineStripGraphics' : '{D2666468-C11D-42F3-AB1E-6E590C5AA182}',
	'ModelFeatureControlFrameDefinition' : '{CD675FA9-2F1B-4574-B287-C0C601CCC1B1}',
	'BIMConnectorDefinition' : '{E41CA526-545A-4782-A383-C44FC7523552}',
	'MaterialAsset' : '{A095B86B-84EF-4364-888E-1F6F03EAA73F}',
	'AutoCADBlockDefinitions' : '{FC290B65-544A-4F65-B812-092CB93AA421}',
	'Balloon' : '{A5F6343C-7FE9-431E-BF12-A7308A57CE91}',
	'ObjectDefaultsStyle' : '{E8528224-258B-471F-81E3-1F276425BC39}',
	'GroundPlaneSettings' : '{A12C6DFA-6381-41A2-9037-13AFE5B1EFBD}',
	'DesignViewRepresentations' : '{C6A2B48C-DBBC-4BA9-A98B-6EB63FB78AE4}',
	'TwoLineAngleDimConstraint3DProxy' : '{407A9D14-6E3A-4F39-9AD6-CDD8873B9FCB}',
	'Parameter' : '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}',
	'DesignProject' : '{9A14B139-7101-40B1-BD92-B3F9870DC7F0}',
	'Material' : '{57CFD4EC-1776-48D3-B5C4-7B6E015D0541}',
	'WorkAxis' : '{28DD48B7-8D70-11D4-8DDE-0010B541CAA8}',
	'iFeatureTableCell' : '{ABC49BF6-3E83-45A6-AF98-059245620FF4}',
	'TextureMaps' : '{8BC9C1AA-4238-4112-A5FC-15F3765E5336}',
	'DiameterDimConstraint' : '{C173A07F-012F-11D5-8DEA-0010B541CAA8}',
	'DSSettings' : '{7771DA59-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DistanceAndAngleChamferDef' : '{8F25CE45-DF1F-4669-BAA8-E2042ED68811}',
	'SketchEllipticalArcProxy' : '{C7A68CC7-14FA-11D6-8E01-0010B541CAA8}',
	'AssemblyWorkPointDef' : '{8E3A45D9-4432-4408-B261-12E725F97A5D}',
	'GroundConstraintProxy' : '{C7A68CDD-14FA-11D6-8E01-0010B541CAA8}',
	'DirectEditOperationProxy' : '{8A4D2830-7D4A-49E5-99BC-3E6C760463E7}',
	'ThickenFeature' : '{97E8752C-E818-41FF-8C13-D10B6FBC522F}',
	'FeaturePatternElementProxy' : '{B4298554-2144-4054-A4EA-81888D6F6997}',
	'SweepFeatures' : '{CADFFDB1-11E6-4684-A35E-7EE2064AA46C}',
	'Matrix2d' : '{DA33F19F-7C3F-11D3-B794-0060B0F159EF}',
	'BIMExchangeServer' : '{6B73769B-1859-4202-87D4-2E508FC9434C}',
	'MeasureEventsSink' : '{3C75ADFE-18C0-42BF-A83D-D0E539BD1F7D}',
	'TangentiMateDefinition' : '{C78E43C1-DB92-414A-9B45-352DFAC434E4}',
	'Point' : '{CB69F172-558E-11D3-B793-0060B0F159EF}',
	'HelpEventsObject' : '{2A922EEA-AE03-4C69-9986-D79D5A5A24DA}',
	'BIMConnectorLinks' : '{99C8344C-60E3-46CA-A32D-1EF2010EB01D}',
	'SketchArc3DProxy' : '{856FF591-895A-4A94-9FB1-16F5265C91C8}',
	'FreeMoveDefinition' : '{D26E4888-3FA1-4A45-94E5-AA1A3A41B4AE}',
	'FaceShells' : '{5DF86091-6B16-11D3-B794-0060B0F159EF}',
	'SketchEntity3D' : '{FD1878BB-56AD-44CD-9186-11BC84E584A4}',
	'RotateTranslateConstraintProxy' : '{9DFB56E1-F6A4-4D2A-99CE-47CBB8A3145D}',
	'FaceOffsetDefinition' : '{20C6159F-9ACD-4AA6-B616-1CC57A6F91CA}',
	'RigidBodyGroups' : '{CBE24DE3-529E-4039-BFDF-D014844691F0}',
	'SculptFeature' : '{7E2A1EB5-F770-45BD-8DC5-8FEE60664D9F}',
	'DWGEntity' : '{6B46D5EC-57DE-414D-8ACC-EF1E7C6C1AAF}',
	'ReferencedOLEFileDescriptors' : '{9CAF98A0-33EA-11D3-B78F-0060B0F159EF}',
	'IntegerAssetValue' : '{48D3D9AD-F3F0-41E8-B4D8-6DA2533CCFC9}',
	'DrawingCurve' : '{1C98EA42-27FC-4BFA-84E4-D29C7A11F889}',
	'_SegPerformanceMonitor' : '{AE621339-6CA8-486C-BF06-E683D2EE3A8E}',
	'BSplineCurve2d' : '{49CB4BBA-872A-11D3-8524-0060B0F0B5B7}',
	'TextBoxConstraint' : '{037C3FDB-8A3C-443F-8CF6-993D3295335C}',
	'CoreCavityFeature' : '{8C1243A8-F557-4626-A5F1-8B9F988B2EFC}',
	'FilletSetback' : '{325CFE17-8D9E-4977-A3B3-97AC9D827CD9}',
	'Sketch3DProxy' : '{FA39B171-CAA5-4FB2-94D0-4E0DF357D13E}',
	'DimensionConstraints' : '{C173A075-012F-11D5-8DEA-0010B541CAA8}',
	'DirectEditDeleteOperationProxy' : '{EAFC6907-44B0-482F-A30F-A46E227A57BC}',
	'FlatPatternFeatures' : '{75A1BC5F-78FC-4E62-99C7-623813E36C43}',
	'BalloonTips' : '{176AA199-DDEA-4CA9-B7EC-0437918DF800}',
	'ProjectedCutProxy' : '{1F3DB03A-352E-44EA-807B-8D3C4FCF855C}',
	'FlushiMateDefinitionProxy' : '{2A87493C-AFCD-42D8-A4AE-8385513E63E9}',
	'iFeature' : '{98675AD1-A109-43DE-A7D7-1612BC503E0E}',
	'BrowserPaneObject' : '{21F02BD0-F849-49E1-A1EC-A04A8F49AE05}',
	'AssetCategory' : '{25E59F53-ADFB-4B1B-8CF4-C8EAE80CA85F}',
	'AngularModelDimensions' : '{29C4F94E-2656-4727-8510-2B0DAF6FCEFE}',
	'IRxStrokesOld' : '{CB69F15A-558E-11D3-B793-0060B0F159EF}',
	'DirectEditMoveOperationProxy' : '{3B833858-7410-47C9-BCAD-F3BE5DEA191D}',
	'Rows' : '{2022FEE8-01DA-481F-A515-D2D89C787EA8}',
	'HorizontalAlignConstraint' : '{8006A086-ECC4-11D4-8DE9-0010B541CAA8}',
	'ImportedDWGComponentProxy' : '{B1EECF0D-991E-44FD-8244-61AB5E826B35}',
	'IRxStrokes' : '{DAEA25A5-513E-41CA-BB8F-8E88B507C52E}',
	'Weld' : '{FFC0E573-23C5-4DB1-A1DC-F6B12EA2907B}',
	'MateiMateDefinition' : '{425EAA71-D590-4893-AFAB-012380A7CEBA}',
	'CornerRoundEdgeSet' : '{289220CD-E245-473D-B626-114D97F9EDCB}',
	'IRxBSplineCurve' : '{5DF86032-6B16-11D3-B794-0060B0F159EF}',
	'OccurrencePatternElement' : '{6ABB8219-4962-11D5-8DEE-0010B541CAA8}',
	'ClientNodeResources' : '{9C8B2909-8C33-481E-8CF5-9C269B4E54DC}',
	'OccurrencePatterns' : '{1112CDE3-CD39-4004-8E74-0C019C73F380}',
	'SketchEquationCurves3D' : '{01BAC9F1-F900-4E57-9FDB-F12232AEC9D2}',
	'HemFeatures' : '{DF566DD8-E3A3-45E3-844D-78F8C072ECDC}',
	'MemberManager' : '{2B24FE45-C9E2-4590-BA7E-F7DB0E5A683F}',
	'FilletConstantRadiusEdgeSet' : '{9374403D-49B0-4DA3-A4CA-55DDAB40D8E1}',
	'DimensionStylesEnumerator' : '{0134748C-7F24-467B-9DF2-6647677B125F}',
	'ClientNodeResource' : '{9ACFBDEF-B81B-4B4D-8EA6-8453F1DD6285}',
	'NameValueMap' : '{6BA435DD-BBD6-11D4-8DE6-0010B541CAA8}',
	'ConcentricConstraint3D' : '{EF118F14-C2D2-4DF4-910A-3438FBEC2817}',
	'AngleConstraint' : '{9048CE40-F6A5-422D-A816-CBE5E03B28D6}',
	'ReferenceFeaturesEnumerator' : '{BEBB7A1A-2E50-4C62-A4E1-64B2E9A18AE6}',
	'GraphicsNodeProxy' : '{C6DE930F-09D7-487F-A4C9-401AA8B19879}',
	'ModelHoleThreadNote' : '{2BAE3F08-F0AE-4B03-A432-E3A3C22408F6}',
	'ShellThicknessFaceSet' : '{0F8F253B-5ED8-4AE0-9C62-3DEFDCCD0BC4}',
	'ModelFeatureControlFrame' : '{F2948971-943D-4CBB-88B0-20E0B48B8573}',
	'FeatureControlFrameRow' : '{7CD6C780-663E-4187-8D35-D132C99F6918}',
	'Bend' : '{AE99EE3F-A9E9-498C-AE33-C919105745F4}',
	'IntentConfiguration' : '{CF66D521-D40D-477C-A686-D2D5A614D323}',
	'EdgeLoopProxy' : '{46AEA72C-4302-11D4-B7AB-0060B0F159EF}',
	'EdgeLoopDefinition' : '{F1779764-61F6-4C25-8B5D-6A6F41B57709}',
	'EdgeLoops' : '{5DF86093-6B16-11D3-B794-0060B0F159EF}',
	'PlanarSketchProxy' : '{C7A68CBB-14FA-11D6-8E01-0010B541CAA8}',
	'PathAndSectionTwistsSweepDef' : '{F369E470-65BE-4BB7-B3E8-AB32C9F6CC22}',
	'ParallelConstraint3DProxy' : '{3163F506-342D-4D68-8AB1-39C306DCA6F6}',
	'Document' : '{70109AA1-63C1-11D2-B78B-0060B0EC020B}',
	'TwoLinesWorkPlaneDef' : '{46785C41-7F4A-11D4-8DDB-0010B541CAA8}',
	'BendOptions' : '{CA6A960F-9215-4EF3-AFFC-A90D277BEF4F}',
	'ColorScheme' : '{917CE8E7-741A-48A3-8E15-89A6DA053C40}',
	'PositionalRepresentation' : '{DD22F707-6FC9-481B-A3FD-44FDA2D695A2}',
	'IRxSphere' : '{5DF8609A-6B16-11D3-B794-0060B0F159EF}',
	'FreeDragMoveOperation' : '{279EB42E-C733-4AA9-BFA8-2A8FCF2B2A4D}',
	'SketchControlPointSpline3D' : '{A4126F98-E952-4997-BD2D-209D4788F70F}',
	'DrawingCurveSegments' : '{D05367DD-3A18-47DC-A618-7550582CEEDA}',
	'SketchSettings' : '{02BCE85C-478B-4A66-8668-6579602A0EB6}',
	'IPersist' : '{0000010C-0000-0000-C000-000000000046}',
	'ModelDimensions' : '{7AD96A84-A539-4220-B9AD-7A2854D518B8}',
	'OrdinateDimensionsEnumerator' : '{A3788117-9A81-4D70-A8C8-C3FF3895E3D2}',
	'FeatureControlFrameStylesEnumerator' : '{852C83B9-26EC-4FDA-89D5-E031523AEE01}',
	'FilletRadiusEdgeSet' : '{A40068C9-5681-4B3D-961A-1C6360B20BFE}',
	'OffsetConstraint' : '{8006A07C-ECC4-11D4-8DE9-0010B541CAA8}',
	'LevelOfDetailRepresentation' : '{F24F9821-0EE5-4157-A555-45B97DE14D6D}',
	'FilletConstantRadiusFaceSet' : '{237CB3F2-314E-4211-92DC-D69C15BF1B64}',
	'DerivedPartCoordinateSystemDef' : '{E9AFE0F2-46D5-4022-B668-F0AE494C48B1}',
	'PartsListColumn' : '{A907AE8B-A78F-11D5-8DF8-0010B541CAA8}',
	'RevolvedFaceWorkAxisDef' : '{28DD48BF-8D70-11D4-8DDE-0010B541CAA8}',
	'ProgressBarObject' : '{3D157428-294A-4446-A33D-6BEA664F61D7}',
	'DWGArcsEnumerator' : '{F5CC3DD7-BC15-476C-853B-3E63BA66A29B}',
	'RadialMarkingMenus' : '{228EA2B9-974A-48DF-8E17-7EAE50A79AFD}',
	'IStream' : '{0000000C-0000-0000-C000-000000000046}',
	'SketchBlockDefinitionsEnumerator' : '{14A842C0-8BD2-431B-B1DA-A487A6E35B18}',
	'UserInputEventsSink' : '{711F30CD-A00B-4015-93A8-397EC8F5A284}',
	'IRxPoint' : '{CB69F15D-558E-11D3-B793-0060B0F159EF}',
	'ContentTableColumn' : '{20C36669-DC84-413C-84A7-4D0983BAD319}',
	'PanelBarObject' : '{C2FEB1BC-115B-443B-A18C-F88B2FCBB7BA}',
	'DragContext' : '{FA403DAE-32E0-4C17-BB7C-CD3626A9BFA9}',
	'FromToWidthExtent' : '{78E9A7D5-C2AD-48C2-85D5-3A0A58D2FDA5}',
	'CornerFeatureProxy' : '{64868FC5-AFD9-4602-A5D5-02D93B65BB05}',
	'SketchArcs' : '{8006A032-ECC4-11D4-8DE9-0010B541CAA8}',
	'DriveConstraintSettingsObject' : '{C3F06C8B-B0EA-4EC3-9922-1657009774D3}',
	'TranslatorAddIn' : '{6ECCBC87-A50D-11D4-8DE4-0010B541CAA8}',
	'BreakOperation' : '{ABCACDBB-5EAF-4AF5-86A0-FB2DB0502D5D}',
	'ImportedComponent' : '{239475B6-6DCA-4683-B410-A5788BF2077B}',
	'PunchToolFeatureProxy' : '{B716CEF3-32C9-4A9A-911D-0D1CF52A74C9}',
	'TwoLinesWorkPointDef' : '{28DD48CD-8D70-11D4-8DDE-0010B541CAA8}',
	'ObjectDefaultsStylesEnumerator' : '{062F6086-60DC-4550-93C5-A9B8CEA89ADB}',
	'PropertySets' : '{73F35CC8-ED6E-11D2-B785-0060B0F159EF}',
	'Vector' : '{CB69F174-558E-11D3-B793-0060B0F159EF}',
	'iAssemblyTableColumns' : '{C7AF47E6-3FDE-469F-B258-85FE0390E7DA}',
	'EdgeLoopDefinitions' : '{9A9B007B-18C5-4C27-BBA5-1D8F7E9B9A30}',
	'ControlDefinitionEventsSink' : '{AB5EF2D1-EAEB-4A4A-A86B-24BF0F2111BD}',
	'DrawingCurvesEnumerator' : '{E49C9290-6D71-4C14-8B15-3595306A49D6}',
	'LinePlaneAndAngleWorkPlaneDef' : '{46785C45-7F4A-11D4-8DDB-0010B541CAA8}',
	'SketchOffsetSplines' : '{16372AAE-1133-4C4C-9A48-D9305D8358F3}',
	'LoftedFlangeDefinition' : '{C16DE191-DEEC-449E-BEF1-1F1220233FB3}',
	'FeatureBasedOccurrencePattern' : '{773C0E8F-2C4C-4871-93F7-AF9483171461}',
	'CornerChamferFeatures' : '{AB61EB61-7785-4854-9498-8210B3DA80B2}',
	'AssetTexture' : '{3E0ED07A-F5ED-46BF-8903-EBC1B409A270}',
	'TangentSketchConstraint' : '{8006A090-ECC4-11D4-8DE9-0010B541CAA8}',
	'RotateTranslateiMateDefinitionProxy' : '{0BD0BDD4-2716-42A0-B258-09F689CFDFB5}',
	'ParallelConstraintProxy' : '{C7A68CE5-14FA-11D6-8E01-0010B541CAA8}',
	'ChangeManager' : '{D70C53E3-58A6-48CA-95D2-AF6F4AAD04EA}',
	'SketchEntity' : '{B546124D-09AA-11D5-8DEC-0010B541CAA8}',
	'CornerRoundFeature' : '{3822A30C-5DAB-449B-8AAA-BDA9DEF3FBF5}',
	'Box' : '{5DF86062-6B16-11D3-B794-0060B0F159EF}',
	'DSLoads' : '{7771DA53-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'CircularPatternFeature' : '{7BB0E824-4852-4F1B-B43C-7F729A3D7EB8}',
	'Face' : '{5DF8608B-6B16-11D3-B794-0060B0F159EF}',
	'FaceDraftFeatureProxy' : '{5874F2D8-29C2-4D48-91C2-BB239564CF26}',
	'AngularModelDimensionDefinition' : '{A765255E-0264-4316-9F81-F5B051281001}',
	'SurfaceGraphicsFaceList' : '{0B8D52D2-8147-4407-B2E3-D982ED775F0C}',
	'SketchCircleProxy' : '{C7A68CC9-14FA-11D6-8E01-0010B541CAA8}',
	'EdgeUse' : '{5DF8608D-6B16-11D3-B794-0060B0F159EF}',
	'FlatPunchResults' : '{22A94C59-66DE-4B31-BA10-BCBB774B4AAF}',
	'iMateResultsEnumerator' : '{359AC6D9-E239-4825-BA81-DD8E433FBD1E}',
	'BrowserNodeDefinition' : '{E9E1E669-7C31-486B-A5A6-FD0825ABCB28}',
	'Vector2d' : '{CB69F175-558E-11D3-B793-0060B0F159EF}',
	'DrawingCurveSegment' : '{EEE9F58F-FD0B-4862-AE21-BAE203DFE23E}',
	'ModelingSettings' : '{81F414A9-1062-46BB-A5EE-26575E90DCF0}',
	'FlushiMateDefinition' : '{4A943DD0-592A-4E36-8E2C-D2E9DD54B2F5}',
	'CustomConstraintProxy' : '{5E600148-DA27-47DD-8286-E38CC9466B2F}',
	'EnumType' : '{127400A4-792F-4C40-892E-1AEEA1BBF1E2}',
	'PartEventsObject' : '{CE45B869-6097-4A49-81B4-0FB7A350079C}',
	'TwoLineAngleDimConstraint3D' : '{1EA98FE3-C2EA-4025-8B42-7F91BD2E8DFC}',
	'VertexProxy' : '{46AEA730-4302-11D4-B7AB-0060B0F159EF}',
	'DWGBlockReferenceProxy' : '{93545775-90CE-4E69-B0A5-4E3F23C30677}',
	'FlangeFeature' : '{5475DDC1-3397-46D6-A7A3-E1C34FA5BD7E}',
	'DirectEditDeleteOperation' : '{A7E03766-451A-4BFB-B4CF-FE7F1F258494}',
	'DerivedPartDefinition' : '{79B234B7-D73B-43B2-91BC-75A419703C12}',
	'InterferenceResults' : '{F2286BBF-D48E-4F85-A613-A48AF46893BC}',
	'DrawingViewLabel' : '{C9216F3D-E886-4E75-89AB-D7665FA14AB1}',
	'TransitionalConstraint' : '{3CBE8AAD-3D92-11D5-8DEE-0010B541CAA8}',
	'IRxCylinder' : '{5DF86098-6B16-11D3-B794-0060B0F159EF}',
	'iMateResults' : '{9788ECD5-7355-4AFC-8784-B139CAC98DF3}',
	'BreakOutOperations' : '{600D4AE6-12FB-47E9-86E6-46C8C2A9161E}',
	'TextBoxProxy' : '{C18888BF-ACD9-481C-BE9C-F8921846BE2D}',
	'SketchEquationCurveProxy' : '{70180CA4-8BB6-4D2A-B750-E7A17EF35B99}',
	'FeatureControlFrameStyle' : '{9CB10C50-7F27-4E55-BADE-15A308DB8820}',
	'PointAndPlaneWorkAxisDef' : '{28DD48C1-8D70-11D4-8DDE-0010B541CAA8}',
	'IRxReferenceKey' : '{5DF86026-6B16-11D3-B794-0060B0F159EF}',
	'NonParametricBaseFeatureProxy' : '{0E7B7C43-1EA3-4FA9-95ED-5A1370E81E3F}',
	'TitleBlockDefinitions' : '{A907AEB5-A78F-11D5-8DF8-0010B541CAA8}',
	'IRxTranslatorAddInServer2' : '{863741CF-1A34-11D5-8DEC-0010B541CAA8}',
	'ChamferNote' : '{C71B52F5-89E4-486C-B80E-8AC74650EB34}',
	'TwoPointDistanceDimConstraint3D' : '{C124F1E0-1B29-481D-A0CB-BA8A8AB69764}',
	'SurfaceTextureStylesEnumerator' : '{1DCB7001-C7CD-4637-AC67-296CEB47A86B}',
	'RotateTranslateiMateDefinition' : '{06460F0C-B76C-49E4-B24A-3C60142219B9}',
	'LayersEnumerator' : '{1010554D-5E7D-4D43-A381-89B57B51A708}',
	'InteractionEventsObject' : '{68D1E13F-F6A4-47FD-AAC0-5545A57B712B}',
	'BalloonValueSet' : '{380ED49C-ADD8-47EC-B99E-10D00CE618D7}',
	'BoundaryPatchLoop' : '{4DF199B9-D7C8-4770-9954-2EFF94867CEC}',
	'iFeatureTableColumns' : '{82B8F63A-474B-4DAC-AE2D-E9F5E9BB2C2E}',
	'ProjectedCut' : '{21E8F0AC-DFCD-4800-B07A-6E0C492CC447}',
	'EmbossFeatureProxy' : '{152C858E-87FE-45AD-867B-80622EF4B8AC}',
	'BalloonStylesEnumerator' : '{7D85BA17-75C5-4EBE-AA18-F7E60AE25733}',
	'LeaderStylesEnumerator' : '{9BAC756F-6695-4C8B-A25C-16D29002F114}',
	'iPartTableColumn' : '{8B3FEE20-C49D-495B-AA3E-B90AE49B736B}',
	'FileDialogEventsObject' : '{5993FFB7-877A-4AFA-9BAA-73D627DE0D39}',
	'Documents' : '{70109AA2-63C1-11D2-B78B-0060B0EC020B}',
	'AttributeManager' : '{46D51BD4-B58D-4C94-BA7A-124B184AC687}',
	'Parameters' : '{528C9A32-4173-420A-AD05-B6FBF8382212}',
	'ProjectAssetLibrary' : '{C6EEC114-BE48-4323-B58C-9DF90ED92996}',
	'DrawingBOMColumns' : '{F78F8237-3CAA-467D-AB38-6998DF84B3BE}',
	'SketchLines' : '{8006A018-ECC4-11D4-8DE9-0010B541CAA8}',
	'GraphicsTextureCoordinateSet' : '{FFA15510-CD22-4C40-8DEE-4F846C3D5470}',
	'CustomTables' : '{2A6C1D0D-FAF8-4A31-A9FB-39761F36F814}',
	'iFeatureTableRow' : '{F0684BBA-73A5-45B8-8D38-E64A53735C9E}',
	'UnitAttributes' : '{4B5F98A9-D670-4DDF-A7CE-8AFCEE0990CA}',
	'GripSnapOptions' : '{C032137F-6434-40C1-8DEC-763A191D1EE0}',
	'IRxEnumComponentOccurrences' : '{5DF86012-6B16-11D3-B794-0060B0F159EF}',
	'iMateResult' : '{6D634B29-2066-44CA-AA97-D87A2C95A172}',
	'IRxReferencedFileDescriptor' : '{00C8476D-E79F-11D2-B785-0060B0F159EF}',
	'iFeatureTemplateDescriptor' : '{3C69FF6F-6ADD-4CF5-8E9B-32CBD2B6BBF7}',
	'DecalFeatureProxy' : '{3BE697C4-0242-46F3-A420-27E86761D1D7}',
	'Materials' : '{C45BCCBE-2E53-4C8F-B76A-E6B7815E87E4}',
	'DriveSettingsSink' : '{0F13E8B9-A4C2-4477-93CA-FC2CD0D2C1B1}',
	'BrowserPaneSink' : '{619680F8-EB9A-4F13-8D23-721FE776C955}',
	'PanelBarEventsSink' : '{30A44C19-C3F4-483B-8835-A0A13B849AC0}',
	'IRxEdgeUse' : '{5DF8606B-6B16-11D3-B794-0060B0F159EF}',
	'DrawingBOMs' : '{68517DF3-9E1D-44AA-B12D-08880086D61A}',
	'RepresentationEventsSink' : '{AFD8E323-2B44-4657-89F2-4C50233D287A}',
	'BendPartFeature' : '{2CBE5BA6-3501-4389-AF3F-AD114C0DAB5A}',
	'PathSweepDef' : '{B7FE7553-8DF0-4F70-9798-C85438D3109E}',
	'DWGBlockDefinitionProxy' : '{518CD473-78CC-4B12-A831-AE93812A2774}',
	'DimensionText' : '{AEFA0FB8-139F-469C-8765-26AEA8C0A175}',
	'CommandManager' : '{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}',
	'AnalyticEdgeWorkAxisDef' : '{AF22C0E0-AEBC-4009-BD3E-85EBF9C9ED58}',
	'MidSurfaceFeatures' : '{B148630A-2ECA-4159-8FF2-77CD1B7A79A5}',
	'BorderDefinitions' : '{A907AEB1-A78F-11D5-8DF8-0010B541CAA8}',
	'RibbonPanel' : '{916EFE1C-6493-4712-92D7-CD789914321A}',
	'BendFeatureProxy' : '{E6885A36-3C1C-43A1-9206-81706779DA32}',
	'ClientViews' : '{3D218008-FA54-48CB-89BC-8EFBF3D0B6CC}',
	'SmoothConstraint3D' : '{281176E3-4EDC-4F4E-9804-6716B7B9059D}',
	'NativeBrowserNodeDefinitionObject' : '{FAD47DA5-3A14-4A2C-9A70-7BCDD992D8A7}',
	'WorkAxisProxy' : '{3CBE8AA5-3D92-11D5-8DEE-0010B541CAA8}',
	'SplitFeatureProxy' : '{38C1B59A-0C1B-4076-A22C-291C34157BBD}',
	'TransitionalConstraintProxy' : '{9E7FC002-194A-4CB7-9862-4A3308F586C8}',
	'IRxEnumFileAndReferences' : '{2C9F9B60-8967-11D2-86B1-080009DB6864}',
	'IRxGeometricLocate' : '{5DF86015-6B16-11D3-B794-0060B0F159EF}',
	'ComboBoxDefinitionSink' : '{ACC63CB3-EBF2-48E3-A0F4-48E3FC13ECED}',
	'OrdinateDimension' : '{3DA40E6A-7ED7-4B2C-A2E5-3FCE98B44077}',
	'SingleHemDefinition' : '{BB5A14E9-4213-4965-9B76-F9B33C807FB3}',
	'GraphicsCoordinateSet' : '{956DA506-F82D-4924-A000-C1A66CDB3B49}',
	'ApplicationEventsObject' : '{6ED45F3A-BAF4-41FE-8907-970BB3CA48DF}',
	'SurfaceBodyDefinition' : '{4D662CE2-D29B-42E0-BA74-715C311E5630}',
	'DriveConstraintSettingsSink' : '{ED68898D-4062-47D4-AC28-9B8A1F38CE90}',
	'LoftDefinition' : '{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}',
	'MeasureEventsObject' : '{6AAD65B4-5F61-42C1-830A-A45C60809D76}',
	'SketchBlockDefinitionProxy' : '{83C558ED-EC43-41A6-8FCB-36461DF6319B}',
	'LipFeatureProxy' : '{8742661B-564A-4CE3-A32C-6F08894FB760}',
	'DWGPointProxy' : '{BA9FAF37-B4D2-45C1-BBBE-78E7B8ECB219}',
	'CompositeiMateDefinitionProxy' : '{AE0AA5DD-80A7-4094-B58C-06304422CE34}',
	'DSJointDefinition' : '{055EC023-CD9B-4983-97E2-2EC073939046}',
	'BaselineDimensionSet' : '{6FD094BA-90C4-4C9D-A3B9-DF3A398ECE26}',
	'ThroughAllExtent' : '{AFEA608B-F136-4BD1-995B-333BCAFDED08}',
	'FixedWorkPlaneDef' : '{2C16786F-83FF-11D4-8DDB-0010B541CAA8}',
	'LinearHolePlacementDefinition' : '{06AC6A50-B820-406B-995A-DDA0CCE3E2F5}',
	'SweepFeature' : '{773586BE-A5CE-422F-9036-FAFC8451F011}',
	'ThickenFeatures' : '{F59CE3B0-44CC-4FB5-9C81-7234A25DD381}',
	'CornerFeatures' : '{63F4004E-C9FE-4B75-A7CB-F526543A5C29}',
	'RevisionTables' : '{DB2B25D3-66F3-47CC-9DBF-D6B7468EE76E}',
	'NotebookOptions' : '{CEF827E8-5A0A-452D-83BB-1A88815C1601}',
	'CategoryManager' : '{2B4C4468-F71B-44EE-BAC6-C68CD4F8DDA1}',
	'StylesManager' : '{D93EE206-0CA6-401E-B74E-0D9E4F924751}',
	'PartsList' : '{A907AE87-A78F-11D5-8DF8-0010B541CAA8}',
	'MouseEventsSink' : '{C18BB14E-4FEF-478B-BF34-4690DE9BFC6C}',
	'DSValue' : '{7771DA56-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'BendFeatures' : '{DAA25411-1CB8-4FE2-8F10-1E98740E0889}',
	'DWGBlockDefinition' : '{50E1E017-584C-4C7D-8001-4CF9AEAB7E5E}',
	'ApplicationAddIns' : '{A0481EEA-2031-11D3-B78D-0060B0F159EF}',
	'SketchSpline3D' : '{61FC7221-543B-4885-9546-B700267C98D1}',
	'_VbaImplementationPresentationEvents' : '{33DE76BF-3E58-4EF2-AE90-AA540F2A6C52}',
	'LineAndPlaneWorkAxisDef' : '{28DD48C3-8D70-11D4-8DDE-0010B541CAA8}',
	'WorkAxes' : '{28DD48B5-8D70-11D4-8DDE-0010B541CAA8}',
	'TwoDistancesChamferDef' : '{5B7A8CDA-6F27-4396-9E39-C21A67CA03D3}',
	'SheetFormats' : '{6AC3D773-1202-450D-9CD2-3557B1395C64}',
	'BIMConnectorLink' : '{8E05BCC6-20B2-477A-A318-CB7116D8D0A7}',
	'PartComponentDefinitions' : '{575F2830-2B6A-11D4-B7A8-0060B0F159EF}',
	'HemDefinition' : '{532E5229-0B80-4B9B-968F-69BC150C59CC}',
	'PointCloudPlaneProxy' : '{E65DEA7B-63C6-4F6E-9FCE-8177FEE904F9}',
	'CentermarkStyle' : '{AD4D6527-A103-4FF5-8433-FB90C52B9473}',
	'PitchAndHeightCoilExtent' : '{7F1F13A7-39BD-4720-AB79-E17BC3922427}',
	'ImportedComponentDefinition' : '{903F1E1B-1A0E-4344-820B-CDD9619C0FDC}',
	'FeatureBasedOccurrencePatternProxy' : '{B134AF6F-7FE5-4485-B5E8-493541D94E3F}',
	'DWGArcProxy' : '{E5CFA472-5D23-4486-8D2C-A4D8D564C196}',
	'TrailsEnumerator' : '{F30319D0-9C9E-40BC-96AC-62D2E9302E5B}',
	'ThreePlanesWorkPointDef' : '{28DD48CB-8D70-11D4-8DDE-0010B541CAA8}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

